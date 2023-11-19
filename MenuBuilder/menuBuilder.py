import unittest

from labwork_1.calculator import main as labwork1
from labwork_2.interface import Interface as labwork2
from labwork_3.interface import Interface as labwork3
from labwork_4.interface import Interface as labwork4
from labwork_5.interface import Interface as labwork5
from labwork_6.interface import Interface as labwork6


def display_menu():
    print("\nWelcome to Menu Builder")
    print("1. Lab Work 1")
    print("2. Lab Work 2")
    print("3. Lab Work 3")
    print("4. Lab Work 4")
    print("5. Lab Work 5")
    print("6. Lab Work 6")
    print("7. Lab Work 7")
    print("8. Lab Work 8")
    print("9. Lab Work 9")
    print("10. Exit")
    print()


def option1():
    labwork1()


def option2():
    interface = labwork2()
    interface.run_calculator()


def option3():
    interface = labwork3()
    interface.user_input()


def option4():
    interface = labwork4()
    interface.user_input()


def option5():
    interface = labwork5()
    interface.user_input()


def option6():
    print("Will be available in the future...")


def option7():
    print("Will be available in the future...")


def option8():
    print("Will be available in the future...")


def option9():
    print("Will be available in the future...")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            option4()
        elif choice == '5':
            option5()
        elif choice == '6':
            option6()
        elif choice == '7':
            option7()
        elif choice == '8':
            option8()
        elif choice == '9':
            option9()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
