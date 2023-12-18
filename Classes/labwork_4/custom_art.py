from colorama import Style

from Classes.labwork_4 import fonts
from Shared.Save.ask_save import AskSave
from Shared.Save.file_save import FileSaver
from Shared.Validate.validate import Validate
from Shared.Choice.colors import ColorChooser


class CustomArt:
    """
    A class that represents custom ASCII art.

    Attributes:
        _alignment (str): The alignment of the ASCII art ('left', 'right', 'center').
        _width (int): The width of the ASCII art.
        _font (dict): The font used for the ASCII art.
        _character (str): The character used to replace non-space characters in the ASCII art.
        valid (Validate): An instance of the Validate class.
        color_chooser (ColorChooser): An instance of the ColorChooser class.
        _color (str): The color code used for printing the ASCII art.
        _file_save (FileSaver): An instance of the FileSaver class.
        _ask_save (AskSave): An instance of the AskSave class.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the CustomArt class.

        Args:
            **kwargs: Additional keyword arguments.
                alignment (str): The alignment of the ASCII art ('left', 'right', 'center').
                width (int): The width of the ASCII art.
                character (str): The character used to replace non-space characters in the ASCII art.
                color (str): The color code used for printing the ASCII art.
        """
        self._alignment = kwargs.get('alignment', 'center')
        self._width = kwargs.get('width', 100)
        self._font = fonts.banner
        self._character = kwargs.get('character', '!')
        self.valid = Validate()
        self.color_chooser = ColorChooser()
        self._color = kwargs.get('color', '2')
        self._file_save = FileSaver("Data/labwork_4")
        self._ask_save = AskSave()

    def create_all(self, direction_message, alignment=None, width=None, character=None):
        """
        Creates the complete ASCII art with the specified direction message, alignment, width, and character.

        Args:
            direction_message (str): The direction message for the ASCII art.
            alignment (str, optional): The alignment of the ASCII art ('left', 'right', 'center').
            width (int, optional): The width of the ASCII art.
            character (str, optional): The character used to replace non-space characters in the ASCII art.

        Returns:
            str: The complete ASCII art.
        """
        width = width or self._width
        alignment = alignment or self._alignment
        character = character or self._character

        art_with_width = self._create_width(direction_message, width)
        art_with_alignment = self._create_alignment(art_with_width, width, alignment)
        art_with_character = self._create_character(art_with_alignment, character)
        return art_with_character

    def _create_width(self, direction_message, max_width):
        """
        Creates the ASCII art with the specified direction message and maximum width.

        Args:
            direction_message (str): The direction message for the ASCII art.
            max_width (int): The maximum width of the ASCII art.

        Returns:
            str: The ASCII art with the specified width.
        """
        max_lines = max(len(self._font.get(letter, '').split('\n')) for letter in direction_message)
        alignment_func = str.center

        line = [""] * max_lines
        line_width = 0
        art = []

        for word in direction_message:
            letter_lines = self._font.get(word, '').split('\n')
            word_width = len(letter_lines[0]) + 1

            if line_width + word_width <= max_width:
                for i in range(max_lines):
                    line[i] += alignment_func(letter_lines[i], word_width)
                line_width += word_width
            else:
                art.append('\n'.join(line))
                line = [""] * max_lines
                for i in range(max_lines):
                    line[i] += alignment_func(letter_lines[i], word_width)
                line_width = word_width

        art.append('\n'.join(line))
        output = '\n'.join(art)
        return output

    def _create_alignment(self, direction_message, width, alignment):
        """
        Creates the ASCII art with the specified alignment.

        Args:
            direction_message (str): The direction message for the ASCII art.
            width (int): The width of the ASCII art.
            alignment (str): The alignment of the ASCII art ('left', 'right', 'center').

        Returns:
            str: The ASCII art with the specified alignment.
        """
        output_lines = direction_message.split('\n')
        aligned_output_lines = []

        for line in output_lines:
            if alignment == "left":
                aligned_line = f"{' '}{line}"
            elif alignment == "right":
                aligned_line = f"{line.rjust(width)}"
            elif alignment == "center":
                aligned_line = f"{line.center(width)}"
            else:
                aligned_line = line

            aligned_output_lines.append(aligned_line)

        aligned_output = '\n'.join(aligned_output_lines)

        return aligned_output

    def _create_character(self, direction_message, character):
        """
        Creates the ASCII art with the specified character.

        Args:
            direction_message (str): The direction message for the ASCII art.
            character (str): The character used to replace non-space characters in the ASCII art.

        Returns:
            str: The ASCII art with the specified character.
        """
        lines = direction_message.split('\n')

        for i in range(len(lines)):
            line = lines[i]
            new_line = ''
            for char in line:
                if char != ' ':
                    new_line += character
                else:
                    new_line += ' '
            lines[i] = new_line

        modified_ascii_art = '\n'.join(lines)

        return modified_ascii_art

    def print_ascii_art(self, ready_art, user_color):
        """
        Prints the ASCII art with the specified color.

        Args:
            ready_art (str): The ASCII art to be printed.
            user_color (str): The color code used for printing the ASCII art.
        """
        print(f"Preview: \n" + user_color + ready_art + Style.RESET_ALL)

        self._ask_save.ask_save(self._file_save, ready_art)