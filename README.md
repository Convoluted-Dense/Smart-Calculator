# Smart-Calculator

Modular command-line mathematical utility providing arithmetic calculations, input validation, and extensible scientific operations.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

---

## Overview

Smart-Calculator is a clean, reliable command-line calculator written in Python. It features modular arithmetic functions, rigorous zero-division exception handling, and user prompt validation for core numerical operations.

---

## Features

- Core Arithmetic: Addition, Subtraction, Multiplication, and Division.
- Error Handling: Explicit zero-division protection via ValueError exceptions with clear user diagnostics.
- Clean Functional Design: Decoupled mathematical functions suitable for integration as a reusable utility module or standalone CLI.
- Zero External Dependencies: Operates entirely using Python standard library primitives.

---

## Repository Structure

```
Smart-Calculator/
├── Smart_calculator.py    # Main calculator implementation and interactive CLI loop
└── README.md              # Project documentation
```

---

## Installation & Execution

### Prerequisites
- Python 3.8 or higher

### Running the Calculator

1. Clone the repository:
```bash
git clone https://github.com/Convoluted-Dense/Smart-Calculator.git
cd Smart-Calculator
```

2. Execute the script:
```bash
python Smart_calculator.py
```

3. Follow the interactive prompts:
```
Enter the operation (add, subtract, multiply, divide): add
Enter first number: 25
Enter second number: 17
Result: 42
```

---

## Modular Usage

You can also import Smart_calculator.py as a module in other Python scripts:

```python
from Smart_calculator import add, subtract, multiply, divide

print(add(15, 30))         # 45
print(divide(100, 4))      # 25.0
```

---

## License

This project is licensed under the MIT License.
