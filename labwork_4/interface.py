from colorama import Style, Fore

from labwork_4 import variables
from labwork_4.errors import Error
from labwork_4.functions import Function
from labwork_4.modifiedArt import CustomArt


class Interface(Function):
    def __init__(self):
        super().__init__()
        self.error = Error()
        self.art = CustomArt()

    def save_to_file(self, file_name, user_word_modify):
        file_name = f"{file_name}.txt"

        with open(file_name, "w") as file:
            file.write(user_word_modify)

    def get_input_width(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return int(value)
            print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

    def get_input_color(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return value
            print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

    def _choice(self, choice):
        if choice.lower() != variables.choice_yes:
            return True

    def user_input(self):
        while True:
            user_word = input(variables.user_word_input)
            user_alignment = input(variables.user_alignment_input)
            user_character = input(variables.user_character_input)
            user_color = self.get_input_color(variables.user_color_input, self.error.check_color, variables.error_color)
            user_width = self.get_input_width(variables.width_input, self.error.check_widht, variables.error_width)

            ready_art = self.art.create_all(user_word, user_width, user_alignment, user_character)
            print(f"Preview: \n" + self._choose_color(user_color) + ready_art + Style.RESET_ALL)

            change_selection = input(variables.ask_change_art)
            if self._choice(change_selection):
                name_file = input(variables.file_name)
                self.save_to_file(name_file, ready_art)
            else:
                continue

            choose_exit = input(variables.choose_exit)
            if self._choice(choose_exit):
                break