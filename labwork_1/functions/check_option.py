from labwork_1.tasks import task2, task6, task7


def check_option(number1, number2, operator):
    if task2.check_operator(operator):
        return task6.calculation_float(number1, number2, operator)
    else:
        return task7.calculation_additional_float(number1, number2, operator)


def check_zero_float(number1, number2, operator):
    if task2.check_operator(operator):
        return task6.check_division_float(number1, number2, operator)
    else:
        return task7.check_root_float(number1, number2, operator)
