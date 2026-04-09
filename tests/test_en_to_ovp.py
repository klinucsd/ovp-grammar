"""
Tests for English -> OVP translator.

Object pronoun prefix follows language.py (Pronoun.get_object_pronoun()):
  3rd-person singular proximal → 'a'
  3rd-person singular distal   → 'u'
Transitive verb stems are always lenited (p→b, t→d, k→g, s→z, m→w̃).

Note: some sentences in the paper's Appendix A use 'ma' instead of 'a'/'u'
for the object pronoun — this appears to be an inconsistency in the source
material. Our generator follows the rules in language.py.
"""

import pytest
from src.en_to_ovp import translate_to_ovp


# ── Noun Subject — Intransitive (NounSV) ─────────────────────────────────────

def test_noun_sv_climb():
    assert translate_to_ovp("That bird climbed.") == "tsiipa-uu tsibui-ku"

def test_noun_sv_smile():
    assert translate_to_ovp("That jackrabbit smiles.") == "kamü-uu wükihaa-dü"

def test_noun_sv_sit():
    assert translate_to_ovp("That wickiup will sit.") == "toni-uu katü-wei"

def test_noun_sv_stand():
    assert translate_to_ovp("That wickiup is standing.") == "toni-uu wünü-ti"

def test_noun_sv_proximal():
    assert translate_to_ovp("This bear swam.") == "pahabichi-ii pahabi-ku"


# ── Noun Subject — Transitive (NounSVO) ──────────────────────────────────────

def test_noun_svo_cook():
    # distal obj → 'u'; s→z lenition
    assert translate_to_ovp("That coyote cooks that fish.") == "isha'-uu pagwi-noka u-zawa-dü"

def test_noun_svo_hear():
    # distal obj → 'u'; n unchanged (no lenition)
    assert translate_to_ovp("This bear hears that worm.") == "pahabichi-ii wo'abi-noka u-naka-dü"

def test_noun_svo_see_future():
    # proximal obj → 'a'; p→b lenition
    assert translate_to_ovp("That bird will see this horse.") == "tsiipa-uu pugu-neika a-buni-wei"

def test_noun_svo_eat_ongoing():
    # proximal obj → 'a'; t→d lenition; glottal-stop noun → no short suffix
    assert translate_to_ovp("That jackrabbit is eating this worm.") == "kamü-uu wo'abi-neika a-düka-ti"

def test_noun_svo_drink_perfect():
    # proximal obj → 'a'; h unchanged
    assert translate_to_ovp("That coyote has drunk this pinenuts.") == "isha'-uu tüba-neika a-hibi-pü"

def test_noun_svo_glottal_stop_obj():
    # isha' ends in glottal stop → short suffix -oka (distal) or -eika (proximal)
    assert translate_to_ovp("That bear ate that coyote.") == "pahabichi-uu isha'-oka u-düka-ku"


# ── Pronoun Subject — Intransitive (PronounVS) ───────────────────────────────

def test_pronoun_vs_swim():
    assert translate_to_ovp("I am swimming.") == "pahabi-ti nüü"

def test_pronoun_vs_sit():
    assert translate_to_ovp("He/she/it sits.") == "katü-dü uhu"

def test_pronoun_vs_laugh():
    assert translate_to_ovp("I have laughed.") == "nishua'i-pü nüü"

def test_pronoun_vs_sleep():
    assert translate_to_ovp("We sleep.") == "üwi-dü nüügwa"


# ── Pronoun Subject — Transitive (PronounOVS) ────────────────────────────────

def test_pronoun_ovs_see():
    # distal obj → 'u'; p→b lenition
    assert translate_to_ovp("I saw that fish.") == "pagwi-noka nüü u-buni-ku"

def test_pronoun_ovs_eat():
    # proximal obj → 'a'; t→d lenition; isha'pugu not a glottal-stop noun → -neika
    assert translate_to_ovp("We ate this dog.") == "isha'pugu-neika nüügwa a-düka-ku"


# ── Round-trip: English → OVP → English ─────────────────────────────────────

def test_roundtrip_noun_sv():
    from src.translator import translate
    ovp = translate_to_ovp("That bird climbed.")
    assert translate(ovp) == "That bird climbed."

def test_roundtrip_noun_svo():
    from src.translator import translate
    ovp = translate_to_ovp("That coyote cooks that fish.")
    assert translate(ovp) == "That coyote cooks that fish."

def test_roundtrip_pronoun_vs():
    from src.translator import translate
    ovp = translate_to_ovp("I am swimming.")
    assert translate(ovp) == "I am swimming."

def test_roundtrip_pronoun_ovs():
    from src.translator import translate
    ovp = translate_to_ovp("I saw that fish.")
    assert translate(ovp) == "I saw that fish."


# ── Error handling ────────────────────────────────────────────────────────────

def test_rejects_unknown_noun():
    with pytest.raises(SyntaxError):
        translate_to_ovp("That dragon swam.")

def test_rejects_unknown_verb():
    with pytest.raises(SyntaxError):
        translate_to_ovp("That bird flew.")
