from Classes.labwork_3.art import Art
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class ArtMenu(Menu):
    """
    Represents a menu for generating ASCII art.

    Attributes:
        _art (Art): An instance of the Art class for generating ASCII art.
        _run_again (RunAgain): An instance of the RunAgain class for determining if the menu should run again.
        _config (dict): A dictionary containing configuration settings for the menu.

    Methods:
        run(): Runs the menu and generates ASCII art based on user input.
        _get_user_input(prompt, valid_input=None, type_=str): Gets user input with optional validation.

    """

    def __init__(self):
        super().__init__()
        self._art = Art()
        self._run_again = RunAgain()
        self._config = self._config['labwork_3']

    def run(self):
        """
        Runs the menu and generates ASCII art based on user input.
        """
        while True:
            user_word = self._get_user_input(self._config["user_word_input"])
            user_choice = self._get_user_input(self._config["user_choice_input"])
            user_font = self._art.font  # set default value

            if user_choice == 'custom':
                user_character = self._get_user_input(self._config["user_character_input"])
                self._art.character = user_character
                self._art.text = user_word
            else:
                user_font = self._get_user_input(self._config["user_font_input"],
                                                 valid_input=["1", "2", "3", "4", "5", "6"])
                user_font = self._art.choose_font(user_font)

            self._art.color_chooser.display_color_menu()
            user_color = self._get_user_input(self._config["user_color_input"],
                                              valid_input=self._art.color_chooser.color_map)
            user_color = self._art.color_chooser.choose_color(user_color)
            user_width = self._get_user_input(self._config["width_input"], type_=int)
            user_height = self._get_user_input(self._config["height_input"], type_=int)
            self._art.print_ascii_art(user_word, user_choice, user_font, user_color, user_width, user_height)
            if self._run_again.get_choice():
                break

    def _get_user_input(self, prompt, valid_input=None, type_=None):
        """
        Gets user input with optional validation.

        Args:
            prompt (str): The prompt to display to the user.
            valid_input (list, optional): A list of valid input values. Defaults to None.
            type_ (type, optional): The type to convert the user input to. Defaults to str.

        Returns:
            The user input converted to the specified type, if valid.

        """
        while True:
            user_input = self._art.valid.get_input(prompt, type_=type_)
            if valid_input is None or user_input in valid_input:
                return user_input
            else:
                print("Invalid input. Please try again.")
