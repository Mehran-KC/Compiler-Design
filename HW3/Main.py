# EmailParserMain.py

import re
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from gen.TextRecognizerLexer import TextRecognizerLexer  # Update this import
from gen.TextRecognizerParser import TextRecognizerParser
from gen.TextRecognizerListener import TextRecognizerListener 


def national_code_check(code, counter, table, tree) :
    # CONSOLE WITH TIME AND SMT

    code = str(code)
    if not code.isnumeric():
        return False
    if len(code) != 10:
        code = '0' * (10 - len(code)) + code
    total = 0
    control_digit = int(code[-1])
    for digit, index in zip(code, range(10,1,-1)):
        total += int(digit) * index

    reminder = total % 11
    if reminder < 2:
        if reminder == control_digit:
            table.add_row("","","",f"[bold purple]{code}[/bold purple]")
            tree.children[3].add(f"[bold purple]{code}[/bold purple]")
            print(f"[{counter}] [bold purple]National Code Found  ==> [/bold purple] {code}")
            return True
    else:
        if 11 - reminder == control_digit:
            table.add_row("","","",f"[bold purple]{code}[/bold purple]")
            tree.children[3].add(f"[bold purple]{code}[/bold purple]")
            print(f"[{counter}] [bold purple]National Code Found  ==> [/bold purple] {code}")
            return True
    return False

def validate_postal_code(postal_code):
    pattern = r'\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b'
    return bool(re.fullmatch(pattern, postal_code))

    
def main(table, tree):
    counter = 1
    
    input_file = "input.txt" 
    input_stream = FileStream(input_file)
    lexer = TextRecognizerLexer(input_stream)
    
    for token in lexer.getAllTokens():
        if (token.type == 6):
            if national_code_check(token.text,counter, table, tree):
                counter+=1
                continue
            national_code_check(token.text,counter, table, tree)

            if validate_postal_code(token.text):
                table.add_row("","",f"[bold yellow]{token.text}[/bold yellow]")
                tree.children[2].add(f"[bold yellow]{token.text}[/bold yellow]")
                print(f"[{counter}][bold yellow] Postal Code Found ==> [/bold yellow] [bold Green]{token.text}[/bold Green]")
                counter+=1

        elif (token.type == 7 ):
            table.add_row(f"[bold Magenta]{token.text}[/bold Magenta]")
            tree.children[0].add(f"[bold Magenta]{token.text}[/bold Magenta]")
            print(f"[{counter}][bold Magenta] Email FOUND ==> [/bold Magenta] [bold Green]{token.text}[/bold Green]")
            counter+=1

        elif (token.type == 8):
            table.add_row("",f"[bold red]{token.text}[/bold red]")
            tree.children[1].add(f"[bold red]{token.text}[/bold red]")
            print(f"[{counter}][bold red] URL FOUND  ==> [/bold red] [bold Green]{token.text}[/bold Green]")
            counter+=1


    token_stream = CommonTokenStream(lexer)
    parser = TextRecognizerParser(token_stream)
    tree = parser.emails()
    walker = ParseTreeWalker()

if __name__ == "__main__":

    tree = Tree("")
    tree.add("Emails")
    tree.add("URLs")
    tree.add("Postal Codes")
    tree.add("National Codes")
    tree.centering = "center"
    table = Table(title="[bold]Text Recognizer[/bold]")
    table.add_column("Emails", justify="center", style="cyan", no_wrap=True)
    table.add_column("URLs", justify="center", style="magenta", no_wrap=True)
    table.add_column("Postal Codes", justify="center", style="green", no_wrap=True)
    table.add_column("National Codes", justify="center", style="red", no_wrap=True)

    main(table, tree)
    print("\n")
    console = Console()
    console.print(Panel(table, expand=False, border_style="green"))
    print("\n")
    #print tree as panel
    console.print(tree, style="bold")