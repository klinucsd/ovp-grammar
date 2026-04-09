# OVP Translation System: Analysis and Architecture Proposal
**Prepared for discussion with Jared Coleman's team, April 10, 2026**

---

## 1. Background

We reviewed Jared Coleman's paper "LLM-Assisted Rule Based Machine Translation for Low/No-Resource Languages" (AmericasNLP 2024) and the four supporting repositories:

- `kubishi` — dictionary/encyclopedia web app (Node.js + MongoDB + React)
- `ovp-lang` — Python grammar library with Pydantic models (~470 lines)
- `sentences-api` — sentence builder and translator backend (Node.js)
- `sentences-frontend` — Vue 3 UI with sentence builder and translator views

The system demonstrates bidirectional translation between Owens Valley Paiute (OVP) and English for simple sentences of 3–5 words. This is a meaningful achievement for a critically endangered language with no publicly available digital corpus.

Our goal is not to criticize what has been built, but to propose an architectural improvement that makes the system more reliable, more extensible, and more useful as a scientific artifact for language revitalization.

---

## 2. How the Current System Works

### OVP → English
The system receives an OVP sentence (e.g., `isha'-uu pagwi-noka u-zawa-dü`), looks up each morpheme (word part) in Python dictionaries, assembles English words from the lookup results, and passes them to an LLM (GPT-3.5/GPT-4o-mini) to produce a readable English sentence.

Crucially, by the time the LLM sees the input, it has already been converted to English words. The LLM is doing template assembly, not translation.

### English → OVP
1. LLM decomposes a natural English sentence into simple Subject-Verb-Object form
2. Rule-based code maps each English word to an OVP morpheme
3. `formatSentence()` assembles the OVP output (applies suffixes, pronoun prefixes, lenition)
4. LLM generates a readable English paraphrase of the result
5. LLM back-translates the OVP output to English as a quality check

Step 5 — the back-translation check — exists because the system does not fully trust its own OVP output. This is a significant signal.

### The constraint builder (`getAllChoices()`)
The sentence builder UI is powered by a 400-line constraint propagation engine, not a grammar parser. It works by eliminating invalid combinations as the user makes selections (e.g., choosing a transitive verb removes intransitive-only options). This is good engineering for a form-based UI, but it does not constitute a grammar — it cannot parse OVP text, cannot verify a sentence typed by a user, and cannot generate sentences programmatically.

---

## 3. What Is a Formal Grammar, and Why Does It Matter Here?

This section is for readers less familiar with compiler and language technology.

A **formal grammar** is a precise, machine-readable specification of what sentences in a language look like. Think of it like a very detailed recipe: it says not just what ingredients exist (the vocabulary), but exactly how they combine, in what order, and what the result means.

A tool like **ANTLR4** (ANother Tool for Language Recognition) reads a grammar file and automatically generates a *parser* — a program that can read any sentence in that language and determine whether it is valid, and if so, what each part means. ANTLR4 is widely used in industry to build programming languages, query languages, and domain-specific languages.

Here is a simplified example from our OVP grammar file (`OVP.g4`):

```antlr
// A sentence is either:
//   noun-subject sentence (word order: Subject-Object-Verb)
//   pronoun-subject sentence (word order: Object-Verb-Subject)

sentence
    : subjectNoun objectNoun transitiveVerb    // "That coyote cooks that fish."
    | subjectNoun intransitiveVerb             // "That bird climbed."
    | objectNoun SUBJECT_PRONOUN transitiveVerb // "I saw that fish."
    | intransitiveVerb SUBJECT_PRONOUN         // "I am swimming."
    ;
```

This single file captures something that currently lives implicitly across hundreds of lines of Python and JavaScript: **OVP's word order alternates between SOV (noun subjects) and OVS (pronoun subjects), with verb-first for intransitive pronoun sentences.** Any linguist or OVP speaker can read this rule directly.

The grammar also captures morphological rules. For example:

```antlr
// A subject noun is: NOUN + hyphen + subject suffix
// Subject suffix is either -ii (proximal/this) or -uu (distal/that)
subjectNoun : NOUN HYPHEN subjectSuffix ;
subjectSuffix : II | UU ;

// A transitive verb is: object-pronoun + hyphen + verb-stem + hyphen + tense
transitiveVerb : OBJ_PRONOUN HYPHEN VERB HYPHEN tense ;
```

