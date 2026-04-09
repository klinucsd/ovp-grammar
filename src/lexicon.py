"""
OVP Lexicon — single source of truth for vocabulary.
Both the grammar and translator reference this file.
Replaces the duplicated vocabulary in ovp-lang/vocab.py
and sentences-api/sentence-builder.js.
"""

# Nouns: OVP stem -> English
NOUN_EN = {
    "isha'":     "coyote",
    "isha'pugu": "dog",
    "kidi'":     "cat",
    "pugu":      "horse",
    "wai":       "rice",
    "tüba":      "pinenuts",
    "maishibü":  "corn",
    "paya":      "water",
    "payahuupü": "river",
    "katünu":    "chair",
    "toyabi":    "mountain",
    "tuunapi":   "food",
    "pasohobü":  "tree",
    "nobi":      "house",
    "toni":      "wickiup",
    "apo":       "cup",
    "küna":      "wood",
    "tübbi":     "rock",
    "tabuutsi'": "cottontail",
    "kamü":      "jackrabbit",
    "aaponu'":   "apple",
    "tüsüga":    "weasel",
    "mukita":    "lizard",
    "wo'ada":    "mosquito",
    "wükada":    "bird snake",
    "wo'abi":    "worm",
    "aingwü":    "squirrel",
    "tsiipa":    "bird",
    "tüwoobü":   "earth",
    "koopi'":    "coffee",
    "pahabichi": "bear",
    "pagwi":     "fish",
    "kwadzi":    "tail",
}

# Transitive verbs: OVP stem -> English base form
# Both base and lenited forms map to the same English
TRANSITIVE_VERB_EN = {
    "tüka":  "eat",   "düka":  "eat",    # t→d lenition
    "puni":  "see",   "buni":  "see",
    "hibi":  "drink",
    "naka":  "hear",
    "kwana": "smell", "gwana": "smell",  # k→g lenition
    "kwati": "hit",   "gwati": "hit",
    "yadohi":"talk to",
    "naki":  "chase",
    "tsibui":"climb",
    "sawa":  "cook",  "zawa":  "cook",   # s→z lenition
    "tama'i":"find",
    "nia":   "read",
    "mui":   "write", "w\u0303ui": "write",  # m→w̃ lenition
    "nobini":"visit",
}

# Intransitive verbs: OVP stem -> English base form
INTRANSITIVE_VERB_EN = {
    "katü":     "sit",
    "üwi":      "sleep",
    "kwisha'i": "sneeze",
    "poyoha":   "run",
    "mia":      "go",
    "hukaw\u0303ia": "walk",
    "wünü":     "stand",
    "habi":     "lie down",
    "yadoha":   "talk",
    "kwatsa'i": "fall",
    "waakü":    "work",
    "wükihaa":  "smile",
    "hubiadu":  "sing",
    "nishua'i": "laugh",
    "tsibui":   "climb",
    "tübinohi": "play",
    "yotsi":    "fly",
    "nüga":     "dance",
    "pahabi":   "swim",
    "tünia":    "read",
    "tümui":    "write",
    "tsiipe'i": "chirp",
}

VERB_EN = {**TRANSITIVE_VERB_EN, **INTRANSITIVE_VERB_EN}

# Subject pronouns: OVP -> English
SUBJECT_PRONOUN_EN = {
    "nüü":     "I",
    "uhu":     "he/she/it",
    "uhuw\u0303a":  "they",
    "mahu":    "he/she/it",
    "mahuw\u0303a": "they",
    "ihi":     "this",
    "ihiw\u0303a":  "these",
    "taa":     "you and I",
    "nüügwa":  "we",
    "taagwa":  "we",
    "üü":      "you",
    "üügwa":   "you all",
}

# Grammatical person for each subject pronoun (used for English verb agreement)
PRONOUN_PERSON = {
    "nüü":     "1sg",   # I
    "uhu":     "3sg",   # he/she/it
    "uhuw\u0303a":  "3pl",   # they
    "mahu":    "3sg",   # he/she/it (evidential)
    "mahuw\u0303a": "3pl",   # they (evidential)
    "ihi":     "3sg",   # this
    "ihiw\u0303a":  "3pl",   # these
    "taa":     "1pl",   # you and I
    "nüügwa":  "1pl",   # we
    "taagwa":  "1pl",   # we
    "üü":      "2sg",   # you
    "üügwa":   "2pl",   # you all
}

