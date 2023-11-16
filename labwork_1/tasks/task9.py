from labwork_1 import variables


def history():
    print("History of computing:")
    for i, calculation in enumerate(variables.history):
        number1, number2, operator, res = calculation
        if operator != '√':
            print(f"{i + 1}: {number1} {operator} {number2} = {res:.2f}")
        else:
            print(f"{i + 1}: {number1} {operator} = {res:.2f}")