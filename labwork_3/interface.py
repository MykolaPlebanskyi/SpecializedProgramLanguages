import pyfiglet
from colorama import Style, Fore

from labwork_3 import variables
from labwork_3.art import Art
from labwork_3.errors import Error
from labwork_3.functions import Function


class Interface(Function, Art):

    def save_to_file(self, file_name, user_word_modify):
        file_name = f"{file_name}.txt"

        with open(file_name, "w") as file:
            file.write(user_word_modify)

    def get_input_size(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return int(value)
            print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

    def get_input_settings(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return value
            print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

    def _choice(self, choice):
        if choice.lower() != 'yes':
            return True

    def user_input(self):
        while True:
            error = Error()
            user_word = input(variables.user_word_input)
            user_choice = input(variables.user_choice_input)
            if user_choice == 'custom':
                user_character = input(variables.user_character_input)
            else:
                user_font = self.get_input_settings(variables.user_font_input, error.check_font, variables.error_font)

            user_color = self.get_input_settings(variables.user_color_input, error.check_color, variables.error_color)

            user_width = self.get_input_size(variables.width_input, error.check_widht, variables.error_width)

            user_height = self.get_input_size(variables.height_input, error.check_height, variables.error_height)

            if user_choice == 'custom':
                user_word_modify = self._create_ascii_art(user_word, width=user_width, character=user_character)
            else:
                user_word_modify = pyfiglet.figlet_format(user_word, font=self._choose_font(user_font), justify="center",
                                                          width=user_width)

            user_word_modify = self._scale_ascii_art_height(user_word_modify, user_height)

            print(f"Preview:\n{self._choose_color(user_color)}{user_word_modify}{Style.RESET_ALL}")

            change_selection = input(variables.ask_change_art)
            if self._choice(change_selection):
                name_file = input(variables.file_name)
                self.save_to_file(name_file, user_word_modify)
            else:
                continue

            choose_exit = input(variables.choose_exit)
            if self._choice(choose_exit):
                break
