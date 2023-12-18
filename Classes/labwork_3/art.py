"""
This module contains the Art class which is used to create ASCII art.
"""

import pyfiglet
from colorama import Style
from Shared.Choice.colors import ColorChooser
from Shared.Save.ask_save import AskSave
from Shared.Validate.validate import Validate
from Shared.Save.file_save import FileSaver


class Art:
    """
    The Art class is used to create ASCII art with various options such as text, font,
    width, character, and color. It also includes methods for choosing a font
    and creating ASCII art.
    """

    def __init__(self, **kwargs):
        """
        The constructor for the Art class.

        Args:
            text (str, optional): The text to be used for the ASCII art. Defaults to ''.
            font (str, optional): The font to be used for the ASCII art. Defaults to 'banner'.
            width (int, optional): The width of the ASCII art. Defaults to 100.
            character (str, optional): The character to be used for the ASCII art. Defaults to '#'.
            color (str, optional): The color of the ASCII art. Defaults to '2'.
        """
        self.text = kwargs.get('text', '')
        self.font = kwargs.get('font', 'banner')
        self._width = kwargs.get('width', 100)
        self.character = kwargs.get('character', '#')
        self.valid = Validate()
        self.color_chooser = ColorChooser()
        self.color = kwargs.get('color', '2')
        self._file_save = FileSaver("Data/labwork_3")
        self._ask_save = AskSave()

    def choose_font(self, user_font):
        """
        This function is used to choose a font for the ASCII art.

        Args:
            user_font (str): The font to be used for the ASCII art.

        Returns:
            str: The font to be used for the ASCII art.

        Raises:
            ValueError: If the font is not valid.

        """
        font_names = ["5lineoblique", "banner", "slant", "doom", "cyberlarge", "big"]
        if user_font in font_names:
            return user_font
        return self.font

    def _create_ascii_art(self):
        """
        This function creates the ASCII art based on the input parameters.

        Args:
            self: The instance of the Art class.

        Returns:
            str: The ASCII art generated based on the input parameters.

        """
        ascii_art = pyfiglet.figlet_format(self.text,
                                        font=self.font, width=self._width)

        lines = ascii_art.split('\n')
        modified_lines = [self._modify_line(line) for line in lines]

        return '\n'.join(modified_lines)

    def _modify_line(self, line):
        """
        This function modifies a line of ASCII art by replacing all characters that are not
        spaces with the specified character.

        Args:
            line (str): The line of ASCII art to be modified.

        Returns:
            str: The modified line of ASCII art.

        """
        new_line = ""
        for char in line:
            if char != " ":
                new_line += self.character
            else:
                new_line += " "
        return new_line

    def _scale_ascii_art_height(self, art: str, height_scale: int) -> str:
        """
        This function scales the height of an ASCII art by repeating
        each line the specified number of times.

        Args:
            art (str): The ASCII art to be scaled.
            height_scale (int): The number of times each line should be repeated.

        Returns:
            str: The scaled ASCII art.
        """
        lines = art.split('\n')
        scaled_lines = [line for line in lines for _ in range(height_scale)]

        return '\n'.join(scaled_lines)

    def print_ascii_art(self, user_word, user_choice, user_font,
                        user_color, user_width, user_height):
        """
        This function is used to print the ASCII art based on the input parameters.

        Args:
            user_word (str): The word to be used for the ASCII art.
            user_choice (str): The choice of the user, either 'custom' or 'default'.
            user_font (str): The font to be used for the ASCII art.
            user_color (str): The color of the ASCII art.
            user_width (int): The width of the ASCII art.
            user_height (int): The height of the ASCII art.

        Returns:
            None

        Raises:
            ValueError: If the input parameters are not valid.

        """
        # if user_choice not in ['custom', 'default']:
        #     raise ValueError(f"Invalid choice: {user_choice}. "
        #                     f"Valid choices are 'custom' and 'default'.")

        if user_choice == 'custom':
            self._width = user_width
            user_word_modify = self._create_ascii_art()
        else:
            user_word_modify = pyfiglet.figlet_format(user_word, font=user_font, width=user_width)
        user_word_modify = self._scale_ascii_art_height(user_word_modify, user_height)

        print(f"Preview:\n{user_color}{user_word_modify}{Style.RESET_ALL}")

        self._ask_save.ask_save(self._file_save, user_word_modify)
