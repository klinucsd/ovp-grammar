"""
Tests for OVP -> English translator.
Sentences taken from the paper's Appendix A (Table 3).

OVP word order:
  - Noun subject:   [subject-suffix] [object-suffix] [pronoun-verb-tense]  (SOV)
  - Pronoun subject:[object-suffix]  [pronoun]       [pronoun-verb-tense]  (OVS)
  - Intransitive:   [verb-tense] [pronoun]  (verb first, pronoun after)
"""

import pytest
from src.translator import translate


# ----------------------------------------------------------------
# Noun Subject — Intransitive (NounSV)
# ----------------------------------------------------------------

def test_noun_sv_climb():
    assert translate("tsiipa-uu tsibui-ku") == "That bird climbed."

def test_noun_sv_smile():
    assert translate("kamü-uu wükihaa-dü") == "That jackrabbit smiles."

def test_noun_sv_sit():
    assert translate("toni-uu katü-wei") == "That wickiup will sit."

def test_noun_sv_stand():
    assert translate("toni-uu wünü-ti") == "That wickiup is standing."


# ----------------------------------------------------------------
# Noun Subject — Transitive (NounSVO)
# ----------------------------------------------------------------

def test_noun_svo_cook():
    assert translate("isha'-uu pagwi-noka u-zawa-dü") == "That coyote cooks that fish."

def test_noun_svo_hear():
    assert translate("pahabichi-ii wo'abi-noka ui-naka-dü") == "This bear hears that worm."

def test_noun_svo_see_future():
    assert translate("tsiipa-uu pugu-neika ma-buni-wei") == "That bird will see this horse."

def test_noun_svo_eat_ongoing():
    assert translate("kamü-uu wo'abi-neika a-düka-ti") == "That jackrabbit is eating this worm."

def test_noun_svo_drink_perfect():
    assert translate("isha'-uu tüba-neika ai-hibi-pü") == "That coyote has drunk this pinenuts."


# ----------------------------------------------------------------
# Pronoun Subject — Intransitive (PronounVS)
# ----------------------------------------------------------------

def test_pronoun_vs_swim():
    assert translate("pahabi-ti nüü") == "I am swimming."

def test_pronoun_vs_sit():
    assert translate("katü-dü uhu") == "He/she/it sits."

def test_pronoun_vs_laugh():
    assert translate("nishua'i-pü nüü") == "I have laughed."

def test_pronoun_vs_sleep():
    # From paper appendix: "üwi-ku ihiw̃a" -> "These slept."
    assert translate("üwi-dü nüügwa") == "We sleep."


# ----------------------------------------------------------------
# Pronoun Subject — Transitive (PronounOVS)
# ----------------------------------------------------------------

def test_pronoun_ovs_see():
    # pagwi-noka nüü ma-puni-ku = I saw that fish
    assert translate("pagwi-noka nüü ma-puni-ku") == "I saw that fish."

def test_pronoun_ovs_eat():
    # isha'pugu-neika nüügwa ma-düka-ku = We ate this dog
    assert translate("isha'pugu-neika nüügwa ma-düka-ku") == "We ate this dog."

def test_pronoun_ovs_eat_lenited():
    # düka is the lenited form of tüka (t->d), used when object pronoun is present
    assert translate("isha'pugu-neika nüügwa ma-düka-ku") == "We ate this dog."


# ----------------------------------------------------------------
# Grammar enforcement: invalid sentences must raise SyntaxError
# ----------------------------------------------------------------

def test_rejects_unknown_word():
    with pytest.raises(SyntaxError):
        translate("blorp-uu zorp-noka u-zawa-dü")

def test_rejects_wrong_word_order():
    # Pronoun before verb is invalid OVP order for intransitive
    with pytest.raises(SyntaxError):
        translate("nüü pahabi-ti")

def test_rejects_missing_tense():
    with pytest.raises(SyntaxError):
        translate("isha'-uu pagwi-noka u-zawa")

def test_rejects_missing_object_suffix():
    with pytest.raises(SyntaxError):
        translate("isha'-uu pagwi u-zawa-dü")
