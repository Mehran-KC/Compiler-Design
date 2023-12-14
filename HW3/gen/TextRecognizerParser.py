# Generated from TextRecognizer.g4 by ANTLR 4.10.1
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
        4,1,8,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,1,0,1,0,3,0,20,8,0,5,0,22,8,0,10,0,12,0,25,9,0,1,
        1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,37,0,12,1,0,
        0,0,2,26,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,8,13,3,2,1,0,9,13,3,4,
        2,0,10,13,3,6,3,0,11,13,5,0,0,1,12,8,1,0,0,0,12,9,1,0,0,0,12,10,
        1,0,0,0,12,11,1,0,0,0,13,23,1,0,0,0,14,19,5,2,0,0,15,20,3,2,1,0,
        16,20,3,4,2,0,17,20,3,6,3,0,18,20,5,0,0,1,19,15,1,0,0,0,19,16,1,
        0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,22,1,0,0,0,21,14,1,0,0,0,22,
        25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,23,1,0,0,
        0,26,27,5,3,0,0,27,28,6,1,-1,0,28,3,1,0,0,0,29,30,5,4,0,0,30,5,1,
        0,0,0,31,32,5,5,0,0,32,33,6,3,-1,0,33,7,1,0,0,0,3,12,19,23
    ]

class TextRecognizerParser ( Parser ):

    grammarFileName = "TextRecognizer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "COLON", "COMMA", "EMAIL", "MELLI_NUMBER", 
                      "URL", "PROTOCOL", "DIGIT", "WS" ]

    RULE_emails = 0
    RULE_email = 1
    RULE_melli_number = 2
    RULE_url = 3

    ruleNames =  [ "emails", "email", "melli_number", "url" ]

    EOF = Token.EOF
    COLON=1
    COMMA=2
    EMAIL=3
    MELLI_NUMBER=4
    URL=5
    PROTOCOL=6
    DIGIT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EmailsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def email(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextRecognizerParser.EmailContext)
            else:
                return self.getTypedRuleContext(TextRecognizerParser.EmailContext,i)


        def melli_number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextRecognizerParser.Melli_numberContext)
            else:
                return self.getTypedRuleContext(TextRecognizerParser.Melli_numberContext,i)


        def url(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextRecognizerParser.UrlContext)
            else:
                return self.getTypedRuleContext(TextRecognizerParser.UrlContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(TextRecognizerParser.EOF)
            else:
                return self.getToken(TextRecognizerParser.EOF, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TextRecognizerParser.COMMA)
            else:
                return self.getToken(TextRecognizerParser.COMMA, i)

        def getRuleIndex(self):
            return TextRecognizerParser.RULE_emails

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmails" ):
                listener.enterEmails(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmails" ):
                listener.exitEmails(self)




    def emails(self):

        localctx = TextRecognizerParser.EmailsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_emails)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TextRecognizerParser.EMAIL]:
                self.state = 8
                self.email()
                pass
            elif token in [TextRecognizerParser.MELLI_NUMBER]:
                self.state = 9
                self.melli_number()
                pass
            elif token in [TextRecognizerParser.URL]:
                self.state = 10
                self.url()
                pass
            elif token in [TextRecognizerParser.EOF]:
                self.state = 11
                self.match(TextRecognizerParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TextRecognizerParser.COMMA:
                self.state = 14
                self.match(TextRecognizerParser.COMMA)
                self.state = 19
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TextRecognizerParser.EMAIL]:
                    self.state = 15
                    self.email()
                    pass
                elif token in [TextRecognizerParser.MELLI_NUMBER]:
                    self.state = 16
                    self.melli_number()
                    pass
                elif token in [TextRecognizerParser.URL]:
                    self.state = 17
                    self.url()
                    pass
                elif token in [TextRecognizerParser.EOF]:
                    self.state = 18
                    self.match(TextRecognizerParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMAIL(self):
            return self.getToken(TextRecognizerParser.EMAIL, 0)

        def getRuleIndex(self):
            return TextRecognizerParser.RULE_email

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmail" ):
                listener.enterEmail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmail" ):
                listener.exitEmail(self)




    def email(self):

        localctx = TextRecognizerParser.EmailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_email)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(TextRecognizerParser.EMAIL)
            print("**email found**")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Melli_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MELLI_NUMBER(self):
            return self.getToken(TextRecognizerParser.MELLI_NUMBER, 0)

        def getRuleIndex(self):
            return TextRecognizerParser.RULE_melli_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMelli_number" ):
                listener.enterMelli_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMelli_number" ):
                listener.exitMelli_number(self)




    def melli_number(self):

        localctx = TextRecognizerParser.Melli_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_melli_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(TextRecognizerParser.MELLI_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URL(self):
            return self.getToken(TextRecognizerParser.URL, 0)

        def getRuleIndex(self):
            return TextRecognizerParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)




    def url(self):

        localctx = TextRecognizerParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(TextRecognizerParser.URL)
            print("**URL found**")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





