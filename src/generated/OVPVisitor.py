# Generated from grammar/OVP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OVPParser import OVPParser
else:
    from OVPParser import OVPParser

# This class defines a complete generic visitor for a parse tree produced by OVPParser.

class OVPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OVPParser#sentence.
    def visitSentence(self, ctx:OVPParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#NounSVO.
    def visitNounSVO(self, ctx:OVPParser.NounSVOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#NounSV.
    def visitNounSV(self, ctx:OVPParser.NounSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#PronounOVS.
    def visitPronounOVS(self, ctx:OVPParser.PronounOVSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#PronounVS.
    def visitPronounVS(self, ctx:OVPParser.PronounVSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#subjectNoun.
    def visitSubjectNoun(self, ctx:OVPParser.SubjectNounContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#objectNoun.
    def visitObjectNoun(self, ctx:OVPParser.ObjectNounContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#transitiveVerb.
    def visitTransitiveVerb(self, ctx:OVPParser.TransitiveVerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#intransitiveVerb.
    def visitIntransitiveVerb(self, ctx:OVPParser.IntransitiveVerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#subjectSuffix.
    def visitSubjectSuffix(self, ctx:OVPParser.SubjectSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#objectSuffix.
    def visitObjectSuffix(self, ctx:OVPParser.ObjectSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OVPParser#tense.
    def visitTense(self, ctx:OVPParser.TenseContext):
        return self.visitChildren(ctx)



del OVPParser