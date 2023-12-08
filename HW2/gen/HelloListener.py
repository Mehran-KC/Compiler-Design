# Generated from Hello.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#greet.
    def enterGreet(self, ctx:HelloParser.GreetContext):
        pass

    # Exit a parse tree produced by HelloParser#greet.
    def exitGreet(self, ctx:HelloParser.GreetContext):
        pass



del HelloParser