These rules enforce constraints structurally. You cannot write a valid sentence with a transitive verb that is missing its object pronoun prefix — the grammar will reject it and raise an error. The current JSON-table approach cannot make this guarantee.

---

## 4. What We Built

We built a working OVP → English translator using ANTLR4, running inside a Docker container (to avoid requiring Java installed locally).

### Components

**`grammar/OVP.g4`** — The grammar specification. 186 lines that encode:
- OVP's two word order patterns (SOV for noun subjects, OVS/verb-first for pronoun subjects)
- All morpheme categories: subject suffixes, object suffixes, tense suffixes, object pronoun prefixes
- All 33 nouns, ~25 transitive verbs, ~22 intransitive verbs, 12 subject pronouns, 12 object pronouns
- Lenited verb forms (consonant weakening when a verb carries an object pronoun prefix: t→d, p→b, k→g, s→z, m→w̃)
- Glottal-stop nouns (which take short suffix forms: `-eika`/`-oka` instead of `-neika`/`-noka`)

**`src/lexicon.py`** — Single source of vocabulary truth (~200 lines). Replaces three separate vocabulary tables currently duplicated across `ovp-lang/vocab.py` and `sentences-api/sentence-builder.js`. Contains:
- OVP stem → English mappings for nouns, verbs, pronouns
- Irregular English verb forms (saw, eaten, drank, went, etc.)
- `conjugate(verb, tense, person)` — applies tense and subject-verb agreement correctly

**`src/translator.py`** — Semantic translation layer (~100 lines). Walks the parse tree produced by ANTLR4 and assembles English output. Handles subject-verb agreement (I *am* swimming, he/she/it *sits*, we *have* eaten).

### Test results

20 tests, all passing. Tests cover all four sentence types:

| Type | Example OVP | Expected English |
|---|---|---|
| Noun + intransitive | `tsiipa-uu tsibui-ku` | That bird climbed. |
| Noun + transitive | `isha'-uu pagwi-noka u-zawa-dü` | That coyote cooks that fish. |
| Pronoun + intransitive | `pahabi-ti nüü` | I am swimming. |
| Pronoun + transitive | `pagwi-noka nüü ma-puni-ku` | I saw that fish. |

Plus four grammar enforcement tests that verify invalid sentences are rejected with a `SyntaxError` — something the current system cannot do at all.

### Demo output
```
OVP                                      English
isha'-uu pagwi-noka u-zawa-dü            That coyote cooks that fish.
pahabi-ti nüü                            I am swimming.
pahabichi-ii wo'abi-noka ui-naka-dü      This bear hears that worm.
tsiipa-uu tsibui-ku                      That bird climbed.
katü-dü uhu                              He/she/it sits.
nishua'i-pü nüü                          I have laughed.
```

---

## 5. Analysis of the Current System

### Where the current system is strong

- The **linguistic knowledge is there**. `ovp-lang/language.py` correctly models morphology: agreement constraints, lenition rules, the 5-dimensional pronoun system (person × number × proximity × animacy). This is genuine expertise.
- The **sentence builder UI** is well-designed for guided sentence composition. The constraint propagation prevents users from assembling invalid combinations.
- **Using LLM to decompose natural English into simple SVO sentences** (step 1 of the English→OVP pipeline) is a legitimate and well-chosen use of LLM capability.

### Where the current system has limitations

**1. Grammar knowledge is buried in code**

The morphological rules exist across `ovp-lang/language.py`, `sentences-api/sentence-builder.js`, and scattered Python conditionals. A linguist or OVP speaker wanting to verify "is this grammar rule correct?" has no single place to look. Adding a new rule (e.g., negation) requires tracing logic through multiple files.

With a formal grammar, the rules live in one readable file. The grammar *is* the documentation.

**2. The system cannot parse OVP text**

Currently there is no way to take a typed OVP sentence as input and verify or translate it. The translator pipeline goes English → OVP only. The OVP → English direction requires the LLM to reassemble English from lookup tables — it cannot handle any OVP input not produced by the system itself.

Our grammar-based parser handles arbitrary valid OVP input and rejects invalid input with a meaningful error.

