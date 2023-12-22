from antlr4 import *
from gen.CalculatorLexer import CalculatorLexer
from gen.CalculatorParser import CalculatorParser
from gen.CalculatorVisitor import CalculatorVisitor

class CalculatorEvalVisitor(CalculatorVisitor):
    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.term(i))
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.factor(i))
            if op == '*':
                result *= right
            elif op == '/':
                result /= right
        return result

    def visitFactor(self, ctx):
        return self.visit(ctx.power())

    def visitPower(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.atom(0))
        else:
            base = self.visit(ctx.atom(0))
            exponent = self.visit(ctx.atom(1))
            return base ** exponent

    def visitAtom(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        else:
            return self.visit(ctx.expr())

input_expr = "3*2+6-(7/9)+7^3*9-10"
input_stream = InputStream(input_expr)
lexer = CalculatorLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = CalculatorParser(tokens)
tree = parser.expr()

eval_visitor = CalculatorEvalVisitor()
result = eval_visitor.visit(tree)
print(f"Result: {result}")
