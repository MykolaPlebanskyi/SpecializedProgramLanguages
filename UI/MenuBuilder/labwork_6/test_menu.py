import unittest


from Classes.labwork_6.test import Test
from Classes.labwork_6.testCalculatorAddition import TestCalculatorAddition
from Classes.labwork_6.testCalculatorDivision import TestCalculatorDivision
from Classes.labwork_6.testCalculatorMultiplication import TestCalculatorMultiplication
from Classes.labwork_6.testCalculatorSubtract import TestCalculatorSubtraction
from Classes.labwork_6.testErrorHandling import TestErrorHandling
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class TestMenu(Menu):
    """
    Represents a menu for selecting and running test cases.

    Attributes:
        test (Test): An instance of the Test class.
        suite (unittest.TestSuite): A test suite to store the selected test cases.
        loader (unittest.TestLoader): A test loader to load test cases from test classes.
        run_again (RunAgain): An instance of the RunAgain class.

    Methods:
        run(): Runs the selected test cases in a loop until the user chooses to exit.
        display_menu(): Displays the menu options for selecting test cases.
    """
    def __init__(self):
        super().__init__()
        self.test = Test()
        self.suite = unittest.TestSuite()
        self.loader = unittest.TestLoader()
        self.run_again = RunAgain()

    def run(self):
        """
        Runs the selected test cases in a loop until the user chooses to exit.

        The function first displays the menu options for selecting test cases.
        The user selects a group of tests by entering a number corresponding to the
        test case they want to run. The selected test cases are added to a test suite,
        which is then executed using the unittest.TextTestRunner().run() method.
        After the tests are run, the test suite is cleared and the run_again menu is
        displayed to allow the user to repeat the tests or exit the program.

        Returns:
            None

        """
        while True:
            self.display_menu()
            choice = self.test.get_input()
            if choice == '1':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorAddition))
            elif choice == '2':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorSubtraction))
            elif choice == '3':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorMultiplication))
            elif choice == '4':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestCalculatorDivision))
            elif choice == '5':
                self.suite.addTest(self.loader.loadTestsFromTestCase(TestErrorHandling))

            unittest.TextTestRunner().run(self.suite)
            self.suite = unittest.TestSuite()  # Clear the suite for the next run

            if self.run_again.get_choice():
                break

    def display_menu(self):
        """
        Displays the menu options for selecting test cases.
    
        The function displays a menu with the options for selecting different test
        cases. The options are numbered sequentially, starting from 1, and include
        Addition, Division, Multiplication, Subtraction, and Error Handling.
    
        Returns:
            None
    
        """
        print("Select a group of tests:")
        print("1. Addition")
        print("2. Division")
        print("3. Multiplication")
        print("4. Subtract")
        print("5. Error Handling")
        print("Select a group of tests: \n 1. Addition\n 2. Division"
              "\n 3. Multiplication\n 4. Subtract\n "
              "5. Error Handling\n")

