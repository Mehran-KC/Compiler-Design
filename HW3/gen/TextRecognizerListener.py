# Generated from TextRecognizer.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TextRecognizerParser import TextRecognizerParser
else:
    from TextRecognizerParser import TextRecognizerParser

# This class defines a complete listener for a parse tree produced by TextRecognizerParser.
class TextRecognizerListener(ParseTreeListener):

    # Enter a parse tree produced by TextRecognizerParser#emails.
    def enterEmails(self, ctx:TextRecognizerParser.EmailsContext):
        pass

    # Exit a parse tree produced by TextRecognizerParser#emails.
    def exitEmails(self, ctx:TextRecognizerParser.EmailsContext):
        pass


    # Enter a parse tree produced by TextRecognizerParser#email.
    def enterEmail(self, ctx:TextRecognizerParser.EmailContext):
        pass

    # Exit a parse tree produced by TextRecognizerParser#email.
    def exitEmail(self, ctx:TextRecognizerParser.EmailContext):
        pass


    # Enter a parse tree produced by TextRecognizerParser#melli_number.
    def enterMelli_number(self, ctx:TextRecognizerParser.Melli_numberContext):
        pass

    # Exit a parse tree produced by TextRecognizerParser#melli_number.
    def exitMelli_number(self, ctx:TextRecognizerParser.Melli_numberContext):
        pass


    # Enter a parse tree produced by TextRecognizerParser#url.
    def enterUrl(self, ctx:TextRecognizerParser.UrlContext):
        pass

    # Exit a parse tree produced by TextRecognizerParser#url.
    def exitUrl(self, ctx:TextRecognizerParser.UrlContext):
        pass



del TextRecognizerParser