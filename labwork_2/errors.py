import math
from labwork_2 import variables


class Error:

    def handle_errors(self, first_number, second_number, operator):
        if operator == '/':
            if second_number == 0:
                try:
                    first_number / second_number
                except ZeroDivisionError:
                    print(variables.zero)
                    return ZeroDivisionError
        elif operator == '√':
            try:
                math.sqrt(first_number)
            except ValueError:
                print(variables.sqrt)
                return ValueError
        elif operator == 'random':
            try:
                if first_number > second_number:
                    raise ValueError(variables.random)
            except ValueError as e:
                print(e)
                return ValueError

    def number_input_check(self, number):
        try:
            float(number)
        except ValueError:
            return ValueError()

    def validate_operator(self, operator):
        try:
            if operator not in ['+', '-', '*', '/', '%', '^', '√', 'random', 'sin', 'cos', 'tan']:
                raise ValueError()
        except ValueError:
            return ValueError()
