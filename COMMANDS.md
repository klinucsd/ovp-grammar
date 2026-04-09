# OVP Grammar — Command Reference

All commands are run from the `ovp-grammar/` directory.
All `make` targets run inside Docker — Java and ANTLR4 are not required on the host.

---

## Quick Reference

| Task | Command |
|---|---|
| First-time setup | `make build` |
| Translate OVP → English | `make ovp2en SENTENCE="..."` |
| Translate English → OVP | `make en2ovp SENTENCE="..."` |
| Show OVP parse tree | `make parse SENTENCE="..."` |
| Run all tests | `make test` |
| Rebuild parser after grammar change | `make generate` |
| Interactive shell in container | `make shell` |
| Remove generated parser files | `make clean` |

---

## Make Commands

### `make build`
Build the Docker image. Run this once before anything else, and again whenever `Dockerfile` or `requirements.txt` changes.

```bash
make build
```

The image includes: Python 3.11, Java JRE (for ANTLR4), ANTLR4 4.13.1 tool, and the `antlr4-python3-runtime` Python package.

---

### `make ovp2en`
Translate an OVP sentence to English.

```bash
make ovp2en SENTENCE="isha'-uu pagwi-noka u-zawa-dü"
# That coyote cooks that fish.

make ovp2en SENTENCE="pahabi-ti nüü"
# I am swimming.

make ovp2en SENTENCE="tsiipa-uu tsibui-ku"
# That bird climbed.

make ovp2en SENTENCE="pagwi-noka nüü ma-puni-ku"
# I saw that fish.
```

Without a `SENTENCE`, runs a built-in demo of 6 example sentences:

```bash
make ovp2en
```

Invalid OVP input raises a `SyntaxError` with a description of what went wrong.

---

### `make en2ovp`
Translate a constrained English sentence to OVP.
Input must use vocabulary from the lexicon and follow simple sentence patterns:
- `(This|That) NOUN VERB-PHRASE [(this|that) NOUN].`
- `PRONOUN VERB-PHRASE [(this|that) NOUN].`

```bash
make en2ovp SENTENCE="That coyote cooks that fish."
# isha'-uu pagwi-noka u-zawa-dü

make en2ovp SENTENCE="I am swimming."
# pahabi-ti nüü

make en2ovp SENTENCE="That bird will see this horse."
# tsiipa-uu pugu-neika a-buni-wei

make en2ovp SENTENCE="We ate this dog."
# isha'pugu-neika nüügwa a-düka-ku
```

All six tenses are supported:

| English pattern | OVP tense suffix | Example |
|---|---|---|
| `verb` / `verbs` | `-dü` (present) | "cooks" |
| `will verb` | `-wei` (future) | "will cook" |
| `am/is/are verbing` | `-ti` (ongoing) | "is cooking" |
| `was/were verbing` | `-ti` | "was cooking" |
| `has/have verbed` | `-pü` (perfect) | "has cooked" |
| `verbed` / irregular past | `-ku` (past) | "cooked", "saw" |
| `am/is/are going to verb` | `-gaa-wei` (going-to) | "is going to cook" |

Without a `SENTENCE`, runs a built-in demo of 12 example sentences:

```bash
make en2ovp
```

---

### `make parse`
Show the ANTLR4 parse tree for an OVP sentence. Useful for understanding how the grammar analyses a sentence.

```bash
make parse SENTENCE="isha'-uu pagwi-noka u-zawa-dü"
```

Output:
```
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

Invalid OVP input raises a `SyntaxError`.

---

### `make test`
Run the full test suite (43 tests) inside the container.

```bash
make test
```

Tests cover:
- OVP → English: all 4 sentence types (NounSV, NounSVO, PronounVS, PronounOVS), all tenses
- English → OVP: all 4 sentence types, round-trip tests, error handling
- Grammar enforcement: invalid sentences rejected with `SyntaxError`

---

### `make generate`
Recompile `grammar/OVP.g4` using ANTLR4 and write the generated Python parser to `src/generated/`.
**Run this whenever you edit `grammar/OVP.g4`** (e.g., to add new words or grammar rules).

```bash
make generate
```

Generated files (do not edit manually):
```
src/generated/
├── OVPLexer.py       # Tokenizer
├── OVPParser.py      # Parser
├── OVPVisitor.py     # Base visitor (subclassed by translator.py)
├── OVPListener.py    # Base listener (unused)
├── OVP.tokens
├── OVPLexer.tokens
├── OVP.interp
├── OVPLexer.interp
└── __init__.py
```

This target uses Java (inside the container) to run the ANTLR4 tool. Java is not needed on the host machine.

---

### `make shell`
Open an interactive bash shell inside the container. Useful for debugging or running ad-hoc Python commands.

```bash
make shell
```

Inside the shell:

```python
python
>>> from src.translator import translate
>>> translate("isha'-uu pagwi-noka u-zawa-dü")
'That coyote cooks that fish.'

