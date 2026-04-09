# Generated from grammar/OVP.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,3,0,23,8,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,
        3,1,0,12,13,1,0,8,11,1,0,2,7,59,0,22,1,0,0,0,2,31,1,0,0,0,4,40,1,
        0,0,0,6,42,1,0,0,0,8,46,1,0,0,0,10,50,1,0,0,0,12,56,1,0,0,0,14,60,
        1,0,0,0,16,62,1,0,0,0,18,64,1,0,0,0,20,23,3,2,1,0,21,23,3,4,2,0,
        22,20,1,0,0,0,22,21,1,0,0,0,23,1,1,0,0,0,24,25,3,6,3,0,25,26,3,8,
        4,0,26,27,3,10,5,0,27,32,1,0,0,0,28,29,3,6,3,0,29,30,3,12,6,0,30,
        32,1,0,0,0,31,24,1,0,0,0,31,28,1,0,0,0,32,3,1,0,0,0,33,34,3,8,4,
        0,34,35,5,14,0,0,35,36,3,10,5,0,36,41,1,0,0,0,37,38,3,12,6,0,38,
        39,5,14,0,0,39,41,1,0,0,0,40,33,1,0,0,0,40,37,1,0,0,0,41,5,1,0,0,
        0,42,43,5,17,0,0,43,44,5,1,0,0,44,45,3,14,7,0,45,7,1,0,0,0,46,47,
        5,17,0,0,47,48,5,1,0,0,48,49,3,16,8,0,49,9,1,0,0,0,50,51,5,15,0,
        0,51,52,5,1,0,0,52,53,5,16,0,0,53,54,5,1,0,0,54,55,3,18,9,0,55,11,
        1,0,0,0,56,57,5,16,0,0,57,58,5,1,0,0,58,59,3,18,9,0,59,13,1,0,0,
        0,60,61,7,0,0,0,61,15,1,0,0,0,62,63,7,1,0,0,63,17,1,0,0,0,64,65,
        7,2,0,0,65,19,1,0,0,0,3,22,31,40
    ]

