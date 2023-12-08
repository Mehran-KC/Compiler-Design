# Main.py
from antlr4 import InputStream, CommonTokenStream
from gen.HelloLexer import HelloLexer
from gen.HelloParser import HelloParser

input_stream = InputStream('Hello \n Mehran')

lexer = HelloLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = HelloParser(token_stream)

tree = parser.greet()

print(tree.toStringTree(recog=parser))
