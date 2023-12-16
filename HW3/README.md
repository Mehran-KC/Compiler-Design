# Text Recognizer

This repository contains a Python script (`text_recognizer.py`) that uses an ANTLR-generated lexer (`TextRecognizerLexer`) to identify and validate various text patterns in an input text file (`input.txt`). The script is designed to recognize and categorize email addresses, URLs, postal codes, national codes, and app version numbers.

## Folder Structure

The repository has the following structure:

- **HW3/**
  - **gen/**: Contains the ANTLR-generated lexer and parser files.
  - **text_recognizer.py**: The main Python script for text recognition.
  - **input.txt**: An example input file containing text for recognition.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- `rich`: A Python library for rich text output.
- `antlr4-python3-runtime`: The ANTLR runtime for Python.
- `antlr4`: A powerful parser generator for reading, processing, executing, or translating structured text or binary files.

You can install these dependencies using the following command:

```bash
pip install rich antlr4-python3-runtime
```

Make sure to include `antlr4-python3-runtime` in the list of dependencies to ensure the proper functioning of the ANTLR runtime in Python.

```bash
pip install rich antlr4 antlr4-python3-runtime
```

## Usage

To run the text recognizer script, execute the following command:

```bash
python text_recognizer.py
```

The script will process the contents of the `input.txt` file and display the recognized patterns in a tabular format using the `rich` library.

## Recognized Patterns

The script identifies the following patterns:

- **Emails**: Displayed in magenta.
- **URLs**: Displayed in sky blue.
- **Postal Codes**: Displayed in bright yellow.
- **National Codes**: Displayed in red.
- **App Version Numbers**: Displayed in orchid.

The recognized patterns are presented in a table for easy visualization.

## ANTLR Grammar

The ANTLR grammar file (`TextRecognizer.g4`) defines the rules for recognizing email addresses, URLs, and national identification numbers (Melli Numbers). The grammar also includes rules for skipping whitespace.

## Example Output

The script generates a tree structure to represent the recognized patterns. Additionally, a table is displayed using the `rich` library, providing a comprehensive view of the recognized text patterns.

[![Screenshot-from-2023-12-16-04-47-15.png](https://i.postimg.cc/rF6Jzd4q/Screenshot-from-2023-12-16-04-47-15.png)](https://postimg.cc/rzJWPwgH)

Feel free to explore and modify the input text file to test different scenarios and observe the script's recognition capabilities.

**Note**: Ensure that the input file (`input.txt`) is present in the same directory as the script.

For more details on the recognized patterns and ANTLR grammar rules, refer to the comments in the script and the grammar file.

**Happy Text Recognition!**
