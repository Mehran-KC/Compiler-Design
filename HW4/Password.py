from antlr4 import *
from gen.PasswordLexer import PasswordLexer
from gen.PasswordParser import PasswordParser

class PasswordListener(ParseTreeListener):
    def exitPassword(self, ctx):
        password = ctx.getText()
        if isValidPassword(password):
            print("Valid password: ", password)
        else:
            print("Invalid password: ", password)

def isValidPassword(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in '!@#$%^&*()_+{}|:"<>?`-=[]\';,./' for c in password)

if __name__ == '__main__':
    input_stream = InputStream("YourPassword123!") #Your input :)
    lexer = PasswordLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PasswordParser(stream)
    tree = parser.password()

    listener = PasswordListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
