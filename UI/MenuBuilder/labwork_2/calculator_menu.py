from Classes.labwork_2.calculator import Calculator
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class CalculatorMenu(Menu):
    """
    Represents a menu for a calculator application.

    Attributes:
        _calculator (Calculator): The calculator object used for calculations.
        _run_again (RunAgain): The object used to determine if the menu should run again.
        _config (dict): The configuration settings for the menu.
    """

    def __init__(self):
        super().__init__()
        self._calculator = Calculator()
        self._run_again = RunAgain()
        self._config = self._config['labwork_2']

    def run(self):
        """
        Runs the calculator menu.

        The menu prompts the user for input, performs calculations using the calculator object,
        and displays the result. The menu continues to run until the user chooses to exit.
        """
        while True:
            self._calculator._first_number = (self._calculator.valid.get_input
                                             (self._config["first_number"], float))
            self._calculator._operator = (self._calculator.valid.get_input
                                         (self._config["operator"], str,
                                          valid_input=['+', '-', '*', '/',
                                                       '%', '^', '√','random']))
            if self._calculator.operator != '√':
                self._calculator._second_number = (self._calculator.valid.get_input
                                                  (self._config["second_number"], float))
            result = self._calculator.calculation()  # Store the result

            print(result)  # Print the result

            if self._run_again.get_choice():
                break
