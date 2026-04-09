"""
OVP -> English translator using the ANTLR4-generated parser.
The grammar enforces structural correctness;
this Visitor handles the semantic translation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from OVPLexer import OVPLexer
from OVPParser import OVPParser
from OVPVisitor import OVPVisitor

from src.lexicon import NOUN_EN, VERB_EN, SUBJECT_PRONOUN_EN, PROXIMITY, conjugate, PRONOUN_PERSON


class StrictErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise SyntaxError(f"OVP parse error at {line}:{col} — {msg}")


class OVPToEnglish(OVPVisitor):
    """
    Visitor that walks the ANTLR4 parse tree and produces an English translation.
    Each visitXxx method corresponds to a labeled grammar rule or parser rule.
    """

    def __init__(self):
        self._person = "3sg"   # default; overwritten at each sentence-level rule

    # ------------------------------------------------------------------
    # Sentence-level rules (labeled alternatives)
    # ------------------------------------------------------------------

    def visitNounSVO(self, ctx):
        self._person = "3sg"   # noun subjects are always 3rd-person-singular
        subj = self.visit(ctx.subjectNoun())
        obj  = self.visit(ctx.objectNoun())
        verb = self.visit(ctx.transitiveVerb())
        return f"{subj} {verb} {obj}."

    def visitNounSV(self, ctx):
        self._person = "3sg"
        subj = self.visit(ctx.subjectNoun())
        verb = self.visit(ctx.intransitiveVerb())
        return f"{subj} {verb}."

    def visitPronounOVS(self, ctx):
        pron = ctx.SUBJECT_PRONOUN().getText()
        self._person = PRONOUN_PERSON.get(pron, "3sg")
        obj  = self.visit(ctx.objectNoun())
        verb = self.visit(ctx.transitiveVerb())
        subj = SUBJECT_PRONOUN_EN.get(pron, pron)
        return f"{subj.capitalize()} {verb} {obj}."

    def visitPronounVS(self, ctx):
        pron = ctx.SUBJECT_PRONOUN().getText()
        self._person = PRONOUN_PERSON.get(pron, "3sg")
        verb = self.visit(ctx.intransitiveVerb())
        subj = SUBJECT_PRONOUN_EN.get(pron, pron)
        return f"{subj.capitalize()} {verb}."

    # ------------------------------------------------------------------
    # Phrase-level rules
    # ------------------------------------------------------------------

    def visitSubjectNoun(self, ctx):
        noun   = ctx.NOUN().getText()
        suffix = ctx.subjectSuffix().getText()
        det, _ = PROXIMITY.get(suffix, ("The", "the"))
        return f"{det} {NOUN_EN.get(noun, f'[{noun}]')}"

    def visitObjectNoun(self, ctx):
        noun   = ctx.NOUN().getText()
        suffix = ctx.objectSuffix().getText()
        _, det = PROXIMITY.get(suffix, ("the", "the"))
        return f"{det} {NOUN_EN.get(noun, f'[{noun}]')}"

    def visitTransitiveVerb(self, ctx):
        stem  = ctx.VERB().getText()
        tense = ctx.tense().getText()
        return conjugate(VERB_EN.get(stem, f"[{stem}]"), tense, self._person)

    def visitIntransitiveVerb(self, ctx):
        stem  = ctx.VERB().getText()
        tense = ctx.tense().getText()
        return conjugate(VERB_EN.get(stem, f"[{stem}]"), tense, self._person)


def _make_parser(ovp_sentence: str):
    """Create a parser for an OVP sentence. Shared by translate() and parse_tree()."""
    stream = InputStream(ovp_sentence.strip())
    lexer  = OVPLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = OVPParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(StrictErrorListener())
    return parser


def translate(ovp_sentence: str) -> str:
    """
    Parse an OVP sentence and return its English translation.
    Raises SyntaxError if the sentence is grammatically invalid.
    """
    parser = _make_parser(ovp_sentence)
    tree = parser.sentence()
    return OVPToEnglish().visit(tree)


def parse_tree(ovp_sentence: str) -> str:
    """
    Parse an OVP sentence and return a pretty-printed syntax tree.
    Raises SyntaxError if the sentence is grammatically invalid.
    """
    parser = _make_parser(ovp_sentence)
    tree = parser.sentence()

    lines = []
    def walk(node, indent=0):
        prefix = "  " * indent
        if hasattr(node, 'getRuleIndex'):
            name = OVPParser.ruleNames[node.getRuleIndex()]
            # Use labeled alt name if available (e.g. NounSVO instead of nounSubjectSentence)
            for attr in dir(node):
                if attr.endswith('Context') and attr[0].isupper():
                    name = attr.replace('Context', '')
                    break
            lines.append(f"{prefix}{name}")
            for child in node.getChildren():
                walk(child, indent + 1)
        else:
            lines.append(f"{prefix}{node.getText()}")
    walk(tree)
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tree":
        ovp = " ".join(sys.argv[2:])
        print(parse_tree(ovp))
    elif len(sys.argv) > 1:
        ovp = " ".join(sys.argv[1:])
        print(translate(ovp))
    else:
        examples = [
            "isha'-uu pagwi-noka u-zawa-dü",
            "pahabi-ti nüü",
            "pahabichi-ii wo'abi-noka ui-naka-dü",
            "tsiipa-uu tsibui-ku",
            "katü-dü uhu",
            "nishua'i-pü nüü",
        ]
        print(f"{'OVP':<45} {'English'}")
        print("-" * 70)
        for sentence in examples:
            print(f"{sentence:<45} {translate(sentence)}")
