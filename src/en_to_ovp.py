"""
English (constrained) → OVP translator.

Input must use vocabulary from lexicon.py and follow simple sentence patterns:
  Noun subject:   (This|That) NOUN VERB-PHRASE [(this|that) NOUN].
  Pronoun subject: PRONOUN VERB-PHRASE [(this|that) NOUN].

Object pronoun prefix follows language.py rules (Pronoun.get_object_pronoun()):
  3rd-person singular proximal → 'a'
  3rd-person singular distal   → 'u'
Transitive verb stems are always lenited when an object pronoun prefix is present.
"""

import re
from src.lexicon import (
    NOUN_EN, TRANSITIVE_VERB_EN, INTRANSITIVE_VERB_EN,
    SUBJECT_PRONOUN_EN, GLOTTAL_STOP_NOUNS, conjugate,
)

# ── Reverse vocabulary tables ────────────────────────────────────────────────

# English noun → OVP stem
_NOUN = {en: ovp for ovp, en in NOUN_EN.items()}

# English verb → OVP base stem (first occurrence = base, before lenited form)
_TRANS_VERB: dict[str, str] = {}
for _ovp, _en in TRANSITIVE_VERB_EN.items():
    if _en not in _TRANS_VERB:
        _TRANS_VERB[_en] = _ovp

_INTRANS_VERB: dict[str, str] = {}
for _ovp, _en in INTRANSITIVE_VERB_EN.items():
    if _en not in _INTRANS_VERB:
        _INTRANS_VERB[_en] = _ovp

_VERB = {**_TRANS_VERB, **_INTRANS_VERB}

# English subject pronoun → OVP pronoun (first mapping wins for ambiguous "we", etc.)
_SUBJ_PRON: dict[str, str] = {}
for _ovp, _en in SUBJECT_PRONOUN_EN.items():
    _k = _en.lower()
    if _k not in _SUBJ_PRON:
        _SUBJ_PRON[_k] = _ovp

# ── Build reverse verb-form lookup from conjugate() ─────────────────────────
# Populates irregular-only reverse tables so regular forms use fallback logic.

_PAST_TO_STEM:    dict[str, str] = {}   # "saw"      → "see"
_PART_TO_STEM:    dict[str, str] = {}   # "seen"     → "see"  (for "has seen")
_ONGOING_TO_STEM: dict[str, str] = {}   # "swimming" → "swim" (for "is swimming")

for _stem in set(_VERB.keys()):
    _past = conjugate(_stem, 'ku', '3sg')
    if not _past.endswith('ed'):
        _PAST_TO_STEM[_past] = _stem

    _pü = conjugate(_stem, 'pü', '3sg')
    _part = _pü.removeprefix('has ')
    if not _part.endswith('ed'):
        _PART_TO_STEM[_part] = _stem

    _ti = conjugate(_stem, 'ti', '3sg')
    _oing = _ti.removeprefix('is ')
    # Add to table if irregular (doubled consonant → stem ≠ oing[:-3])
    if not _oing.endswith('ing') or _oing[:-3] != _stem:
        _ONGOING_TO_STEM[_oing] = _stem

# ── Lenition ─────────────────────────────────────────────────────────────────

_LENIS = {'p': 'b', 't': 'd', 'k': 'g', 's': 'z', 'm': 'w̃'}

def _lenite(stem: str) -> str:
    return _LENIS.get(stem[0], stem[0]) + stem[1:]

# ── Object morphology ────────────────────────────────────────────────────────

def _obj_suffix(noun_ovp: str, proximity: str) -> str:
    short = noun_ovp in GLOTTAL_STOP_NOUNS
    if proximity == 'proximal':
        return 'eika' if short else 'neika'
    else:
        return 'oka' if short else 'noka'

def _obj_pronoun(proximity: str) -> str:
    """3rd-person singular object pronoun prefix (language.py rule)."""
    return 'a' if proximity == 'proximal' else 'u'

# ── Verb phrase parser ───────────────────────────────────────────────────────

