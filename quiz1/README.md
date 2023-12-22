# Calculator using ANTLR4 and Python

This repository contains a simple calculator implemented using ANTLR4 and Python. The calculator can handle basic arithmetic expressions with addition, subtraction, multiplication, division, and exponentiation.

## How to Use

### Prerequisites

Make sure you have Python and ANTLR4 installed on your machine.

- Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install ANTLR4: [https://www.antlr.org/](https://www.antlr.org/)

## How to Use

Ensure you have ANTLR installed. If not, you can install it using:

    ```bash
    pip install antlr4-python3-runtime
    ```
### Generating ANTLR Files

To generate the ANTLR files, run the following command in your terminal:

```bash
antlr4 -Dlanguage=Python3 -visitor Calculator.g4
```

### Running the Calculator

Execute the `Main.py` script to input an arithmetic expression and obtain the result. For example:

```bash
python Main.py
```

Enter the arithmetic expression when prompted. The calculator will parse the expression and display the result.

### Example

```python
input_expr = "3*2+6-(7/9)+7^3*9-10"
```
For input of `3*2+6-(7/9)+7^3*9-10` output should be like image below:
[![Screenshot-from-2023-12-22-13-22-35.png](https://i.postimg.cc/vHW7N6fS/Screenshot-from-2023-12-22-13-22-35.png)](https://postimg.cc/tY4V1Jrh)

### Grammar

The calculator grammar is defined in the `Calculator.g4` file. It includes rules for numbers, basic arithmetic operations, parentheses, and exponentiation.

### Python Code

The `Main.py` file contains the Python code that uses the generated ANTLR files to parse and evaluate arithmetic expressions. The code defines a visitor (`CalculatorEvalVisitor`) that traverses the parse tree and performs the necessary calculations.

