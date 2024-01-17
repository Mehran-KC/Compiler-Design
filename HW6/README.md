# Understand Python Code Analyzer with Rich Display

## Overview

This Python script utilizes the Scientific Toolworks Understand API to analyze a Java codebase and presents the results using the Rich library for a visually appealing display. The script focuses on identifying references related to variable setting and initialization within different entities (e.g., classes, methods) of the code.

## Prerequisites

Before running the script, ensure you have the following:

- [Scientific Toolworks Understand](https://scitools.com/) installed.
- Understand Python API accessible in your Python environment.
- Rich library installed:

  ```bash
  pip install rich
  ```

## Setup

1. Add the Understand Python API path to the system path:

   ```bash
   sys.path.append("/path/to/Understand/Python/API")
   ```

2. Open an Understand database:

   ```python
   db = understand.open("/path/to/your/codebase.udb")
   ```

## Usage

Run the script to extract information about variable setting and initialization references:

```bash
python eyval.py
```

## Output

The script categorizes references into the following and displays the results using the Rich library:

- **Set:**
  - **Description:** Instances where a variable is being set, assigned, or modified.
  - **Example:** `VariableExample.initializedVar` is identified, suggesting that the variable `initializedVar` is being set.

- **SetBy:**
  - **Description:** Instances where a variable is set by another entity or method.
  - **Example:** `VariableExample.SV.setVar` and `VariableExample.S.variableSetBy` suggest that the variables are being set by methods or entities named `SV` and `S`, respectively.

- **Set Init:**
  - **Description:** Instances where a variable is initialized, i.e., given an initial value.
  - **Example:** `VariableExample.initializedVar` is mentioned, suggesting that the variable `initializedVar` is initialized somewhere in the code.

- **SetBy Init:**
  - **Description:** Instances where a variable is initialized by another entity or method.
  - **Example:** `VariableExample.P.variableSetAndInitBy` suggests that the variable is both set and initialized by the method or entity named `P`.

- **Set Partial:**
  - **Description:** Instances where a variable is partially set, indicating that the setting process might be incomplete.
  - **Example:** (No output provided)

- **SetBy Partial:**
  - **Description:** Instances where a variable is partially set by another entity or method, indicating an incomplete setting process by an external entity.
  - **Example:** (No output provided)

The results are presented in a visually organized table format.

## Sample Output
##### Output is something like ScreenShot below :

[![Screenshot-from-2024-01-17-16-55-43.png](https://i.postimg.cc/KjDB8JpJ/Screenshot-from-2024-01-17-16-55-43.png)](https://postimg.cc/bSds6Hht)

## Notes

- Ensure that the Understand database path, API path, and Rich library are correctly set in the script.
- Customize the script to match the structure of your codebase.