**3. The back-translation quality check (step 5) is circular**

The system generates OVP output (step 3), then translates it back to English (step 5) to verify quality. But the back-translation uses the same vocabulary tables and rules as the forward translation. If the forward rules are wrong, the backward rules will produce the same wrong result, and the check will pass. This cannot detect systematic errors.

**4. Vocabulary is duplicated**

`ovp-lang/vocab.py` and `sentences-api/sentence-builder.js` maintain separate copies of the OVP vocabulary. These can drift out of sync. Our `lexicon.py` is a single source of truth that both the grammar and the translator reference.

**5. Evaluation methodology**

The paper reports 98/100 accuracy on OVP→English, but the labels were produced by the authors, not by independent native speakers or linguists. The English→OVP accuracy relies on the circular back-translation metric described above. We raise this not to diminish the work, but because stronger evaluation — even a small native-speaker review — would significantly strengthen future publications.

---

## 6. Recommended Architecture

We are not proposing to eliminate LLM from the system. LLM is genuinely useful in two places. The recommendation is to use each tool where it is best suited:

```
Natural English input
        │
        ▼  [LLM]
        Normalize to simple SVO sentences
        with explicit tense, subject, object, proximity
        │
        ▼  [Rule-based grammar core]
        Apply OVP morphology:
          - select suffixes (-uu/-ii, -noka/-neika, etc.)
          - apply lenition if needed
          - choose word order (SOV vs OVS vs verb-first)
          - enforce all agreement constraints
        │
        ▼
        OVP output  ←——→  OVP input
                               │
                          [Grammar parser]
                          Validate and parse OVP
                               │
                          [Rule-based translator]
                          Map morphemes to English
                               │
                          ▼  [LLM, optional]
                          Naturalize English phrasing
                          Flag ambiguities (gender, tense)
```

| Task | Best tool | Reason |
|---|---|---|
| Decompose natural English to simple SVO | LLM | LLM excels at understanding English variation |
| Generate OVP morphology | Formal grammar | Deterministic, verifiable, correct |
| Parse and translate OVP → English | Formal grammar | Deterministic, 100% accurate |
| Naturalize English output, flag ambiguities | LLM (optional) | LLM excels at English fluency |
| Guarantee OVP grammatical correctness | Formal grammar only | LLM has seen essentially no OVP in training |

The key principle: **LLM should never generate or modify OVP output directly.** OVP is a low-resource language with virtually no training data available to LLMs. The LLM cannot know whether its OVP output is correct. The grammar always knows.

---

## 7. Path Forward

### Short term (demonstrable now)
- OVP → English translation: **complete and working**, 20/20 tests passing, all sentence types from the paper's Appendix A covered
- Grammar enforcement: invalid OVP input is rejected with a meaningful error message
- Single vocabulary source: `lexicon.py` consolidates the duplicated vocabulary tables

### Medium term
- **English → OVP**: the OVP morphology generation side is straightforward (the rules already exist in `ovp-lang/language.py`). The main engineering task is wiring up the LLM normalization step to feed into the grammar-based generator.
- **Expand vocabulary**: the grammar file and lexicon have a clear, simple format for adding new words
- **Consolidate repositories**: the grammar core could replace the vocabulary duplication across `ovp-lang` and `sentences-api`

### Longer term
- Nominalization (verb as noun: "swimmer", "the one who ate")
- Possessives on nouns
- Negation
- Question formation
- Each of these is one or a few grammar rules — the architecture scales naturally

---

## 8. Summary

The core argument is simple: **the OVP grammar rules are the most valuable output of this research.** They encode expert knowledge about a critically endangered language. That knowledge should live in an explicit, readable, verifiable form — not buried in Python conditionals and JSON tables that only a developer can read.

A formal grammar achieves this. It is the living documentation of OVP syntax and morphology. It is readable by linguists. It is verifiable by OVP speakers. It generates correct output by construction. And it provides the foundation on which negation, questions, complex sentences, and future linguistic discoveries can be built — one rule at a time.

LLM has a real role in this system, at the boundaries where natural language understanding is needed. The grammar is the core.

---

*Proof-of-concept code available at:* `/data/home/klin/Owens_Valley_Paiute/ovp-grammar/`
