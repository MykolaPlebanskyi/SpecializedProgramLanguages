from labwork_1.functions import check_exeption


def calculation_float(number1, number2, operator):
    if operator in ['+', '-', '*']:
        if operator == "+":
            result = number1 + number2
            return result
        elif operator == '-':
            result = number1 - number2
            return result
        elif operator == '*':
            result = number1 * number2
            return result
    elif operator == '/':
        result = number1 / number2
        return result


def check_division_float(number1, number2, operator):
    if operator == '/':
        if check_exeption.check_division_zero(number1, number2):
            return True
        else:
            result = calculation_float(number1, number2, operator)
            return print(f"{number1} {operator} {number2} = {result:.2f}")
    else:
        result = calculation_float(number1, number2, operator)
        return print(f"{number1} {operator} {number2} = {result:.2f}")