def calculation(number1, number2, operator):
    if operator == "+":
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        result = number1 / number2

    return print(f"{number1} {operator} {number2} = {result}")
