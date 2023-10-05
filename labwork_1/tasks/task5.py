from labwork_1.functions import check_exeption
from labwork_1.tasks import task3


def check_division(number1, number2, operator):
    if operator == '/':
        if check_exeption.check_division_zero(number1, number2):
            return True
        else:
            task3.calculation(number1, number2, operator)
    else:
        task3.calculation(number1, number2, operator)
