import unittest

from colorama import Fore, Style

from labwork_6 import variables
from labwork_6.errors import Error
from labwork_6.testCalculatorAddition import TestCalculatorAddition
from labwork_6.testCalculatorDivision import TestCalculatorDivision
from labwork_6.testCalculatorMultiplication import TestCalculatorMultiplication
from labwork_6.testCalculatorSubtract import TestCalculatorSubtraction
from labwork_6.testErrorHandling import TestErrorHandling


class Interface:

    def __init__(self):
        self.error = Error()
        self.suite = unittest.TestSuite()
        self.loader = unittest.TestLoader()

    def user_interface(self):
        while True:

            choice = self.get_input(variables.user_input, self.error.number_input_check, variables.error_input)
            if choice == '1':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorAddition))
                return self.suite
            elif choice == '2':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorSubtraction))
                return self.suite
            elif choice == '3':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorMultiplication))
                return self.suite
            elif choice == '4':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorDivision))
                return self.suite
            elif choice == '5':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestErrorHandling))
                return self.suite

    def get_input(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return value
            print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

