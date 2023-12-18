"""
This module provides a Calculator class that performs basic arithmetic operations.
"""

import math
import random
from Shared.Validate.validate import Validate


class Calculator:
    """
    A simple calculator class.
    """

    def __init__(self, **kwargs):
        self._first_number = kwargs.get('first_number', 0)
        self._second_number = kwargs.get('second_number', 0)
        self._operator = kwargs.get('operator', '+')
        self._round = kwargs.get('custom_round', 0)
        self._result = None
        self.valid = Validate()

    def calculation(self):
        """
        Perform the calculation based on the provided operator.
        """
        operations = {
            '+': float.__add__,
            '-': float.__sub__,
            '*': float.__mul__,
            '/': float.__truediv__,
            '^': float.__pow__,
            '√': math.sqrt,
            '%': float.__mod__,
            'random': random.uniform
        }
        try:
            if self._operator == '√':
                self._result = operations[self._operator](self._first_number)
            else:
                self._result = operations[self._operator](self._first_number, self._second_number)
        except ZeroDivisionError:
            self._result = "Error: Division by zero is not allowed."
        except ValueError:
            self._result = "Error: Invalid value."

        return self

    def __str__(self):
        """
        Print the result.
        """
        if isinstance(self._result, str):
            return self._result
        if self._operator == '√':
            return f"Result: {self._first_number:.2f} {self._operator} = {self._result:.2f}"
        if self._operator in ('sin', 'cos', 'tan'):
            return f"Result: {self._operator}({self._first_number:.2f}°) = {self._result:.2f}"
        if self._operator == 'random':
            return (f"Random number from {self._first_number:.2f} to "
                    f"{self._second_number:.2f} is {self._result:.2f}")

        else:
            return (f"Result: {self._first_number:.2f} {self._operator} "
                    f"{self._second_number:.2f} = {self._result:.2f}")

    @property
    def operator(self):
        return self._operator
