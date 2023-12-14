# Generated from TextRecognizer.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,25,8,3,11,3,12,3,26,
        1,4,4,4,30,8,4,11,4,12,4,31,1,5,1,5,1,5,1,5,1,5,1,5,1,6,4,6,41,8,
        6,11,6,12,6,42,1,7,4,7,46,8,7,11,7,12,7,47,1,7,1,7,0,0,8,1,1,3,2,
        5,0,7,0,9,0,11,3,13,4,15,5,1,0,4,1,0,48,57,7,0,37,37,43,43,45,46,
        48,57,65,90,95,95,97,122,4,0,45,46,48,57,65,90,97,122,2,0,9,10,13,
        13,51,0,1,1,0,0,0,0,3,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,24,1,0,0,0,9,29,1,0,
        0,0,11,33,1,0,0,0,13,40,1,0,0,0,15,45,1,0,0,0,17,18,5,58,0,0,18,
        2,1,0,0,0,19,20,5,44,0,0,20,4,1,0,0,0,21,22,7,0,0,0,22,6,1,0,0,0,
        23,25,7,1,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,
        0,0,0,27,8,1,0,0,0,28,30,7,2,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,10,1,0,0,0,33,34,3,7,3,0,34,35,5,64,
        0,0,35,36,3,9,4,0,36,37,5,46,0,0,37,38,3,9,4,0,38,12,1,0,0,0,39,
        41,3,5,2,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
        0,43,14,1,0,0,0,44,46,7,3,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,
        1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,6,7,0,0,50,16,1,0,0,0,
        5,0,26,31,42,47,1,6,0,0
    ]

class TextRecognizerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COLON = 1
    COMMA = 2
    EMAIL = 3
    MELLI_NUMBER = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COLON", "COMMA", "EMAIL", "MELLI_NUMBER", "WS" ]

    ruleNames = [ "COLON", "COMMA", "DIGIT", "LOCAL_SUBPART", "DOMAIN_SUBPART", 
                  "EMAIL", "MELLI_NUMBER", "WS" ]

    grammarFileName = "TextRecognizer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


