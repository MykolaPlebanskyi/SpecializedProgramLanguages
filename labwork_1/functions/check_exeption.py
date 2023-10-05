import math

import variables


def check_division_zero(number1, number2):
    try:
        number1 / number2
    except ZeroDivisionError:
        print(variables.zero)
        return ZeroDivisionError


def check_sqrt_less_zero(number1):
    try:
        math.sqrt(number1)
    except ValueError:
        print(variables.sqrt)
        return ValueError
