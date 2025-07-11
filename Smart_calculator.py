import math
def add(x, y):
    """Return the sum of x and y."""
    return x + y
def subtract(x, y):
    """Return the difference of x and y."""
    return x - y
def multiply(x, y):
    """Return the product of x and y."""
    return x * y
def divide(x, y):
    """Return the quotient of x and y. Raises ValueError if y is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
operations = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
if operations not in ['add', 'subtract', 'multiply', 'divide']:
    raise ValueError("Invalid operation. Please choose from add, subtract, multiply, or divide.")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
if operations == 'add':
    result = add(x, y)
elif operations == 'subtract':
    result = subtract(x, y)
elif operations == 'multiply':
    result = multiply(x, y)
elif operations == 'divide':
    result = divide(x, y)
print(f"The result of {operations}ing {x} and {y} is: {result}")