from logger import logging
from colorama import Fore, Back


class ColorChooser:
    """
    A class that provides methods for choosing colors and displaying color menus.

    Attributes:
        color_map (dict): A dictionary mapping user color choices to color codes.
        back_color_map (dict): A dictionary mapping user color choices to background color codes.
        back_and_font_color_map (dict): A dictionary mapping user color choices to combined font and background color codes.
    """

    def __init__(self):
        self.color_map = {
            '1': Fore.BLACK,
            '2': Fore.RED,
            '3': Fore.GREEN,
            '4': Fore.YELLOW,
            '5': Fore.BLUE,
            '6': Fore.WHITE,
            '7': Fore.CYAN,
            '8': Fore.MAGENTA
        }

        self.back_color_map = {
            '1': Back.BLACK,
            '2': Back.RED,
            '3': Back.GREEN,
            '4': Back.YELLOW,
            '5': Back.BLUE,
            '6': Back.WHITE,
            '7': Back.CYAN,
            '8': Back.MAGENTA
        }

        self.back_and_font_color_map = {
            '1': Fore.LIGHTBLACK_EX + Back.WHITE,
            '2': Fore.BLACK + Back.WHITE,
            '3': Fore.WHITE + Back.BLACK,
            '4': Fore.WHITE + Back.LIGHTBLACK_EX
        }

    def choose_color(self, user_color):
        """
        Choose a color based on the user's color choice.

        Args:
            user_color (str): The user's color choice.

        Returns:
            str: The color code corresponding to the user's color choice. If the user's color choice is not found, returns the default color code.
        """
        logging.info(f"User use: choose_color")
        return self.color_map.get(user_color, Fore.WHITE)

    def choose_back_and_font_color(self, user_color):
        """
        Choose a combined font and background color based on the user's color choice.

        Args:
            user_color (str): The user's color choice.

        Returns:
            str: The combined font and background color code corresponding to the user's color choice. If the user's color choice is not found, returns the default combined color code.
        """
        logging.info(f"User use: choose_back_and_font_color")
        return self.back_and_font_color_map.get(user_color, Fore.WHITE + Back.BLACK)

    def choose_back_color(self, user_color):
        """
        Choose a background color based on the user's color choice.

        Args:
            user_color (str): The user's color choice.

        Returns:
            str: The background color code corresponding to the user's color choice. If the user's color choice is not found, returns the default background color code.
        """
        logging.info(f"User use: choose_back_color")
        return self.back_color_map.get(user_color, Back.WHITE)

    def display_color_menu(self):
        """
        Display the color menu.

        Returns:
            str: The color menu as a string.
        """
        logging.info(f"User: choose_back_color")
        color_names = ['black', 'red', 'green', 'yellow', 'blue', 'white', 'cyan', 'magenta']
        menu = "Colors: \n"
        for i, color in enumerate(color_names, start=1):
            menu += f"{i}. '{color}'\n"
        print(menu)
        return menu

    def display_back_color_menu(self):
        """
        Display the background color menu.

        Returns:
            str: The background color menu as a string.
        """
        logging.info(f"User: def display_back_color_menu(self):")
        color_names = ['gray and white', 'black and white', 'white and black', 'white and gray']
        menu = "Colors: \n"
        for i, color in enumerate(color_names, start=1):
            menu += f"{i}. '{color}'\n"
        print(menu)
        return menu
