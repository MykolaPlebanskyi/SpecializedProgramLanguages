import re

from colorama import Fore, Back

from Shared.Choice.colors import ColorChooser
from Shared.Save.ask_save import AskSave
from Shared.Save.file_save import FileSaver
from Shared.Validate.validate import Validate


class Parallelepiped:
    """
    A class representing a parallelepiped.

    Attributes:
    - width: The width of the parallelepiped.
    - height: The height of the parallelepiped.
    - length: The length of the parallelepiped.
    - oblique: The character used to represent the oblique lines in the parallelepiped.
    - top: The character used to represent the top line of the parallelepiped.
    - column: The character used to represent the column lines in the parallelepiped.
    - transform: The character used to represent the line break in the parallelepiped.
    - space_count: The number of spaces used in the parallelepiped.
    - increment_count: The increment count used in the parallelepiped.
    - color_chooser: An instance of the ColorChooser class used for choosing colors.
    - valid: An instance of the Validate class used for validation.
    - default_colors: A dictionary containing the default colors for the parallelepiped.
    - gap: The character used to represent the gap in the parallelepiped.
    - line: The character used to represent the line in the parallelepiped.
    """

    def __init__(self, width=None, height=None, length=None):
        self._file_save = FileSaver("Data/labwork_5")
        self._ask_save = AskSave()
        self.width = width if width is not None else 10
        self.height = height if height is not None else 10
        self.save_height = self.height
        self.length = length if length is not None else 15
        self.oblique = '\\'
        self.top = '+'
        self.column = '|'
        self.transform = '\n'
        self.space_count = 0
        self.increment_count = 1
        self.color_chooser = ColorChooser()
        self.valid = Validate()

        self.default_colors = {
            'color1': '4',
            'color2': '5',
            'color3': '3',
            'color4': '6'
        }
        self.gap = ' '
        self.line = '—'

    def custom_background_color(self, text: str, color: str) -> str:
        """
        This function takes in a text and a color and returns the text with the background color of the given color.

        Args:
            text (str): The text that you want to have a background color.
            color (str): The color that you want the background to be.

        Returns:
            str: The text with the background color of the given color.

        Raises:
            ValueError: If the color is not valid.
        """

        # Choose the background color
        return self.color_chooser.choose_back_color(color) + text + Fore.RESET + Back.RESET

    def display_parallelepiped(self, number, colors=None):
        """
        This function generates and displays a parallelepiped based on the given parameters.

        Args:
            number (int): The number of the parallelepiped.
            colors (dict, optional): A dictionary containing the colors for the parallelepiped.

        Returns:
            str: The generated parallelepiped.

        Raises:
            ValueError: If the number is not valid.
        """

        # Choose the colors for the parallelepiped
        colors = colors if colors else self.default_colors

        # Generate the parallelepiped based on the given number
        if number == 1:
            art = self.generate_layer(
                self.custom_background_color(' ', colors['color1']),
                self.custom_background_color(' ', colors['color2']),
                self.custom_background_color(' ', colors['color3']),
                self.custom_background_color(' ', colors['color4']),
                gap=self.gap,
                line=self.line
            )
        else:
            art = self.generate_layer(
                self.custom_background_color('  ', colors['color1']),
                self.custom_background_color('  ', colors['color2']),
                self.custom_background_color('  ', colors['color3']),
                self.custom_background_color('  ', colors['color4']),
                gap='  ',
                line='——'
            )

        return art

    def display_parallelepiped_without_zoom(self, user_parallelepiped, colors=None):
        user_parallelepiped = user_parallelepiped.display_parallelepiped(number=1, colors=colors)
        print(user_parallelepiped)
        return user_parallelepiped

    def display_parallelepiped_with_zoom(self, user_parallelepiped, colors=None):
        user_parallelepiped = user_parallelepiped.display_parallelepiped(number=2, colors=colors)
        print(user_parallelepiped)
        return user_parallelepiped

    def generate_layer(self, color1, color2, color3, color4, gap, line):
        """
        This function generates the layer of the parallelepiped.

        Args:
            color1 (str): The color of the top and bottom lines.
            color2 (str): The color of the middle lines.
            color3 (str): The color of the left and right columns.
            color4 (str): The color of the shadow.
            gap (str): The gap between the lines.
            line (str): The line of the parallelepiped.

        Returns:
            str: The generated layer of the parallelepiped.
        """
        shadow = color4 * self.save_height
        art = self.save_height * gap + self.top + line * (self.width - 2) + self.top + self.transform
        for i in range(self.length - 4, 0, -1):
            if self.height > 2:
                art = self._generate_multi_height_layer(color1, color2, gap, art)
            if self.height == 2:
                art = self._generate_two_height_layer(color1, color2, shadow, art)
            if self.height == 1:
                art = self._generate_one_height_layer(color1, color2, gap, shadow, art)
            if i == 1:
                art = self._generate_final_layer(color1, color3, color4, gap, line, shadow, art)
        return art

    def _generate_multi_height_layer(self, color1: str, color2: str, gap: str, art: str) -> str:
        """
        This function generates the layer of the parallelepiped with multiple heights.

        Args:
            color1 (str): The color of the top and bottom lines.
            color2 (str): The color of the middle lines.
            gap (str): The gap between the lines.
            art (str): The generated art so far.

        Returns:
            str: The updated art with the generated layer of the parallelepiped.
        """
        art += self.save_height * gap + self.column + color1 * self.space_count + self.oblique + (
                color2 * (self.width - 2)) + self.oblique + self.transform
        self.reduction_height_and_magnification_count()
        return art

    def _generate_two_height_layer(self, color1: str, color2: str, shadow: str, art: str) -> str:
        """
        This function generates the layer of the parallelepiped with two heights.

        Args:
            color1 (str): The color of the top and bottom lines.
            color2 (str): The color of the middle lines.
            shadow (str): The color of the shadow.
            art (str): The generated art so far.

        Returns:
            str: The updated art with the generated layer of the parallelepiped.
        """
        art += shadow + self.top + self.space_count * color1 + self.oblique + (
                color2 * (self.width - 2)) + self.oblique + self.transform
        self.reduction_height_and_magnification_count()
        return art

    def _generate_one_height_layer(self, color1: str, color2: str, gap: str, shadow: str, art: str) -> str:
        """
        This function generates the layer of the parallelepiped with one height.

        Args:
            color1 (str): The color of the top and bottom lines.
            color2 (str): The color of the middle lines.
            gap (str): The gap between the lines.
            shadow (str): The color of the shadow.
            art (str): The generated art so far.

        Returns:
            str: The updated art with the generated layer of the parallelepiped.
        """
        art += gap * self.increment_count + shadow + self.oblique + (self.space_count - 1) * color1 + self.oblique + (
                color2 * (self.width - 2)) + self.oblique + self.transform
        self.update_increment()
        return art

    def _generate_final_layer(self, color1: str, color3: str, color4: str, gap: str, line: str, shadow: str, art: str) -> str:
        """
        This function generates the final layer of the parallelepiped.

        Args:
            color1 (str): The color of the top and bottom lines.
            color3 (str): The color of the left and right columns.
            color4 (str): The color of the shadow.
            gap (str): The gap between the lines.
            line (str): The line of the parallelepiped.
            shadow (str): The color of the shadow.
            art (str): The generated art so far.

        Returns:
            str: The updated art with the generated final layer of the parallelepiped.
        """
        # Add the final layer of the parallelepiped
        art += gap * self.increment_count + shadow + self.oblique + (self.space_count - 1) * color1 + self.top + (
            line * (self.width - 2)) + self.top + self.transform
        self.update_increment()

        # Loop through each layer of the final layer
        for i in range(self.space_count, 0, -1):
            # Add the layer of the final layer
            art += (gap * self.increment_count + shadow + self.oblique + color1 * (self.space_count - 2) +
                    self.column + color3 * (self.width - 2) + self.column + self.transform)
            self.reduction_count_and__height()
            self.update_increment()

            # Check if the current layer is the final layer
            if self.space_count == 1:
                # Add the final layer of the parallelepiped
                art += (gap * self.increment_count + color4 * self.save_height + self.top + line *
                        (self.width - 2) + self.top + self.transform)
                break

        return art

    def reduction_height_and_magnification_count(self):
        """ 
        This function reduces the height of the parallelepiped and increases the magnification count.

        Parameters:
        - self: The instance of the Parallelepiped class.

        Returns:
        - None.

        Raises:
        - ValueError: If the height is less than or equal to 1.
        """

        # Reduce the height of the parallelepiped
        self.height -= 1

        # Increase the magnification count
        self.space_count += 1

    def update_increment(self):
        """
        This function increases the increment count by 1.

        Parameters:
        - self: The instance of the Parallelepiped class.

        Returns:
        - None.
        """
        self.increment_count += 1

    def reduction_count_and__height(self):
        """
        This function reduces the height of the parallelepiped and decreases the magnification count.

        Parameters:
        - self: The instance of the Parallelepiped class.

        Returns:
        - None.

        Raises:
        - ValueError: If the height is less than or equal to 1.
        """

        # Reduce the height of the parallelepiped
        self.height -= 1

        # Decrease the magnification count
        self.space_count -= 1

    def save_to_file(self, parallelepiped):
        """
        This function saves the given parallelepiped to a file.

        Parameters:
        - self: The instance of the Parallelepiped class.
        - parallelepiped (str): The parallelepiped that you want to save.

        Returns:
        - None.

        Raises:
        - ValueError: If the given parallelepiped is not a string.
        """

        # Remove the ANSI escape sequences from the given parallelepiped
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        ansi_escape = ansi_escape.sub('', parallelepiped)

        # Ask the user if they want to save the given parallelepiped to a file
        self._ask_save.ask_save(self._file_save, ansi_escape)