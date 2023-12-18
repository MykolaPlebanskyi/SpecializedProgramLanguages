from Classes.labwork_4.custom_art import CustomArt
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class CustomArtMenu(Menu):
    """
    A menu class for creating and printing custom ASCII art.

    Attributes:
        custom_art (CustomArt): An instance of the CustomArt class.
        run_again (RunAgain): An instance of the RunAgain class.
        _config (dict): A dictionary containing configuration settings.

    Methods:
        run(): Runs the custom art menu.
    """
    def __init__(self):
        super().__init__()
        self.custom_art = CustomArt()
        self.run_again = RunAgain()
        self._config = self._config['labwork_4']

    def run(self):
        """
        Runs the custom art menu.

        The menu will loop until the user chooses to exit. At each iteration, the user will be prompted to enter
        values for various parameters, such as the word to be used in the art, the alignment of the text, the
        character set to be used, the background and font colors, and the width of the art. The menu will then
        create the art using these parameters and print it to the screen.

        If the user chooses to run the menu again, the loop will repeat.

        Args:
            None

        Returns:
            None
        """
        while True:
            # Get user input for various parameters
            user_word = self.custom_art.valid.get_input(self._config["user_word_input"])
            user_alignment = self.custom_art.valid.get_input(self._config["user_alignment_input"])
            user_character = self.custom_art.valid.get_input(self._config["user_character_input"])

            # Display background color menu
            self.custom_art.color_chooser.display_back_color_menu()

            # Get user input for background color
            user_color = self.custom_art.valid.get_input(self._config["user_color_input"],
                                                        valid_input=self.custom_art.color_chooser.back_and_font_color_map)

            # Choose background and font colors based on user input
            user_color = self.custom_art.color_chooser.choose_back_and_font_color(user_color)

            # Get user input for width
            user_width = self.custom_art.valid.get_input(self._config["width_input"], int)

            # Create the art using the input parameters
            ready_art = self.custom_art.create_all(user_word, user_alignment, user_width, user_character)

            # Print the art to the screen
            self.custom_art.print_ascii_art(ready_art, user_color)

            # Prompt the user to run the menu again
            if self.run_again.get_choice():
                # If the user chooses to run the menu again, repeat the loop
                break
