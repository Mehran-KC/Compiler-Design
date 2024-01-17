import os
import sys
from rich.console import Console
from rich.table import Table

sys.path.append(
    "/home/mehran/Downloads/Scientific.Toolworks.Understand.5.1.1023.Linux/Understand-5.1.1023-Linux-64bit/scitools/bin/linux64/Python"
)

import understand

db = understand.open(
    "/home/mehran/Desktop/Compiler-Design/HW6/src/hw6test.udb"
)

dbents = db.ents()

# Create a Rich Table
table = Table(title="Entity References")
table.add_column("Entity", justify="center", style="cyan")
table.add_column("Reference Type", justify="center", style="magenta")
table.add_column("Reference Entity", justify="center", style="green")

# Helper function to add rows to the table
def add_row(entity, ref_type, ref_entity):
    table.add_row(entity.longname(), ref_type, ref_entity.longname())

# Iterate through entities and references
for i in dbents:
    for ref in i.refs("Set,SetBy"):
        add_row(i, "Set,SetBy", ref.ent())
    for ref in i.refs("Set Init,SetBy Init"):
        add_row(i, "Set Init,SetBy Init", ref.ent())
    for ref in i.refs("Set Partial,SetBy Partial"):
        add_row(i, "Set Partial,SetBy Partial", ref.ent())

# Display the table using Rich Console
console = Console()
console.print(table)

