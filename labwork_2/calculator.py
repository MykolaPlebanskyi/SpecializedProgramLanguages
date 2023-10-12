import random


class Calculator:
    def __init__(self):
        self.first_number = None
        self.second_number = None
        self.operator = None
        self.result = None

    def _calculation(self, first_number, second_number, operator):
        if operator == '+':
            return first_number + second_number
        elif operator == '-':
            return first_number - second_number
        elif operator == '*':
            return first_number * second_number
        elif operator == '/':
            return first_number / second_number
        elif operator == '^':
            return first_number ** second_number
        elif operator == '√':
            return first_number ** 0.5
        elif operator == '%':
            return first_number % second_number
        elif operator == 'random':
            return random.uniform(first_number, second_number)
