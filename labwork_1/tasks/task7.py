from labwork_1.functions import check_exeption


def calculation_additional_float(number1, number2, operator):
    if operator in ['^', '%']:
        if operator == '^':
            result = number1 ** number2
            return result
        elif operator == '%':
            result = number1 % number2
            return result
    elif operator == '√':
        result = number1 ** 0.5
        return result


def check_root_float(number1, number2, operator):
    if operator == '√':
        if check_exeption.check_sqrt_less_zero(number1):
            return True
        else:
            result = calculation_additional_float(number1, number2, operator)
            return print(f"{number1} {operator} = {result:.2f}")
    else:
        result = calculation_additional_float(number1, number2, operator)
        return print(f"{number1} {operator} {number2} = {result:.2f}")
