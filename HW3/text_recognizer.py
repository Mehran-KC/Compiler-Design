import re
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from antlr4 import FileStream
from gen.TextRecognizerLexer import TextRecognizerLexer 

emailFound = '[{}][bold magenta1] Email Found ==> [/bold magenta1] [bold cyan1]{}[/bold cyan1]'
urlFound = '[{}][bold sky_blue3] URL Found ==> [/bold sky_blue3] [bold cyan1]{}[/bold cyan1]'
postalFound = '[{}][bold bright_yellow] Postal Code Found ==> [/bold bright_yellow] [bold cyan1]{}[/bold cyan1]'
nationalFound = '[{}][bold red1] National Code Found ==> [/bold red1] [bold cyan1]{}[/bold cyan1]'
versionFound = '[{}][bold orchid1] APP_VERSION ==> [/bold orchid1] [bold cyan1]{}[/bold cyan1]'

def national_code_check(code, counter, table, tree) :
    code = str(code)
    if not 8 <= len(code) <= 10 or not code.isnumeric(): 
        return False
    
    code = '0' * (10 - len(code)) + code    
    total = 0
    control_digit = int(code[-1])

    for digit, index in zip(code, range(10,1,-1)):
        total += int(digit) * index

    reminder = total % 11
    
    valid = (reminder < 2 and reminder == control_digit) or (11 - reminder == control_digit)    
    
    if valid:
        table.add_row("", "", "", f"[bold red1]{code}[/bold red1]")
        tree.children[3].add(f"[bold red1]{code}[/bold red1]")
        Console().log(nationalFound.format(counter, code))
    return valid

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
                table.add_row("","",f"[bold bright_yellow]{token.text}[/bold bright_yellow]")
                tree.children[2].add(f"[bold bright_yellow]{token.text}[/bold bright_yellow]")
                Console().log(postalFound.format(counter, token.text))
                counter+=1

        elif (token.type == 7 ):
            table.add_row(f"[bold magenta1]{token.text}[/bold magenta1]")
            tree.children[0].add(f"[bold magenta1]{token.text}[/bold magenta1]")
            Console().log(emailFound.format(counter, token.text))
            counter+=1

        elif (token.type == 8):
            try:
                float(token.text.replace(".", ""))
                table.add_row("","","","",f"[bold orchid1]{token.text}[/bold orchid1]")
                tree.children[4].add(f"[bold orchid1]{token.text}[/bold orchid1]")
                Console
                counter+=1
            except:
                table.add_row("",f"[bold sky_blue3]{token.text}[/bold sky_blue3]")
                tree.children[1].add(f"[bold sky_blue3]{token.text}[/bold sky_blue3]")
                Console().log(urlFound.format(counter, token.text))
                counter+=1

if __name__ == "__main__":

    tree = Tree("Input")
    
    tree.add("[magenta1]Emails[/magenta1]")
    tree.add("[sky_blue3]URLs[/sky_blue3]")
    tree.add("[bright_yellow]Postal Codes[/bright_yellow]")
    tree.add("[red1]National Codes[/red1]")
    tree.add("[orchid1]APP_VERSION[/orchid1]")
    tree.centering = "center"

    table = Table(title="[bold]Text Recognizer[/bold]")
    table.add_column("[magenta1]Emails[/magenta1]", justify="center", no_wrap=True)
    table.add_column("[sky_blue3]URLs[/sky_blue3]", justify="center", no_wrap=True)
    table.add_column("[bright_yellow]Postal Codes[/bright_yellow]", justify="center", no_wrap=True)
    table.add_column("[red1]National Codes[/red1]", justify="center", no_wrap=True)
    table.add_column("[orchid1]APP_VERSION[/orchid1]", justify="center", no_wrap=True)
    
    console = Console()
    main(table, tree)
    print("\n")
    console.print(Panel(table, expand=False, border_style="green"))
    print("\n")
    console.print(tree, style="bold")