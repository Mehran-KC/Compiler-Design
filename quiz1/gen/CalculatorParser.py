# Generated from Calculator.g4 by ANTLR 4.10.1
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
        4,1,10,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,
        1,1,2,1,2,1,3,1,3,1,3,3,3,32,8,3,1,4,1,4,1,4,1,4,1,4,3,4,39,8,4,
        1,4,0,0,5,0,2,4,6,8,0,2,1,0,1,2,1,0,3,4,39,0,10,1,0,0,0,2,18,1,0,
        0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,38,1,0,0,0,10,15,3,2,1,0,11,12,7,
        0,0,0,12,14,3,2,1,0,13,11,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,
        16,1,0,0,0,16,1,1,0,0,0,17,15,1,0,0,0,18,23,3,4,2,0,19,20,7,1,0,
        0,20,22,3,4,2,0,21,19,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,3,1,0,0,0,25,23,1,0,0,0,26,27,3,6,3,0,27,5,1,0,0,0,28,
        31,3,8,4,0,29,30,5,5,0,0,30,32,3,8,4,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,7,1,0,0,0,33,39,5,8,0,0,34,35,5,6,0,0,35,36,3,0,0,0,36,37,5,
        7,0,0,37,39,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,39,9,1,0,0,0,4,15,
        23,31,38
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "DIGIT", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_power = 3
    RULE_atom = 4

    ruleNames =  [ "expr", "term", "factor", "power", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    DIGIT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.TermContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.TermContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CalculatorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.term()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalculatorParser.T__0 or _la==CalculatorParser.T__1:
                self.state = 11
                _la = self._input.LA(1)
                if not(_la==CalculatorParser.T__0 or _la==CalculatorParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                self.term()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.FactorContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.FactorContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CalculatorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.factor()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalculatorParser.T__2 or _la==CalculatorParser.T__3:
                self.state = 19
                _la = self._input.LA(1)
                if not(_la==CalculatorParser.T__2 or _la==CalculatorParser.T__3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.factor()
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def power(self):
            return self.getTypedRuleContext(CalculatorParser.PowerContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CalculatorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.power()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.AtomContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.AtomContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_power

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)




    def power(self):

        localctx = CalculatorParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_power)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.atom()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CalculatorParser.T__4:
                self.state = 29
                self.match(CalculatorParser.T__4)
                self.state = 30
                self.atom()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CalculatorParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CalculatorParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculatorParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(CalculatorParser.NUMBER)
                pass
            elif token in [CalculatorParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(CalculatorParser.T__5)
                self.state = 35
                self.expr()
                self.state = 36
                self.match(CalculatorParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





