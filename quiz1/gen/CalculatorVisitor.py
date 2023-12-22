# Generated from Calculator.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#expr.
    def visitExpr(self, ctx:CalculatorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#term.
    def visitTerm(self, ctx:CalculatorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#factor.
    def visitFactor(self, ctx:CalculatorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#power.
    def visitPower(self, ctx:CalculatorParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#atom.
    def visitAtom(self, ctx:CalculatorParser.AtomContext):
        return self.visitChildren(ctx)



del CalculatorParser