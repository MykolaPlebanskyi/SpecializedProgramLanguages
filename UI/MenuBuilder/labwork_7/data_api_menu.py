from Classes.labwork_7.data_api import DataDisplay
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class DataAPIMenu(Menu):
    """
    Represents a menu for interacting with a data API.

    Attributes:
        data_api (DataDisplay): An instance of the DataDisplay class.
        run_again (RunAgain): An instance of the RunAgain class.
        _config (dict): Configuration settings for the menu.

    Methods:
        run(): Runs the menu loop.
        display_menu(): Displays the menu options.
    """

    def __init__(self):
        super().__init__()
        self.data_api = DataDisplay()
        self.run_again = RunAgain()
        self._config = self._config['labwork_7']

    def run(self):
        """
        Runs the menu loop.

        The menu loop allows the user to interact with the menu options. It continuously displays the menu and prompts the user for input. Based on the user's input, the program will perform the corresponding action.

        The menu loop will continue until the user chooses to exit the program.

        Returns:
            None
        """
        while True:
            self.display_menu()
            menu_input = self.data_api.valid.get_input(self._config["menu_input"], str)
            if menu_input == "1":
                # If the user selects option 1, perform an API request
                url_choice = self.data_api.valid.get_input(self._config["url_choice"], int)
                url_choice = self.data_api.url_choice(url_choice)
                url = url_choice
                url_choice = self.data_api.check_api_data(url_choice)

                method = self.data_api.choose_method(
                    self.data_api.valid.get_input(self._config["method_input"], int))
                self.data_api.color_chooser.display_color_menu()
                user_color = self.data_api.valid.get_input(self._config["user_color_input"],
                                                        valid_input=self.data_api.color_chooser.color_map)
                user_color = self.data_api.color_chooser.choose_color(user_color)
                data = self.data_api.display_data(url, url_choice, user_color, method)
                self.data_api.add_to_request_history(url)
                change_selection = self.data_api.valid.get_input(self._config["ask_save_to_file"], str)
                if change_selection == 'yes':
                    # If the user selects "yes" to saving the data to a file, prompt for the file name and format
                    name_file = self.data_api.valid.get_input(self._config["file_name"], str)
                    format_file = self.data_api.choose_format(self.data_api.valid.get_input(self._config["format_input"]))
                    self.data_api.save_to_file(name_file, data, format_file)
                if self.run_again.get_choice():
                    # If the user selects to run the menu again, break out of the loop
                    break
            elif menu_input == '2':
                # If the user selects option 2, show the request history
                self.data_api.show_request_history()
            else:
                # If the user selects anything else, exit the program
                break
                # break

    def display_menu(self):
        """
        Displays the main menu for the data API.

        The menu consists of three options:

        1. Do API request: Allows the user to make an API request.
        2. Show history: Shows the request history.
        3. Exit: Exits the program.

        This function prompts the user for input and performs the corresponding action based on the user's input.
        """
        print("What you want? \n1. Do API request\n2. Show history\n3. Exit\n")


