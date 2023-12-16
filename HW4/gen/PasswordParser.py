# Generated from Password.g4 by ANTLR 4.10.1
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
        4,1,6,8,2,0,7,0,1,0,4,0,4,8,0,11,0,12,0,5,1,0,0,0,1,0,0,0,7,0,3,
        1,0,0,0,2,4,5,1,0,0,3,2,1,0,0,0,4,5,1,0,0,0,5,3,1,0,0,0,5,6,1,0,
        0,0,6,1,1,0,0,0,1,5
    ]

class PasswordParser ( Parser ):

    grammarFileName = "Password.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "CHAR", "UPPER", "LOWER", "DIGIT", "SYMBOL", 
                      "WS" ]

    RULE_password = 0

    ruleNames =  [ "password" ]

    EOF = Token.EOF
    CHAR=1
    UPPER=2
    LOWER=3
    DIGIT=4
    SYMBOL=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PasswordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PasswordParser.CHAR)
            else:
                return self.getToken(PasswordParser.CHAR, i)

        def getRuleIndex(self):
            return PasswordParser.RULE_password

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassword" ):
                listener.enterPassword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassword" ):
                listener.exitPassword(self)




    def password(self):

        localctx = PasswordParser.PasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_password)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                self.match(PasswordParser.CHAR)
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PasswordParser.CHAR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





