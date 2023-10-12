from labwork_2 import variables
from labwork_2.advanced_calculator import AdvancedCalculator
from labwork_2.errors import Error


class Interface(AdvancedCalculator):

    def _choice(self):
        return input(variables.choose_exit).lower() != 'yes'

    def run_calculator(self):
        error = Error()
        while True:
            first_number, operator, second_number = self._user_input()

            if not error.handle_errors(first_number, second_number, operator):
                self.result = self._calculation(first_number, second_number, operator)
                result = self.result
                if operator == '√':
                    print(f"Result: {first_number:.2f} {operator} = {result:.2f}")
                elif operator in ('sin', 'cos', 'tan'):
                    print(f"Result: {operator}({first_number:.2f}°) = {result:.2f}")
                elif operator == 'random':
                    print(f"Random number from {first_number:.2f} to {second_number:.2f} is {result:.2f}")
                else:
                    print(f"Result: {first_number:.2f} {operator} {second_number:.2f} = {result:.2f}")

            if self._choice():
                break

    def _user_input(self):
        error = Error()

        first_number = self.get_input(variables.first_number_input, error.number_input_check,
                                      variables.input_number_error)

        operator = ''
        while error.validate_operator(operator):
            operator = input(variables.operator_input)
            if error.validate_operator(operator):
                print(variables.operator_error)

        second_number = None
        if operator not in ('√', 'sin', 'cos', 'tan'):
            second_number = self.get_input(variables.second_number_input, error.number_input_check,
                                           variables.input_number_error)

        return first_number, operator, second_number

    def get_input(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return float(value)
            print(error_message)