def _parse_verb_phrase(phrase: str) -> tuple[str, str]:
    """
    Parse an English verb phrase → (english_stem, ovp_tense_suffix).

    Examples:
      "cooks"         → ("cook",  "dü")
      "will cook"     → ("cook",  "wei")
      "is cooking"    → ("cook",  "ti")
      "am swimming"   → ("swim",  "ti")
      "has cooked"    → ("cook",  "pü")
      "have eaten"    → ("eat",   "pü")
      "cooked"        → ("cook",  "ku")
      "saw"           → ("see",   "ku")
      "is going to cook" → ("cook", "gaa-wei")
    """
    phrase = phrase.strip()

    # Going-to future: "am/is/are going to [verb]" — must check before ongoing
    m = re.match(r'^(?:am|is|are) going to (.+)$', phrase)
    if m:
        return m.group(1), 'gaa-wei'

    # Simple future: "will [verb]"
    if phrase.startswith('will '):
        return phrase[5:], 'wei'

    # Ongoing: "am/is/are [Xing]"
    m = re.match(r'^(?:am|is|are) (.+)$', phrase)
    if m:
        oing = m.group(1)
        stem = _ONGOING_TO_STEM.get(oing)
        if stem is None:
            stem = oing[:-3]  # strip -ing
            # un-double consonant if needed (shouldn't reach here for knowns)
            if len(stem) >= 2 and stem[-1] == stem[-2] and stem[-1] not in 'aeiou':
                stem = stem[:-1]
        return stem, 'ti'

    # Perfect: "has/have [participle]"
    m = re.match(r'^(?:has|have) (.+)$', phrase)
    if m:
        part = m.group(1)
        stem = _PART_TO_STEM.get(part) or part[:-2]  # fallback: strip -ed
        return stem, 'pü'

    # Irregular past
    if phrase in _PAST_TO_STEM:
        return _PAST_TO_STEM[phrase], 'ku'

    # Regular past: ends in -ed
    if phrase.endswith('ed'):
        return phrase[:-2], 'ku'

    # Present 3sg: strip -s or -es
    if phrase.endswith('es') and phrase[:-2] in _VERB:
        return phrase[:-2], 'dü'
    if phrase.endswith('s') and phrase[:-1] in _VERB:
        return phrase[:-1], 'dü'

    # Present base form
    if phrase in _VERB:
        return phrase, 'dü'

    raise SyntaxError(f"Cannot parse verb phrase: {phrase!r}")

# ── Sentence parser ──────────────────────────────────────────────────────────

_DETS = {'this': 'proximal', 'that': 'distal'}


def _parse(sentence: str) -> dict:
    """Parse a constrained English sentence into a structured intermediate dict."""
    sentence = sentence.strip().rstrip('.')
    tokens = sentence.split()

    if not tokens:
        raise SyntaxError("Empty sentence")

    if tokens[0].lower() in _DETS:
        # ── Noun subject ─────────────────────────────────────────────────────
        if len(tokens) < 3:
            raise SyntaxError(f"Incomplete noun-subject sentence: {sentence!r}")
        subj_prox = _DETS[tokens[0].lower()]
        subj_en   = tokens[1].lower()
        rest      = tokens[2:]

        if len(rest) >= 2 and rest[-2].lower() in _DETS:
            # Transitive: NounSVO
            obj_prox = _DETS[rest[-2].lower()]
            obj_en   = rest[-1].lower()
            verb_en, tense = _parse_verb_phrase(' '.join(rest[:-2]))
            return {'type': 'NounSVO',
                    'subj': subj_en, 'subj_prox': subj_prox,
                    'verb': verb_en, 'tense': tense,
                    'obj': obj_en,   'obj_prox': obj_prox}
        else:
            # Intransitive: NounSV
            verb_en, tense = _parse_verb_phrase(' '.join(rest))
            return {'type': 'NounSV',
                    'subj': subj_en, 'subj_prox': subj_prox,
                    'verb': verb_en, 'tense': tense}

    else:
        # ── Pronoun subject ──────────────────────────────────────────────────
        pron_en = tokens[0]
        rest    = tokens[1:]

        if len(rest) >= 2 and rest[-2].lower() in _DETS:
            # Transitive: PronounOVS
            obj_prox = _DETS[rest[-2].lower()]
            obj_en   = rest[-1].lower()
            verb_en, tense = _parse_verb_phrase(' '.join(rest[:-2]))
            return {'type': 'PronounOVS',
                    'pron': pron_en,
                    'verb': verb_en, 'tense': tense,
                    'obj': obj_en,   'obj_prox': obj_prox}
        else:
            # Intransitive: PronounVS
            verb_en, tense = _parse_verb_phrase(' '.join(rest))
            return {'type': 'PronounVS',
                    'pron': pron_en,
                    'verb': verb_en, 'tense': tense}

