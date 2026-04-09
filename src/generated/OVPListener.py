# Generated from grammar/OVP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OVPParser import OVPParser
else:
    from OVPParser import OVPParser

# This class defines a complete listener for a parse tree produced by OVPParser.
class OVPListener(ParseTreeListener):

    # Enter a parse tree produced by OVPParser#sentence.
    def enterSentence(self, ctx:OVPParser.SentenceContext):
        pass

    # Exit a parse tree produced by OVPParser#sentence.
    def exitSentence(self, ctx:OVPParser.SentenceContext):
        pass


    # Enter a parse tree produced by OVPParser#NounSVO.
    def enterNounSVO(self, ctx:OVPParser.NounSVOContext):
        pass

    # Exit a parse tree produced by OVPParser#NounSVO.
    def exitNounSVO(self, ctx:OVPParser.NounSVOContext):
        pass


    # Enter a parse tree produced by OVPParser#NounSV.
    def enterNounSV(self, ctx:OVPParser.NounSVContext):
        pass

    # Exit a parse tree produced by OVPParser#NounSV.
    def exitNounSV(self, ctx:OVPParser.NounSVContext):
        pass


    # Enter a parse tree produced by OVPParser#PronounOVS.
    def enterPronounOVS(self, ctx:OVPParser.PronounOVSContext):
        pass

    # Exit a parse tree produced by OVPParser#PronounOVS.
    def exitPronounOVS(self, ctx:OVPParser.PronounOVSContext):
        pass


    # Enter a parse tree produced by OVPParser#PronounVS.
    def enterPronounVS(self, ctx:OVPParser.PronounVSContext):
        pass

    # Exit a parse tree produced by OVPParser#PronounVS.
    def exitPronounVS(self, ctx:OVPParser.PronounVSContext):
        pass


    # Enter a parse tree produced by OVPParser#subjectNoun.
    def enterSubjectNoun(self, ctx:OVPParser.SubjectNounContext):
        pass

    # Exit a parse tree produced by OVPParser#subjectNoun.
    def exitSubjectNoun(self, ctx:OVPParser.SubjectNounContext):
        pass


    # Enter a parse tree produced by OVPParser#objectNoun.
    def enterObjectNoun(self, ctx:OVPParser.ObjectNounContext):
        pass

    # Exit a parse tree produced by OVPParser#objectNoun.
    def exitObjectNoun(self, ctx:OVPParser.ObjectNounContext):
        pass


    # Enter a parse tree produced by OVPParser#transitiveVerb.
    def enterTransitiveVerb(self, ctx:OVPParser.TransitiveVerbContext):
        pass

    # Exit a parse tree produced by OVPParser#transitiveVerb.
    def exitTransitiveVerb(self, ctx:OVPParser.TransitiveVerbContext):
        pass


    # Enter a parse tree produced by OVPParser#intransitiveVerb.
    def enterIntransitiveVerb(self, ctx:OVPParser.IntransitiveVerbContext):
        pass

    # Exit a parse tree produced by OVPParser#intransitiveVerb.
    def exitIntransitiveVerb(self, ctx:OVPParser.IntransitiveVerbContext):
        pass


    # Enter a parse tree produced by OVPParser#subjectSuffix.
    def enterSubjectSuffix(self, ctx:OVPParser.SubjectSuffixContext):
        pass

    # Exit a parse tree produced by OVPParser#subjectSuffix.
    def exitSubjectSuffix(self, ctx:OVPParser.SubjectSuffixContext):
        pass


    # Enter a parse tree produced by OVPParser#objectSuffix.
    def enterObjectSuffix(self, ctx:OVPParser.ObjectSuffixContext):
        pass

    # Exit a parse tree produced by OVPParser#objectSuffix.
    def exitObjectSuffix(self, ctx:OVPParser.ObjectSuffixContext):
        pass


    # Enter a parse tree produced by OVPParser#tense.
    def enterTense(self, ctx:OVPParser.TenseContext):
        pass

    # Exit a parse tree produced by OVPParser#tense.
    def exitTense(self, ctx:OVPParser.TenseContext):
        pass



del OVPParser