# Object pronouns: OVP -> English
OBJECT_PRONOUN_EN = {
    "i":   "me",
    "u":   "him/her/it",
    "ui":  "them",
    "ma":  "him/her/it",
    "mai": "them",
    "a":   "him/her/it",
    "ai":  "them",
    "ni":  "us",
    "tei": "us",
    "ta":  "us",
    "ü":   "you",
    "üi":  "you all",
}

# Proximity suffixes -> English determiner
PROXIMITY = {
    "ii":    ("This",  "this"),   # (capitalized, lowercase)
    "uu":    ("That",  "that"),
    "eika":  ("This",  "this"),
    "neika": ("This",  "this"),
    "oka":   ("That",  "that"),
    "noka":  ("That",  "that"),
}

# Irregular English verb forms: verb_base -> {tense_suffix -> form}
# Covers past (ku), perfect (pü), and ongoing (ti) where rules don't apply
_IRREGULAR = {
    "see":      {"ku": "saw",    "pü": "seen",    "ti": "seeing"},
    "eat":      {"ku": "ate",    "pü": "eaten",   "ti": "eating"},
    "drink":    {"ku": "drank",  "pü": "drunk",   "ti": "drinking"},
    "go":       {"ku": "went",   "pü": "gone",    "ti": "going"},
    "write":    {"ku": "wrote",  "pü": "written", "ti": "writing"},
    "read":     {"ku": "read",   "pü": "read",    "ti": "reading"},
    "find":     {"ku": "found",  "pü": "found",   "ti": "finding"},
    "hit":      {"ku": "hit",    "pü": "hit",     "ti": "hitting"},
    "hear":     {"ku": "heard",  "pü": "heard",   "ti": "hearing"},
    "swim":     {"ku": "swam",   "pü": "swum",   "ti": "swimming"},
    "sit":      {"ti": "sitting"},
    "run":      {"ku": "ran",    "pü": "run",    "ti": "running"},
    "lie down": {"ti": "lying down"},
    "talk to":  {"ku": "talked to", "pü": "talked to", "ti": "talking to"},
    "climb":    {"ku": "climbed", "pü": "climbed", "ti": "climbing"},
    "laugh":    {"ku": "laughed", "pü": "laughed", "ti": "laughing"},
}

def _be(person: str) -> str:
    """Return correct present form of 'be' for the given grammatical person."""
    if person == "1sg": return "am"
    if person == "3sg": return "is"
    return "are"

def _have(person: str) -> str:
    """Return 'has' for 3rd-person-singular, 'have' otherwise."""
    return "has" if person == "3sg" else "have"

def _third_sg_s(verb: str) -> str:
    """Add 3rd-person-singular present -s, handling multi-word verbs and irregulars."""
    _special = {"go": "goes", "do": "does"}
    if verb in _special:
        return _special[verb]
    words = verb.split(None, 1)          # "talk to" -> ["talk", "to"]
    if len(words) > 1:
        return _third_sg_s(words[0]) + " " + words[1]
    if verb.endswith(("s", "sh", "ch", "x", "z")):
        return verb + "es"
    if verb.endswith("y") and verb[-2] not in "aeiou":
        return verb[:-1] + "ies"
    return verb + "s"

def conjugate(verb: str, tense: str, person: str = "3sg") -> str:
    """Apply tense suffix to English verb, handling irregular forms and subject agreement."""
    irreg = _IRREGULAR.get(verb, {}).get(tense)
    if irreg:
        if tense == "ku":  return irreg
        if tense == "ti":  return f"{_be(person)} {irreg}"
        if tense == "pü":  return f"{_have(person)} {irreg}"
        return irreg
    return {
        "ku":      f"{verb}ed",
        "ti":      f"{_be(person)} {verb}ing",
        "dü":      _third_sg_s(verb) if person == "3sg" else verb,
        "wei":     f"will {verb}",
        "gaa-wei": f"{_be(person)} going to {verb}",
        "pü":      f"{_have(person)} {verb}ed",
    }.get(tense, verb)

# Nouns that end in glottal stop (use short object suffix -eika/-oka)
# Only nouns whose OVP stem ends in "'" qualify (language.py: target_word.endswith("'"))
GLOTTAL_STOP_NOUNS = {
    "isha'", "kidi'", "tabuutsi'", "aaponu'", "koopi'", "kwisha'i"
}

def object_suffix(noun: str, proximity: str) -> str:
    """Return the correct object suffix for a noun given proximity."""
    short = noun in GLOTTAL_STOP_NOUNS
    if proximity == "proximal":
        return "eika" if short else "neika"
    else:
        return "oka" if short else "noka"
