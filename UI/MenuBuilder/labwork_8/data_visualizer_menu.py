from Classes.labwork_7.data_api import DataDisplay
from Classes.labwork_8.data_visualizer import DataVisualizer
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class DataVisualizerMenu(Menu):
    def __init__(self):
        """
        Constructor for DataVisualizerMenu class.
        Initializes a new instance of the DataVisualizerMenu class.

        """
        self.data_visualizer = DataVisualizer()
        super().__init__()

    def run(self):
        """
        Runs the menu and performs operations based on user input.

        """
        # Explore the data
        self.data_visualizer.explore_data()

        # Display the menu
        while True:
            self.display_menu()
            user_choice = input("Your choice: ")

            if user_choice.lower() == "0":
                # Exit the menu
                break

            # Visualize the data based on the user's choice
            self.data_visualizer.visualize_data(user_choice)

    def display_menu(self):
        """
        Display the menu options.

        Parameters:
            None

        Returns:
            None

        """
        print("\nWhat you want? \n1. Scatter plot\n2. Histogram plot\n3. Bar plot\n4. Output all charts\n0. Exit\n")
