import re

from colorama import Fore, Style

from labwork_5 import variables
from labwork_5.errors import Error
from labwork_5.parallelepiped import Parallelepiped


class Interface:
    def __init__(self):
        self.error = Error()

    def _choice_exit(self, choice):
        if choice.lower() not in [variables.choice_yes, variables.choice_y]:
            return True

    def _choice(self, choice):
        if choice.lower() in [variables.choice_yes, variables.choice_y]:
            return True

    def user_input(self):
        while True:
            width, height, length = self.input_parameters()
            user_parallelepiped = Parallelepiped(width, height, length)
            print(variables.colors)
            colors = self.input_colors(user_parallelepiped)
            user_parallelepiped = user_parallelepiped.display_parallelepiped(number=1, colors=colors)
            print(user_parallelepiped)
            choose_zoom = input(variables.choose_zoom)
            if self._choice(choose_zoom):
                parallelepiped_zoom = Parallelepiped(width, height, length)
                user_parallelepiped = parallelepiped_zoom.display_parallelepiped(number=2, colors=colors)
                print(user_parallelepiped)
            change_selection = input(variables.ask_save_art)
            if self._choice(change_selection):
                name_file = input(variables.file_name)
                self.save_to_file(name_file, user_parallelepiped)
            choose_exit = input(variables.choose_exit)
            if self._choice_exit(choose_exit):
                break

    def input_parameters(self):
        width = self.get_valid_input(variables.user_width, self.error.check_width_and_height,
                                     variables.error_width_and_height)
        height = self.get_valid_input(variables.user_height, self.error.check_width_and_height,
                                      variables.error_width_and_height)
        length = self.get_valid_length(variables.user_length, height, self.error.check_length, variables.error_length)

        return width, height, length

    def get_valid_input(self, prompt, error_check, error_message):
        while True:
            value = input(prompt).strip()
            if not self.error.check_empty(value):
                return None
            if error_check(value):
                print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)
            else:
                return int(value)

    def get_valid_length(self, prompt, height, error_check, error_message):
        while True:
            length = input(prompt).strip()
            if not self.error.check_empty(length):
                return None
            if error_check(height, length):
                print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)
            else:
                return int(length)

    def input_colors(self, parallelepiped):
        custom_color1 = self.get_input_color(variables.color_left, self.is_valid_color,
                                             parallelepiped.default_colors['color1'])
        custom_color2 = self.get_input_color(variables.color_top, self.is_valid_color,
                                             parallelepiped.default_colors['color2'])
        custom_color3 = self.get_input_color(variables.color_front, self.is_valid_color,
                                             parallelepiped.default_colors['color3'])
        custom_color4 = self.get_input_color(variables.color_shadow, self.is_valid_color,
                                             parallelepiped.default_colors['color4'])

        parallelepiped_colors = {
            'color1': custom_color1,
            'color2': custom_color2,
            'color3': custom_color3,
            'color4': custom_color4
        }
        return parallelepiped_colors

    def is_valid_color(self, color):
        colors = {
            'black': '\033[40m',
            'red': '\033[41m',
            'green': '\033[42m',
            'yellow': '\033[43m',
            'blue': '\033[44m',
            'magenta': '\033[45m',
            'cyan': '\033[46m',
            'white': '\033[47m',
        }
        return color.lower() in colors

    def get_input_color(self, entered_value, error_check, default_value):
        while True:
            value = input(entered_value).strip().lower()
            if value in {'', ' ', None} or not error_check(value):
                return default_value
            return value

    def save_to_file(self, file_name, user_parallelepiped):
        file_name = f"{file_name}.txt"
        stripped_text = self.strip_ansi(user_parallelepiped)

        with open(file_name, "w") as file:
            file.write(stripped_text)

    def strip_ansi(self, text):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)
