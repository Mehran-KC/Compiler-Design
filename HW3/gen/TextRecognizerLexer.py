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
        4,0,8,140,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,4,2,27,8,2,11,
        2,12,2,28,1,3,4,3,32,8,3,11,3,12,3,33,1,4,1,4,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,65,8,6,11,6,12,6,66,3,6,69,8,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,4,6,78,8,6,11,6,12,6,79,3,6,82,8,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,95,8,6,11,6,12,6,96,3,
        6,99,8,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,107,8,6,11,6,12,6,108,3,6,111,
        8,6,3,6,113,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,3,7,130,8,7,1,8,1,8,1,9,4,9,135,8,9,11,9,12,9,136,1,
        9,1,9,0,0,10,1,1,3,2,5,0,7,0,9,3,11,4,13,5,15,6,17,7,19,8,1,0,4,
        7,0,37,37,43,43,45,46,48,57,65,90,95,95,97,122,4,0,45,46,48,57,65,
        90,97,122,1,0,48,57,2,0,9,10,13,13,152,0,1,1,0,0,0,0,3,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,
        19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,26,1,0,0,0,7,31,1,0,0,0,9,
        35,1,0,0,0,11,41,1,0,0,0,13,112,1,0,0,0,15,129,1,0,0,0,17,131,1,
        0,0,0,19,134,1,0,0,0,21,22,5,58,0,0,22,2,1,0,0,0,23,24,5,44,0,0,
        24,4,1,0,0,0,25,27,7,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,
        0,0,28,29,1,0,0,0,29,6,1,0,0,0,30,32,7,1,0,0,31,30,1,0,0,0,32,33,
        1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,8,1,0,0,0,35,36,3,5,2,0,36,
        37,5,64,0,0,37,38,3,7,3,0,38,39,5,46,0,0,39,40,3,7,3,0,40,10,1,0,
        0,0,41,42,3,17,8,0,42,43,3,17,8,0,43,44,3,17,8,0,44,45,3,17,8,0,
        45,46,3,17,8,0,46,47,3,17,8,0,47,48,3,17,8,0,48,49,3,17,8,0,49,50,
        3,17,8,0,50,51,3,17,8,0,51,12,1,0,0,0,52,53,3,15,7,0,53,54,5,119,
        0,0,54,55,5,119,0,0,55,56,5,119,0,0,56,57,5,46,0,0,57,58,1,0,0,0,
        58,59,3,5,2,0,59,68,5,46,0,0,60,69,3,7,3,0,61,62,3,7,3,0,62,64,5,
        47,0,0,63,65,3,7,3,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,
        67,1,0,0,0,67,69,1,0,0,0,68,60,1,0,0,0,68,61,1,0,0,0,69,113,1,0,
        0,0,70,71,3,15,7,0,71,72,3,5,2,0,72,81,5,46,0,0,73,82,3,7,3,0,74,
        75,3,7,3,0,75,77,5,47,0,0,76,78,3,7,3,0,77,76,1,0,0,0,78,79,1,0,
        0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,73,1,0,0,0,81,74,
        1,0,0,0,82,113,1,0,0,0,83,84,5,119,0,0,84,85,5,119,0,0,85,86,5,119,
        0,0,86,87,5,46,0,0,87,88,1,0,0,0,88,89,3,5,2,0,89,98,5,46,0,0,90,
        99,3,7,3,0,91,92,3,7,3,0,92,94,5,47,0,0,93,95,3,7,3,0,94,93,1,0,
        0,0,95,96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,90,
        1,0,0,0,98,91,1,0,0,0,99,113,1,0,0,0,100,101,3,5,2,0,101,110,5,46,
        0,0,102,111,3,7,3,0,103,104,3,7,3,0,104,106,5,47,0,0,105,107,3,7,
        3,0,106,105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,
        0,0,109,111,1,0,0,0,110,102,1,0,0,0,110,103,1,0,0,0,111,113,1,0,
        0,0,112,52,1,0,0,0,112,70,1,0,0,0,112,83,1,0,0,0,112,100,1,0,0,0,
        113,14,1,0,0,0,114,115,5,104,0,0,115,116,5,116,0,0,116,117,5,116,
        0,0,117,118,5,112,0,0,118,119,5,58,0,0,119,120,5,47,0,0,120,130,
        5,47,0,0,121,122,5,104,0,0,122,123,5,116,0,0,123,124,5,116,0,0,124,
        125,5,112,0,0,125,126,5,115,0,0,126,127,5,58,0,0,127,128,5,47,0,
        0,128,130,5,47,0,0,129,114,1,0,0,0,129,121,1,0,0,0,130,16,1,0,0,
        0,131,132,7,2,0,0,132,18,1,0,0,0,133,135,7,3,0,0,134,133,1,0,0,0,
        135,136,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,
        138,139,6,9,0,0,139,20,1,0,0,0,14,0,28,33,66,68,79,81,96,98,108,
        110,112,129,136,1,6,0,0
    ]

class TextRecognizerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COLON = 1
    COMMA = 2
    EMAIL = 3
    MELLI_NUMBER = 4
    URL = 5
    PROTOCOL = 6
    DIGIT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COLON", "COMMA", "EMAIL", "MELLI_NUMBER", "URL", "PROTOCOL", 
            "DIGIT", "WS" ]

    ruleNames = [ "COLON", "COMMA", "LOCAL_SUBPART", "DOMAIN_SUBPART", "EMAIL", 
                  "MELLI_NUMBER", "URL", "PROTOCOL", "DIGIT", "WS" ]

    grammarFileName = "TextRecognizer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


