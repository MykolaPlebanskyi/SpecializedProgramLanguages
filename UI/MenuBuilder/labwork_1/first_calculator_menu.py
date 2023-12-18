from UI.MenuBuilder.menu_builder import Menu
from Classes.labwork_1 import main as labwork_1
from Shared.Choice.run_again import RunAgain


class FirstCalculatorMenu(Menu):
    """
    Represents the menu for the first calculator.
    """

    def run(self):
        while True:
            labwork_1.main()
            break

