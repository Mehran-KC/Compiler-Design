# Password Validator

This repository contains a simple Python implementation for validating passwords using ANTLR (ANother Tool for Language Recognition). The provided ANTLR grammar defines the structure of a password, and the Python script utilizes this grammar to check the validity of a given password.

## Repository Structure

```
HW4/
|-- gen/
|   |-- Password.g4
|   |-- PasswordLexer.g4
|   |-- PasswordParser.g4
|   |-- ...
|-- Password.py
```

- **gen/**: Contains the ANTLR grammar and generated lexer and parser files.
- **Password.py**: Python script that uses ANTLR to validate passwords.

## How to Use

1. Ensure you have ANTLR installed. If not, you can install it using:

    ```bash
    pip install antlr4-python3-runtime
    ```

2. Run the ANTLR tool to generate lexer and parser files:

    ```bash
    antlr4 -Dlanguage=Python3 Password.g4
    ```

3. Execute the Password.py script:

    ```bash
    python Password.py
    ```

   Replace the `input_stream` variable in the script with the desired password for validation.

## Password Validation Rules

The password validation rules are defined in the `Password.g4` grammar file. The password must:

- Be at least 8 characters long.
- Contain at least one uppercase letter.
- Contain at least one lowercase letter.
- Contain at least one digit.
- Contain at least one special symbol from the set `!@#$%^&*()_+{}|:"<>?`-=[]\';,./`.

## Example

```python
from antlr4 import *
from gen.PasswordLexer import PasswordLexer
from gen.PasswordParser import PasswordParser

# ... (Code from Password.py)

if __name__ == '__main__':
    input_stream = InputStream("YourPassword123!")  # Replace with your desired password
    lexer = PasswordLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PasswordParser(stream)
    tree = parser.password()

    listener = PasswordListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
```

Replace `"YourPassword123!"` with the password you want to validate. The script will output whether the password is valid or not.

Feel free to customize the ANTLR grammar or the Python script according to your specific requirements.