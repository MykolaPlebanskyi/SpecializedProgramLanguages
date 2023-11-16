from labwork_1.functions import check_operator, check_option
from labwork_1 import variables
from labwork_1.tasks import task1, task2, task3, task5, task6, task7, task8, task9, task10


def main():
    print(variables.tasks)
    while True:
        selected_task = input(variables.task_choose)

        if selected_task in ['1', '2', '3', '4', '5']:
            number1 = int(input(variables.number1))
            operator = input(variables.operator)
            number2 = check_operator.check_sqrt(operator)

            if selected_task == '1':
                task1.output(number1, number2, operator)

            elif selected_task == '2':
                done_task2 = task2.check_operator(operator)
                print(done_task2)
                if not task2.check_operator(operator):
                    print(variables.error_operator)
                    continue

            elif selected_task == '3':
                if not task2.check_operator(operator):
                    print(variables.error_operator)
                    continue
                task3.calculation(number1, number2, operator)

            elif selected_task == '4':
                if not task2.check_operator(operator):
                    print(variables.error_operator)
                    continue
                task3.calculation(number1, number2, operator)
                repeat = input(variables.choose_exit)
                if repeat.lower() != "yes":
                    break

            elif selected_task == '5':
                if not task2.check_operator(operator):
                    print(variables.error_operator)
                    continue
                task5.check_division(number1, number2, operator)
                repeat = input(variables.choose_exit)
                if repeat.lower() != "yes":
                    break

        elif selected_task in ['6', '7', '8', '9', '10']:
            number1 = float(input(variables.number1))
            operator = input(variables.operator_additional)
            number2 = check_operator.check_sqrt_float(operator)

            if selected_task == '6':
                if not task2.check_operator(operator):
                    print(variables.error_operator)
                    continue
                task6.check_division_float(number1, number2, operator)

            elif selected_task == '7':
                if not task2.check_additional_operator(operator):
                    print(variables.error_operator)
                    continue
                if task2.check_operator(operator):
                    task6.check_division_float(number1, number2, operator)
                else:
                    task7.check_root_float(number1, number2, operator)

            elif selected_task == '8':
                if not task2.check_additional_operator(operator):
                    print(variables.error_operator)
                    continue
                if not check_option.check_zero_float(number1, number2, operator):
                    result = check_option.check_option(number1, number2, operator)
                    task8.working_memory(result)

            elif selected_task == '9':
                if not task2.check_additional_operator(operator):
                    print(variables.error_operator)
                    continue
                if not check_option.check_zero_float(number1, number2, operator):
                    result = check_option.check_option(number1, number2, operator)
                    variables.history.append((number1, number2, operator, result))
                    task9.history()

            elif selected_task == '10':
                if not task2.check_additional_operator(operator):
                    print(variables.error_operator)
                    continue
                if not check_option.check_zero_float(number1, number2, operator):
                    change_float = input(variables.change_float)
                    if change_float.lower() == "yes":
                        numbers = int(input(variables.numbers))
                        result = task10.check_root_floating(number1, number2, operator, numbers)
                    else:
                        result = check_option.check_option(number1, number2, operator)
                    task8.working_memory(result)
                    variables.history.append((number1, number2, operator, result))
                    task9.history()

            repeat = input(variables.choose_exit)
            if repeat.lower() != "yes":
                break
        else:
            print(variables.incorrect_choose)
            continue


if __name__ == "__main__":
    main()
