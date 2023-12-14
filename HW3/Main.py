# EmailParserMain.py

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from gen.TextRecognizerLexer import TextRecognizerLexer  # Update this import
from gen.TextRecognizerParser import TextRecognizerParser
from gen.TextRecognizerListener import TextRecognizerListener 

def main():
    
    input_file = "input.txt" 
    input_stream = FileStream(input_file)
    lexer = TextRecognizerLexer(input_stream)
    for token in lexer.getAllTokens():
        if(token.type == 3):
            print("Found email:", token.text)
        if(token.type == 4):
            print("MELLI CODE Found:", token.text)
    token_stream = CommonTokenStream(lexer)
    parser = TextRecognizerParser(token_stream)
    tree = parser.emails()
    walker = ParseTreeWalker()

if __name__ == "__main__":
    main()