>>> from src.en_to_ovp import translate_to_ovp
>>> translate_to_ovp("That coyote cooks that fish.")
'isha\'-uu pagwi-noka u-zawa-dü'

>>> from src.translator import parse_tree
>>> print(parse_tree("tsiipa-uu tsibui-ku"))
sentence
  nounSubjectSentence
    subjectNoun
      ...
```

---

### `make clean`
Remove the generated parser files from `src/generated/`. After running this, you must run `make generate` (or `make build`) before tests will work again.

```bash
make clean
```

---

## Docker Commands

The `make` targets are thin wrappers around `docker compose`. You can also run Docker commands directly if you need more control.

### Build the image

```bash
docker compose build
```

### Run a one-off Python command

```bash
docker compose run --rm ovp-grammar python -c "from src.translator import translate; print(translate('pahabi-ti nüü'))"
```

### Run pytest directly

```bash
docker compose run --rm ovp-grammar python -m pytest tests/ -v

# Run only one test file
docker compose run --rm ovp-grammar python -m pytest tests/test_translator.py -v

# Run only one test
docker compose run --rm ovp-grammar python -m pytest tests/test_translator.py::test_noun_svo_cook -v
```

### Run the OVP → English demo

```bash
docker compose run --rm ovp-grammar python -m src.translator
```

### Run the English → OVP demo

```bash
docker compose run --rm ovp-grammar python -m src.en_to_ovp
```

### Regenerate the parser manually (with explicit volume mount)

```bash
docker compose run --rm \
  -v $(PWD)/src/generated:/app/src/generated \
  ovp-grammar \
  bash -c "antlr4 -Dlanguage=Python3 -visitor -o /tmp/gen grammar/OVP.g4 \
           && cp /tmp/gen/grammar/*.py src/generated/ \
           && cp /tmp/gen/grammar/*.tokens src/generated/ \
           && cp /tmp/gen/grammar/*.interp src/generated/"
touch src/generated/__init__.py
```

### Interactive shell

```bash
docker compose run --rm ovp-grammar bash
```

### Remove stopped containers

```bash
docker compose down
```

---

## Workflow: Adding New Vocabulary

1. Add the new noun or verb to **`src/lexicon.py`** (both `NOUN_EN` / `VERB_EN` dicts and the `_IRREGULAR` table if needed)
2. Add the new token to **`grammar/OVP.g4`** (in the `NOUN` or `VERB` lexer rule)
3. Run `make generate` to recompile the parser
4. Run `make test` to verify nothing broke
5. Add a test case to `tests/test_translator.py` and/or `tests/test_en_to_ovp.py`

## Workflow: Modifying Grammar Rules

1. Edit **`grammar/OVP.g4`** — parser rules (lowercase) or lexer rules (UPPERCASE)
2. If you add labeled alternatives (`# LabelName`), add the corresponding `visitLabelName` method to `src/translator.py`
3. Run `make generate`
4. Run `make test`

---

## File Overview

```
ovp-grammar/
├── grammar/
│   └── OVP.g4              # ANTLR4 grammar — edit this to change language rules
├── src/
│   ├── lexicon.py          # Vocabulary + English verb conjugation
│   ├── translator.py       # OVP → English (ANTLR4 Visitor)
│   ├── en_to_ovp.py        # English → OVP (pure rule-based, no LLM)
│   └── generated/          # Auto-generated by ANTLR4 (do not edit)
├── tests/
│   ├── test_translator.py  # 20 tests: OVP → English
│   └── test_en_to_ovp.py   # 23 tests: English → OVP + round-trips
├── CLAUDE.md               # Project guide for Claude Code sessions
├── COMMANDS.md             # This file
├── report.md               # Architecture analysis for Jared Coleman's team
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── Makefile
```