class OVPParser ( Parser ):

    grammarFileName = "OVP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'gaa-wei'", "'ku'", "'ti'", "'d\\u00FC'", 
                     "'wei'", "'p\\u00FC'", "'neika'", "'noka'", "'eika'", 
                     "'oka'", "'uu'", "'ii'" ]

    symbolicNames = [ "<INVALID>", "HYPHEN", "GAA_WEI", "KU", "TI", "DU", 
                      "WEI", "PU", "NEIKA", "NOKA", "EIKA", "OKA", "UU", 
                      "II", "SUBJECT_PRONOUN", "OBJ_PRONOUN", "VERB", "NOUN", 
                      "WS" ]

    RULE_sentence = 0
    RULE_nounSubjectSentence = 1
    RULE_pronounSubjectSentence = 2
    RULE_subjectNoun = 3
    RULE_objectNoun = 4
    RULE_transitiveVerb = 5
    RULE_intransitiveVerb = 6
    RULE_subjectSuffix = 7
    RULE_objectSuffix = 8
    RULE_tense = 9

    ruleNames =  [ "sentence", "nounSubjectSentence", "pronounSubjectSentence", 
                   "subjectNoun", "objectNoun", "transitiveVerb", "intransitiveVerb", 
                   "subjectSuffix", "objectSuffix", "tense" ]

    EOF = Token.EOF
    HYPHEN=1
    GAA_WEI=2
    KU=3
    TI=4
    DU=5
    WEI=6
    PU=7
    NEIKA=8
    NOKA=9
    EIKA=10
    OKA=11
    UU=12
    II=13
    SUBJECT_PRONOUN=14
    OBJ_PRONOUN=15
    VERB=16
    NOUN=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nounSubjectSentence(self):
            return self.getTypedRuleContext(OVPParser.NounSubjectSentenceContext,0)


        def pronounSubjectSentence(self):
            return self.getTypedRuleContext(OVPParser.PronounSubjectSentenceContext,0)


        def getRuleIndex(self):
            return OVPParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = OVPParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.nounSubjectSentence()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.pronounSubjectSentence()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NounSubjectSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OVPParser.RULE_nounSubjectSentence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NounSVContext(NounSubjectSentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OVPParser.NounSubjectSentenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def subjectNoun(self):
            return self.getTypedRuleContext(OVPParser.SubjectNounContext,0)

        def intransitiveVerb(self):
            return self.getTypedRuleContext(OVPParser.IntransitiveVerbContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNounSV" ):
                listener.enterNounSV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNounSV" ):
                listener.exitNounSV(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNounSV" ):
                return visitor.visitNounSV(self)
            else:
                return visitor.visitChildren(self)


    class NounSVOContext(NounSubjectSentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OVPParser.NounSubjectSentenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def subjectNoun(self):
            return self.getTypedRuleContext(OVPParser.SubjectNounContext,0)

        def objectNoun(self):
            return self.getTypedRuleContext(OVPParser.ObjectNounContext,0)

        def transitiveVerb(self):
            return self.getTypedRuleContext(OVPParser.TransitiveVerbContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNounSVO" ):
                listener.enterNounSVO(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNounSVO" ):
                listener.exitNounSVO(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNounSVO" ):
                return visitor.visitNounSVO(self)
            else:
                return visitor.visitChildren(self)



    def nounSubjectSentence(self):

        localctx = OVPParser.NounSubjectSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nounSubjectSentence)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = OVPParser.NounSVOContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.subjectNoun()
                self.state = 25
                self.objectNoun()
                self.state = 26
                self.transitiveVerb()
                pass

            elif la_ == 2:
                localctx = OVPParser.NounSVContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.subjectNoun()
                self.state = 29
                self.intransitiveVerb()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PronounSubjectSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OVPParser.RULE_pronounSubjectSentence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PronounVSContext(PronounSubjectSentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OVPParser.PronounSubjectSentenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def intransitiveVerb(self):
            return self.getTypedRuleContext(OVPParser.IntransitiveVerbContext,0)

        def SUBJECT_PRONOUN(self):
            return self.getToken(OVPParser.SUBJECT_PRONOUN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPronounVS" ):
                listener.enterPronounVS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPronounVS" ):
                listener.exitPronounVS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPronounVS" ):
                return visitor.visitPronounVS(self)
            else:
                return visitor.visitChildren(self)


    class PronounOVSContext(PronounSubjectSentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OVPParser.PronounSubjectSentenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def objectNoun(self):
            return self.getTypedRuleContext(OVPParser.ObjectNounContext,0)

        def SUBJECT_PRONOUN(self):
            return self.getToken(OVPParser.SUBJECT_PRONOUN, 0)
        def transitiveVerb(self):
            return self.getTypedRuleContext(OVPParser.TransitiveVerbContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPronounOVS" ):
                listener.enterPronounOVS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPronounOVS" ):
                listener.exitPronounOVS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPronounOVS" ):
                return visitor.visitPronounOVS(self)
            else:
                return visitor.visitChildren(self)



    def pronounSubjectSentence(self):

        localctx = OVPParser.PronounSubjectSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pronounSubjectSentence)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = OVPParser.PronounOVSContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.objectNoun()
                self.state = 34
                self.match(OVPParser.SUBJECT_PRONOUN)
                self.state = 35
                self.transitiveVerb()
                pass
            elif token in [16]:
                localctx = OVPParser.PronounVSContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.intransitiveVerb()
                self.state = 38
                self.match(OVPParser.SUBJECT_PRONOUN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectNounContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self):
            return self.getToken(OVPParser.NOUN, 0)

        def HYPHEN(self):
            return self.getToken(OVPParser.HYPHEN, 0)

        def subjectSuffix(self):
            return self.getTypedRuleContext(OVPParser.SubjectSuffixContext,0)


        def getRuleIndex(self):
            return OVPParser.RULE_subjectNoun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubjectNoun" ):
                listener.enterSubjectNoun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubjectNoun" ):
                listener.exitSubjectNoun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubjectNoun" ):
                return visitor.visitSubjectNoun(self)
            else:
                return visitor.visitChildren(self)




    def subjectNoun(self):

        localctx = OVPParser.SubjectNounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subjectNoun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(OVPParser.NOUN)
            self.state = 43
            self.match(OVPParser.HYPHEN)
            self.state = 44
            self.subjectSuffix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectNounContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self):
            return self.getToken(OVPParser.NOUN, 0)

        def HYPHEN(self):
            return self.getToken(OVPParser.HYPHEN, 0)

        def objectSuffix(self):
            return self.getTypedRuleContext(OVPParser.ObjectSuffixContext,0)


        def getRuleIndex(self):
            return OVPParser.RULE_objectNoun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectNoun" ):
                listener.enterObjectNoun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectNoun" ):
                listener.exitObjectNoun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectNoun" ):
                return visitor.visitObjectNoun(self)
            else:
                return visitor.visitChildren(self)




    def objectNoun(self):

        localctx = OVPParser.ObjectNounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_objectNoun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(OVPParser.NOUN)
            self.state = 47
            self.match(OVPParser.HYPHEN)
            self.state = 48
            self.objectSuffix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitiveVerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJ_PRONOUN(self):
            return self.getToken(OVPParser.OBJ_PRONOUN, 0)

        def HYPHEN(self, i:int=None):
            if i is None:
                return self.getTokens(OVPParser.HYPHEN)
            else:
                return self.getToken(OVPParser.HYPHEN, i)

        def VERB(self):
            return self.getToken(OVPParser.VERB, 0)

        def tense(self):
            return self.getTypedRuleContext(OVPParser.TenseContext,0)


        def getRuleIndex(self):
            return OVPParser.RULE_transitiveVerb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitiveVerb" ):
                listener.enterTransitiveVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitiveVerb" ):
                listener.exitTransitiveVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransitiveVerb" ):
                return visitor.visitTransitiveVerb(self)
            else:
                return visitor.visitChildren(self)




    def transitiveVerb(self):

        localctx = OVPParser.TransitiveVerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transitiveVerb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(OVPParser.OBJ_PRONOUN)
            self.state = 51
            self.match(OVPParser.HYPHEN)
            self.state = 52
            self.match(OVPParser.VERB)
            self.state = 53
            self.match(OVPParser.HYPHEN)
            self.state = 54
            self.tense()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntransitiveVerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERB(self):
            return self.getToken(OVPParser.VERB, 0)

        def HYPHEN(self):
            return self.getToken(OVPParser.HYPHEN, 0)

        def tense(self):
            return self.getTypedRuleContext(OVPParser.TenseContext,0)


        def getRuleIndex(self):
            return OVPParser.RULE_intransitiveVerb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntransitiveVerb" ):
                listener.enterIntransitiveVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntransitiveVerb" ):
                listener.exitIntransitiveVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntransitiveVerb" ):
                return visitor.visitIntransitiveVerb(self)
            else:
                return visitor.visitChildren(self)




    def intransitiveVerb(self):

        localctx = OVPParser.IntransitiveVerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_intransitiveVerb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(OVPParser.VERB)
            self.state = 57
            self.match(OVPParser.HYPHEN)
            self.state = 58
            self.tense()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def II(self):
            return self.getToken(OVPParser.II, 0)

        def UU(self):
            return self.getToken(OVPParser.UU, 0)

        def getRuleIndex(self):
            return OVPParser.RULE_subjectSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubjectSuffix" ):
                listener.enterSubjectSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubjectSuffix" ):
                listener.exitSubjectSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubjectSuffix" ):
                return visitor.visitSubjectSuffix(self)
            else:
                return visitor.visitChildren(self)




    def subjectSuffix(self):

        localctx = OVPParser.SubjectSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subjectSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEIKA(self):
            return self.getToken(OVPParser.NEIKA, 0)

        def NOKA(self):
            return self.getToken(OVPParser.NOKA, 0)

        def EIKA(self):
            return self.getToken(OVPParser.EIKA, 0)

        def OKA(self):
            return self.getToken(OVPParser.OKA, 0)

        def getRuleIndex(self):
            return OVPParser.RULE_objectSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectSuffix" ):
                listener.enterObjectSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectSuffix" ):
                listener.exitObjectSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectSuffix" ):
                return visitor.visitObjectSuffix(self)
            else:
                return visitor.visitChildren(self)




    def objectSuffix(self):

        localctx = OVPParser.ObjectSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_objectSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TenseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KU(self):
            return self.getToken(OVPParser.KU, 0)

        def TI(self):
            return self.getToken(OVPParser.TI, 0)

        def DU(self):
            return self.getToken(OVPParser.DU, 0)

        def WEI(self):
            return self.getToken(OVPParser.WEI, 0)

        def GAA_WEI(self):
            return self.getToken(OVPParser.GAA_WEI, 0)

        def PU(self):
            return self.getToken(OVPParser.PU, 0)

        def getRuleIndex(self):
            return OVPParser.RULE_tense

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTense" ):
                listener.enterTense(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTense" ):
                listener.exitTense(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTense" ):
                return visitor.visitTense(self)
            else:
                return visitor.visitChildren(self)




    def tense(self):

        localctx = OVPParser.TenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tense)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 252) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





