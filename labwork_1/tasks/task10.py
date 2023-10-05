from labwork_1.functions import check_exeption
from labwork_1.functions import check_option


def check_root_floating(number1, number2, operator, numbers):
    if operator == '√':
        if check_exeption.check_sqrt_less_zero(number1):
            return True
        else:
            result = check_option.check_option(number1, number2, operator)
            print(f"{number1} {operator} = {result:.{numbers}f}")
            return result
    else:
        result = check_option.check_option(number1, number2, operator)
        print(f"{number1} {operator} {number2} = {result:.{numbers}f}")
        return result

