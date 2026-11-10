# Laboratory Measurement Converter

A Python command-line program that converts laboratory temperature measurements from Celsius to Fahrenheit.

## Overview

The Laboratory Measurement Converter simulates a scientific laboratory recording the temperature of a chemical reaction and converting the measurement into Fahrenheit.

The program uses a Celsius measurement, performs a mathematical conversion, and displays both temperature values in the terminal.

## Example Output

```text 
Chemical Reaction Temperature
---------------------------------------------------
Celsius: 32 °C
Fahrenheit: 89.6 °F
```

## Conversion Formula

Fahrenheit is calculated using the following formula:

`F = (C × 9 / 5) + 32`

Where:

- `C` represents the Celsius temperature.
- `F` represents the Fahrenheit temperature.

## Concepts Practised

- `Variables and assignment` — storing measurements and calculated results.
- `Variable reuse` — using stored measurements in calculations and output.
- `Arithmetic expressions` — performing mathematical operations with variables.
- `Numeric types` — working with integers and floating-point results.
- `Reassignment` — changing a measurement and recalculating the result.
- `Redundant assignments` — identifying unnecessary variables.
- `F-strings` — displaying variable values in formatted output.
- `"print()"` — displaying a scientific measurement report.

## Test Cases

Celsius|Expected Fahrenheit
-------|--------------------
25| 77.0
0| 32.0
100| 212.0
-40| -40.0

All test cases passed.

## How to Run

Requirements: Python 3 installed.

Run the program from the project directory:

python main.py

Depending on your installation, you may need:

python3 main.py

## Project Structure

```text
004-lab-measurement-converter/
└── main.py
```

## Learning Objective

This project demonstrates how variables can be used in mathematical expressions, how calculated results can be stored and reused, and how Python produces numerical results from arithmetic operations.

## Scope

This is an educational command-line program. It uses a predefined Celsius measurement and does not yet accept interactive input or perform scientific validation.

---

Part of the Python Variables Build-to-Learn series.