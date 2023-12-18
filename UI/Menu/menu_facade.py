from UI.MenuBuilder.labwork_1.first_calculator_menu import FirstCalculatorMenu
from UI.MenuBuilder.labwork_2.calculator_menu import CalculatorMenu
from UI.MenuBuilder.labwork_3.art_menu import ArtMenu
from UI.MenuBuilder.labwork_4.custom_art_menu import CustomArtMenu
from UI.MenuBuilder.labwork_5.parallelepiped_menu import ParallelepipedMenu
from UI.MenuBuilder.labwork_6.test_menu import TestMenu
from UI.MenuBuilder.labwork_7.data_api_menu import DataAPIMenu
from UI.MenuBuilder.labwork_8.data_visualizer_menu import DataVisualizerMenu

class MenuFacade:
    """
    The MenuFacade class represents a facade for managing different menus in a program.
    """

    def __init__(self):
        self.__menus = [("Labwork - First Calculator", FirstCalculatorMenu()),
                        ("Labwork - Calculator", CalculatorMenu()),
                        ("Labwork - Art Generator", ArtMenu()),
                        ("Labwork - Custom Art Generator", CustomArtMenu()),
                        ("Labwork - Parallelepiped", ParallelepipedMenu()),
                        ("Labwork - Tests", TestMenu()),
                        ("Labwork - Data API", DataAPIMenu()),
                        ("Labwork - Data Visualizer", DataVisualizerMenu())]
        self.__finish_number = 0

    def print_menu_options(self):
        """
        Prints the menu options to the console.
        """
        for index, (name, _) in enumerate(self.__menus, start=1):
            print(f"{index}. {name}")
        print(f"{self.__finish_number}. Exit")

    def start(self):
        while True:
            self.print_menu_options()
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice == self.__finish_number:
                    break
                if not 1 <= choice <= len(self.__menus):
                    raise ValueError
                _, menu = self.__menus[choice - 1]
                menu.run()
            except ValueError:
                print("Invalid choice. Enter again!")
def start(self):
    """
    Starts the menu facade by repeatedly prompting the user for a choice and
    starting the corresponding menu until the user chooses to exit.
    """
    while True:
        # Print the menu options
        self.print_menu_options()

        # Prompt the user for a choice
        choice = input("Enter your choice: ")

        # Try to convert the choice to an integer
        try:
            choice_int = int(choice)
        except ValueError:
            # The input was not a valid integer, print an error message and continue
            print("Invalid choice. Enter again!")
            continue

        # Check if the user chose to exit
        if choice_int == self.__finish_number:
            # The user chose to exit, so break out of the loop
            break

        # Check if the choice is a valid option
        if not 1 <= choice_int <= len(self.__menus):
            # The choice is not a valid option, print an error message and continue
            print("Invalid choice. Enter again!")
            continue

        # Extract the menu corresponding to the chosen option
        menu_name, menu = self.__menus[choice_int - 1]

        # Start the chosen menu
        menu.run()