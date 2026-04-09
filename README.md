# OVP Grammar — Bidirectional Owens Valley Paiute ↔ English Translator

A formal grammar-based translation system for **Owens Valley Paiute (OVP)**, a critically endangered Uto-Aztecan language spoken in the Owens Valley of California.

This code is based entirely on the work of Jared Coleman et al. as described in their AmericasNLP 2024 paper. The vocabulary, morphological rules, and sentence patterns all originate from their research. This repository applies a formal language approach (ANTLR4 grammar) to the same data as a proof of concept — to explore whether a deterministic, rule-based system for OVP processing.

---

## Overview

This project uses [ANTLR4](https://www.antlr.org/) to define a formal grammar for OVP and implements bidirectional translation between OVP and English for simple declarative sentences.

| Direction | Approach |
|---|---|
| OVP → English | ANTLR4 parser + Visitor pattern |
| English → OVP | Reverse vocabulary lookup + OVP morphology rules |

The grammar encodes OVP's core syntactic and morphological features:
- **Word order**: SOV for noun subjects, OVS for pronoun subjects, verb-first for intransitive pronoun sentences
- **Morphology**: subject suffixes (`-uu`/`-ii`), object suffixes (`-noka`/`-neika`/`-oka`/`-eika`), tense suffixes, object pronoun prefixes
- **Lenition**: consonant weakening on transitive verb stems (p→b, t→d, k→g, s→z, m→w̃)
- **Proximity deixis**: proximal (`ii`/`this`) vs distal (`uu`/`that`)
- **Subject-verb agreement** in English output

---

## Requirements

- [Docker](https://www.docker.com/) and Docker Compose

Java and ANTLR4 are bundled inside the Docker image — nothing else is needed on the host machine.

---

## Quick Start

```bash
# 1. Build the Docker image (first time only)
make build

# 2. Translate OVP → English
make ovp2en SENTENCE="isha'-uu pagwi-noka u-zawa-dü"
# That coyote cooks that fish.

# 3. Translate English → OVP
make en2ovp SENTENCE="That coyote cooks that fish."
# isha'-uu pagwi-noka u-zawa-dü

# 4. Show parse tree
make parse SENTENCE="isha'-uu pagwi-noka u-zawa-dü"

# 5. Run all tests
make test
```

---

## Commands

| Command | Description |
|---|---|
| `make build` | Build the Docker image |
| `make ovp2en SENTENCE="..."` | Translate OVP → English |
| `make en2ovp SENTENCE="..."` | Translate English → OVP |
| `make parse SENTENCE="..."` | Show ANTLR4 parse tree for an OVP sentence |
| `make test` | Run all 43 tests |
| `make generate` | Recompile `grammar/OVP.g4` after editing |
| `make shell` | Interactive shell inside the container |

Run any command without `SENTENCE` to see a built-in demo.

See [COMMANDS.md](COMMANDS.md) for full documentation including Docker commands and workflows.

---

## Examples

### OVP → English

```
OVP                                      English
isha'-uu pagwi-noka u-zawa-dü            That coyote cooks that fish.
pahabi-ti nüü                            I am swimming.
pahabichi-ii wo'abi-noka u-naka-dü       This bear hears that worm.
tsiipa-uu tsibui-ku                      That bird climbed.
katü-dü uhu                              He/she/it sits.
nishua'i-pü nüü                          I have laughed.
```

### English → OVP

```
English                                  OVP
That bird climbed.                       tsiipa-uu tsibui-ku
That jackrabbit is eating this worm.     kamü-uu wo'abi-neika a-düka-ti
That coyote has drunk this pinenuts.     isha'-uu tüba-neika a-hibi-pü
I am swimming.                           pahabi-ti nüü
We sleep.                                üwi-dü nüügwa
I saw that fish.                         pagwi-noka nüü u-buni-ku
```

### Parse tree

```
$ make parse SENTENCE="isha'-uu pagwi-noka u-zawa-dü"

sentence
  nounSubjectSentence
    subjectNoun
      isha'
      -
      subjectSuffix
        uu
    objectNoun
      pagwi
      -
      objectSuffix
        noka
    transitiveVerb
      u
      -
      zawa
      -
      tense
        dü
```

---

## Sentence Types Supported

| OVP Pattern | Word Order | Example |
|---|---|---|
| Noun + intransitive | SOV (no object) | `tsiipa-uu tsibui-ku` — That bird climbed. |
| Noun + transitive | SOV | `isha'-uu pagwi-noka u-zawa-dü` — That coyote cooks that fish. |
| Pronoun + intransitive | Verb-Subject | `pahabi-ti nüü` — I am swimming. |
| Pronoun + transitive | OVS | `pagwi-noka nüü u-buni-ku` — I saw that fish. |

### Tenses

| OVP suffix | Meaning | English example |
|---|---|---|
| `-dü` | present | cooks |
| `-ku` | past | cooked / saw |
| `-ti` | ongoing | is cooking |
| `-wei` | future | will cook |
| `-pü` | perfect | has cooked |
| `-gaa-wei` | going-to | is going to cook |

---

## Project Structure

```
ovp-grammar/
├── grammar/
│   └── OVP.g4              # ANTLR4 grammar — OVP syntax and morphology rules
├── src/
│   ├── lexicon.py          # Vocabulary + English verb conjugation
│   ├── translator.py       # OVP → English (ANTLR4 Visitor)
│   ├── en_to_ovp.py        # English → OVP (rule-based)
│   └── generated/          # Auto-generated by ANTLR4 (do not edit)
├── tests/
│   ├── test_translator.py  # 20 tests: OVP → English
│   └── test_en_to_ovp.py   # 23 tests: English → OVP + round-trips
├── COMMANDS.md             # Full command reference
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── Makefile
```

---

## Vocabulary

The lexicon (`src/lexicon.py`) contains:
- **33 nouns**: coyote, dog, cat, horse, bear, fish, bird, jackrabbit, and more
- **25 transitive verbs**: eat, see, drink, hear, cook, find, and more (including lenited forms)
- **22 intransitive verbs**: sit, sleep, swim, run, climb, laugh, and more
- **12 subject pronouns**: nüü (I), uhu (he/she/it), nüügwa (we), üü (you), and more

The English → OVP direction accepts exactly the English words that appear in the lexicon — a well-defined, finite vocabulary.

---

## How OVP → English Translation Works

OVP is morphologically rich: each word carries grammatical information as suffixes and prefixes separated by hyphens. For example:

```
isha'-uu   pagwi-noka   u-zawa-dü
 noun-subj  noun-obj    obj_pron-verb-tense
 coyote-that  fish-that  it-cook(lenited)-present
→ "That coyote cooks that fish."
```

Translation proceeds in two steps:

**Step 1 — Parse.** The ANTLR4 grammar (`grammar/OVP.g4`) reads the OVP sentence and builds a parse tree. The grammar knows exactly what morphemes are legal, what order they must appear in, and which combinations are valid. Invalid sentences are rejected immediately with an error — no silent failure.

**Step 2 — Visit.** A Visitor (`src/translator.py`) walks the parse tree node by node. At each node it performs a simple lookup:
- `isha'` → `NOUN_EN["isha'"]` → `"coyote"`
- `-uu` → `PROXIMITY["uu"]` → `"That"`
- `-noka` → `PROXIMITY["noka"]` → `"that"`
- `zawa` → `VERB_EN["zawa"]` → `"cook"` (lenited form of `sawa`, same English meaning)
- `-dü` + subject is noun (3rd person singular) → `conjugate("cook", "dü", "3sg")` → `"cooks"`

The sentence structure (SOV vs OVS vs verb-first) is determined by which grammar rule matched, so word order is handled structurally, not by string manipulation.

No English grammar is needed for this direction — OVP's own grammar drives everything.

---

## How English → OVP Translation Works

There is no formal grammar for English in this system. Instead, translation relies on two observations:

1. **The English input is constrained.** We only accept English sentences that express concepts OVP can express — meaning the vocabulary is exactly the set of words in the lexicon (~33 nouns, ~47 verbs, known pronouns and determiners). This makes the English input space finite and fully enumerable.

2. **English sentence structure is simple and regular.** The supported patterns are:
   - `(This|That) NOUN VERB-PHRASE [(this|that) NOUN].` — noun subject sentence
   - `PRONOUN VERB-PHRASE [(this|that) NOUN].` — pronoun subject sentence

Given these constraints, translation proceeds in two steps:

**Step 1 — Parse English structurally.** The sentence is split into tokens. The first token identifies the sentence type (determiner → noun subject, known pronoun → pronoun subject). The last two tokens identify whether an object is present. The remaining tokens form the verb phrase.

The verb phrase is parsed by recognising a small set of patterns:

| English verb phrase | Detected as | OVP tense |
|---|---|---|
| `cooks` / `cook` | present (3sg or base) | `-dü` |
| `will cook` | future | `-wei` |
| `is/am/are cooking` | ongoing | `-ti` |
| `has/have cooked` | perfect | `-pü` |
| `cooked` / `saw` / `ate` | past (regular or irregular) | `-ku` |
| `is going to cook` | going-to future | `-gaa-wei` |

Irregular past and participle forms (saw, eaten, drank, swum, etc.) are resolved through a reverse lookup table built automatically from the lexicon.

**Step 2 — Generate OVP morphology.** Given the parsed structure, OVP is assembled rule by rule:
- Look up the OVP noun stem from the English noun: `"coyote"` → `"isha'"`
- Select subject suffix by proximity: `"that"` → `-uu`
- Look up the OVP verb stem: `"cook"` → `"sawa"` (base form)
- Apply lenition to the verb stem (always required for transitive verbs): `sawa` → `zawa` (s→z)
- Select object pronoun prefix by proximity: `"that"` (distal) → `u`
- Select object suffix: `"fish"` (`pagwi`, no glottal stop, distal) → `-noka`
- Assemble in OVP word order (SOV for noun subject): `isha'-uu pagwi-noka u-zawa-dü`

Every rule in this process is an explicit, inspectable line of Python code — there is no guessing or probabilistic inference.

---

## Scope and Limitations

**Currently supported**: simple declarative sentences (subject + verb, or subject + verb + object).

**Not yet implemented**:
- Interrogative sentences (questions)
- Negation
- Relative clauses
- Nominalization (verb used as noun)
- Possessives

These are natural extensions once the corresponding OVP grammatical rules are documented.

---

## Background

The vocabulary, grammar rules, and sentence patterns in this system are derived entirely from the work of Jared Coleman and colleagues, documented in their AmericasNLP 2024 paper. 

**Reference:** Jared Coleman et al., "LLM-Assisted Rule Based Machine Translation for Low/No-Resource Languages," AmericasNLP 2024.
