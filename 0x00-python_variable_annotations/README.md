# Type annotations in Python 3

Python 3 introduced type annotations, which allow you to specify the expected types for function parameters and return values. This can help catch type-related errors during development and make your code more readable and maintainable.

## How to use type annotations

def greet(name: str) -> str:
return f"Hello, {name}!"

In this example, `name: str` specifies that the `name` parameter should be a string, and `-> str` specifies that the function should return a string.

## Variable type annotations

You can also annotate variable types:

x: int = 5
y: float = 3.14

## Duck typing

Python follows the "duck typing" philosophy, which means that an object's type is less important than the methods and attributes it has. This allows for more flexibility and dynamic programming.

## Validating code with mypy

Mypy is a static type checker for Python that can analyze your code and catch type-related errors. To use it, you'll need to install it and run it on your code:

$ pip install mypy
$ mypy your_file.py

Mypy will analyze your code and report any type-related errors or inconsistencies. This can help catch bugs before they happen and make your code more robust.