# ── OVP generator ────────────────────────────────────────────────────────────

def _lookup_noun(en: str) -> str:
    if en not in _NOUN:
        raise SyntaxError(f"Unknown noun: {en!r}")
    return _NOUN[en]

def _lookup_verb_trans(en: str) -> str:
    if en not in _TRANS_VERB:
        raise SyntaxError(f"Unknown transitive verb: {en!r}")
    return _TRANS_VERB[en]

def _lookup_verb_intrans(en: str) -> str:
    if en in _INTRANS_VERB:
        return _INTRANS_VERB[en]
    if en in _TRANS_VERB:
        return _TRANS_VERB[en]
    raise SyntaxError(f"Unknown verb: {en!r}")

def _lookup_pron(en: str) -> str:
    key = en.lower()
    if key not in _SUBJ_PRON:
        raise SyntaxError(f"Unknown pronoun: {en!r}")
    return _SUBJ_PRON[key]


def _generate(parsed: dict) -> str:
    """Generate an OVP sentence from a parsed English structure."""
    t = parsed['type']

    if t == 'NounSV':
        subj_ovp = _lookup_noun(parsed['subj'])
        subj_sfx = 'uu' if parsed['subj_prox'] == 'distal' else 'ii'
        verb_ovp = _lookup_verb_intrans(parsed['verb'])
        return f"{subj_ovp}-{subj_sfx} {verb_ovp}-{parsed['tense']}"

    elif t == 'NounSVO':
        subj_ovp = _lookup_noun(parsed['subj'])
        subj_sfx = 'uu' if parsed['subj_prox'] == 'distal' else 'ii'
        obj_ovp  = _lookup_noun(parsed['obj'])
        obj_sfx  = _obj_suffix(obj_ovp, parsed['obj_prox'])
        obj_pron = _obj_pronoun(parsed['obj_prox'])
        verb_ovp = _lenite(_lookup_verb_trans(parsed['verb']))
        return f"{subj_ovp}-{subj_sfx} {obj_ovp}-{obj_sfx} {obj_pron}-{verb_ovp}-{parsed['tense']}"

    elif t == 'PronounVS':
        pron_ovp = _lookup_pron(parsed['pron'])
        verb_ovp = _lookup_verb_intrans(parsed['verb'])
        return f"{verb_ovp}-{parsed['tense']} {pron_ovp}"

    elif t == 'PronounOVS':
        pron_ovp = _lookup_pron(parsed['pron'])
        obj_ovp  = _lookup_noun(parsed['obj'])
        obj_sfx  = _obj_suffix(obj_ovp, parsed['obj_prox'])
        obj_pron = _obj_pronoun(parsed['obj_prox'])
        verb_ovp = _lenite(_lookup_verb_trans(parsed['verb']))
        return f"{obj_ovp}-{obj_sfx} {pron_ovp} {obj_pron}-{verb_ovp}-{parsed['tense']}"

    raise SyntaxError(f"Unknown sentence type: {t}")

# ── Public API ───────────────────────────────────────────────────────────────

def translate_to_ovp(english: str) -> str:
    """
    Translate a constrained English sentence to OVP.
    Raises SyntaxError if the sentence cannot be parsed or contains unknown words.
    """
    return _generate(_parse(english))


if __name__ == "__main__":
    import sys
    sentence = ' '.join(sys.argv[1:]).strip()
    if sentence:
        print(translate_to_ovp(sentence))
    else:
        examples = [
            "That bird climbed.",
            "That jackrabbit smiles.",
            "That wickiup will sit.",
            "That coyote cooks that fish.",
            "That bird will see this horse.",
            "That jackrabbit is eating this worm.",
            "I am swimming.",
            "He/she/it sits.",
            "I have laughed.",
            "We sleep.",
            "I saw that fish.",
            "We ate this dog.",
        ]
        print(f"{'English':<45} {'OVP'}")
        print("-" * 75)
        for s in examples:
            print(f"{s:<45} {translate_to_ovp(s)}")
