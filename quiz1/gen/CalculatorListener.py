# Generated from Calculator.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#expr.
    def enterExpr(self, ctx:CalculatorParser.ExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#expr.
    def exitExpr(self, ctx:CalculatorParser.ExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#term.
    def enterTerm(self, ctx:CalculatorParser.TermContext):
        pass

    # Exit a parse tree produced by CalculatorParser#term.
    def exitTerm(self, ctx:CalculatorParser.TermContext):
        pass


    # Enter a parse tree produced by CalculatorParser#factor.
    def enterFactor(self, ctx:CalculatorParser.FactorContext):
        pass

    # Exit a parse tree produced by CalculatorParser#factor.
    def exitFactor(self, ctx:CalculatorParser.FactorContext):
        pass


    # Enter a parse tree produced by CalculatorParser#power.
    def enterPower(self, ctx:CalculatorParser.PowerContext):
        pass

    # Exit a parse tree produced by CalculatorParser#power.
    def exitPower(self, ctx:CalculatorParser.PowerContext):
        pass


    # Enter a parse tree produced by CalculatorParser#atom.
    def enterAtom(self, ctx:CalculatorParser.AtomContext):
        pass

    # Exit a parse tree produced by CalculatorParser#atom.
    def exitAtom(self, ctx:CalculatorParser.AtomContext):
        pass



del CalculatorParser