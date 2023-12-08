# HW2

This is a simple Python script that uses ANTLR4 to parse a simple language and print the parse tree. The grammar defines a rule for a simple greeting message.
This script takes a string of letters as input and removes newline (\n), tab (\t), and carriage return (\r) characters before parsing.

## Getting Started

### Prerequisites

Make sure you have Python and ANTLR4 installed on your machine.

- [Python](https://www.python.org/downloads/)
- [ANTLR4](https://www.antlr.org/)

### Installation

1. Install ANTLR4 using the official installation instructions: [ANTLR4 - Getting Started](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

2. Install the Python runtime for ANTLR4:

```bash
   pip install antlr4-python3-runtime
```
### Running the Example
1. Clone this repository:
```bash
   git clone https://github.com/Mehran-KC/Compiler-Design.git
   cd Compiler-Design/HW2
   ```
[Screenshot-from-2023-12-09-01-03-40.png](https://postimg.cc/N2409CLM)

2. Run the Main.py script:
```bash
   python Main.py
```
[Screenshot-from-2023-12-09-01-04-05.png](https://postimg.cc/t7tdNXx1)

** This will parse the input string 'Hello \n Mehran' according to the defined grammar and print the parse tree. **

### To use a different input, modify the input_stream in the Main.py script.
