"""
    This module contains functions for performing mathematical operations
and managing a history of calculations.
    It includes a function for performing operations like addition,
subtraction, multiplication, division, modulus, power, and square root.
    It also includes a function for printing the history of calculations.
"""
import json

from Shared.Choice.run_again import RunAgain
from Shared.Validate.validate import Validate
import math

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    config = config['variables']
    config = config['labwork_1']


def calculate(first_number: float, second_number: float, operator: str):
    """
    Performs a mathematical operation on two numbers.

    Args:
        first_number (float): The first number.
        second_number (float): The second number.
        operator (str): The operator representing the mathematical operation.

    Returns:
        float or None: The result of the mathematical operation, or None if an error occurs.
    """
    operations = {
        '+': first_number.__add__,
        '-': first_number.__sub__,
        '*': first_number.__mul__,
        '/': first_number.__truediv__,
        '%': first_number.__mod__,
        '^': first_number.__pow__,
        '√': math.sqrt
    }
    try:
        if operator == '√' and first_number < 0:
            print(config["error_zero"])
            return None
        return operations[operator](second_number if operator != '√' else first_number)
    except ZeroDivisionError:
        print(config["error_sqrt"])
        return None


def print_history(history):
    """
    Prints the history of calculations.

    Args:
        history (list): List of tuples representing each calculation.
            Each tuple contains the first number, second number (if applicable),
            operator, result, and decimal places.

    Returns:
        None
    """
    print("History:")
    for i, (first_number, second_number, operator, result, decimal_places) in enumerate(history):
        print(
            f"{i + 1}: {first_number} {operator} "
            f"{second_number if operator != '√' else ''} = "
            f"{result:.{decimal_places}f}")


def main():
    """
    This function represents the main logic of the program.
    It takes user input for numbers and operator, performs calculations,
    and stores the history of calculations.
    """
    history = []
    validate = Validate()
    run_again = RunAgain()
    while True:
        first_number = validate.get_input(config["first_number"], float)
        operator = validate.get_input(config["operator"],
                                      valid_input=['+', '-', '*', '/', '%', '^', '√'])
        second_number = validate.get_input(config["second_number"],
                                           float) if operator != '√' else None
        result = calculate(first_number, second_number, operator)
        if result is not None:
            decimal_places = validate.get_input(config["numbers"], int)
            print(f"{first_number} {operator} {second_number if operator != '√' else ''}"
                  f" = {result:.{decimal_places}f}")
            history.append((first_number, second_number, operator, result, decimal_places))
            print_history(history)

        if run_again.get_choice():
            break
