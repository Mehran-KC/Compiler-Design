# Code Analysis Comparison - OpenUnderstand vs. Understand

This project involves the analysis of a Java codebase using two different tools: OpenUnderstand and the original Understand tool. Below, we provide details on how to use both tools and compare the results.

## OpenUnderstand

### Overview

OpenUnderstand is a custom library used for code analysis. The analysis script (`test_run.py`) uses OpenUnderstand to open an database and retrieve information about classes in the codebase.

### Usage

1. Clone the OpenUnderstand repository:
   ```bash
   git clone https://github.com/m-zakeri/OpenUnderstand.git
   cd OpenUnderstand
   git fetch
   git checkout -b dev origin/dev
   ```

2. Make things costumize in config.ini, test_openunderstand.py and test_run.py

### Results

The OpenUnderstand analysis script reports the following classes:

 - ss2 (Java Unknown Class Type Member)
 - String (Java Unknown Class Type Member)
 - ss2 (Java Unknown Class Type Member)
 - System (Java Unknown Class Type Member)
 - ss2 (Java Class Type Default Member)
 - ss1 (Java Class Type Public Member)

**Number of Classes: 6**

[![Screenshot-from-2024-01-03-02-46-35.png](https://i.postimg.cc/g08D8J80/Screenshot-from-2024-01-03-02-46-35.png)](https://postimg.cc/Y42YwtXc)

## Original Understand Tool

### Overview

The original Understand tool is a commercial code analysis tool. The analysis script (`api.py`) uses the Understand Python API to analyze the Java code and print information about the classes.

### Usage

1. Install the Understand tool from [SciTools website](https://scitools.com/download/all-products/).

2. Run the analysis script in test Directory:
   ```bash
   python api.py
   ```

### Results

The original Understand analysis script reports the following classes:

- String
- ss1
- ss2

**Number of Classes: 3**

[![Screenshot-from-2024-01-03-02-44-01.png](https://i.postimg.cc/X71Q0tnn/Screenshot-from-2024-01-03-02-44-01.png)](https://postimg.cc/MvRy7PcL)

## Comparison

While both tools aim to analyze the codebase, there are differences in the reported classes. OpenUnderstand identifies additional classes such as ".", "..", and ".String", which might be system-defined entities. Understanding these differences can help in choosing the tool that best suits your analysis needs.

Feel free to explore and compare the results further based on your specific requirements.

