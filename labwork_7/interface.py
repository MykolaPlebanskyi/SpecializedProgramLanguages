from colorama import Fore, Style
import requests

from labwork_7.data_display import DataDisplay
from labwork_7.errors import Error
from labwork_7 import variables


class Interface:
    def __init__(self):
        self.error = Error()
        self.user_requests = []
        self.api_data = DataDisplay()

    def _choose_color(self, user_color):
        if user_color == '1':
            return Fore.BLACK
        elif user_color == '2':
            return Fore.RED
        elif user_color == '3':
            return Fore.GREEN
        elif user_color == '4':
            return Fore.YELLOW
        elif user_color == '5':
            return Fore.BLUE
        elif user_color == '6':
            return Fore.WHITE
        elif user_color == '7':
            return Fore.CYAN
        elif user_color == '8':
            return Fore.MAGENTA

    def _choose_method(self, method):
        if method == '1':
            return 'table'
        else:
            return 'list'

    def _choose_format(self, format):
        if format == '1':
            return 'txt'
        elif format == '2':
            return 'json'
        else:
            return 'csv'

    def user_input(self):
        while True:
            # url = "https://jsonplaceholder.org/users"
            # url = "https://jsonplaceholder.org/posts"
            # url = "https://jsonplaceholder.org/comments"
            menu_input = input(variables.menu_input)
            if menu_input == "1":
                url, url_good = self.get_input_api(self.error.check_api_data, variables.error_url)
                method = self._choose_method(self.get_input_settings(variables.method_input, self.error.check_method,
                                                                     variables.error_method))
                color = self._choose_color(self.get_input_settings(variables.color_input, self.error.check_color,
                                                                   variables.error_color))
                data = self.display_data(url, url_good, color, method)
                self.add_to_request_history(url)
                change_selection = input(variables.ask_save_to_file)
                if self._choice(change_selection):
                    name_file = input(variables.file_name)
                    format = self._choose_format(self.get_input_settings(variables.format_input, self.error.check_fomat,
                                                                         variables.error_method))
                    self.save_to_file(name_file, data, format)
            elif menu_input == '2':
                self.show_request_history()
            else:
                break

    def display_data(self, url, url_data, color, method="list"):
        print(f"Data displayed as a {method}:")
        if url.endswith("users"):
            if method == "table":
                data = self.api_data.display_data_as_table(url_data, color, 1)
            else:
                data = self.api_data.display_data_as_list(url_data, color, 1)
        else:
            if method == "table":
                data = self.api_data.display_data_as_table(url_data, color, 2)
            else:
                data = self.api_data.display_data_as_list(url_data, color, 2)
        print(data)
        return data

    def show_request_history(self):
        if not self.user_requests:
            print(f"{Fore.RED + Style.BRIGHT}{variables.empty_history}{Style.RESET_ALL}")
        else:
            print(f"{variables.history}")
            for index, request in enumerate(self.user_requests, start=1):
                print(f"{index}. {request}")

    def add_to_request_history(self, url):
        return self.user_requests.append(url)

    def save_to_file(self, file_name, data, format):
        file_name = f"{file_name}.{format}"

        cleaned_text = self.api_data.remove_color_tags(data)

        with open(file_name, "w") as file:
            file.write(cleaned_text)

    def get_input_settings(self, number, error_check, error_message):
        while True:
            value = input(number)
            if not error_check(value):
                return value
            print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

    def get_input_api(self, error_check, error_message):
        while True:
            try:
                url = input(variables.url_input)
                if error_check(url):
                    data = requests.get(url)
                    data = data.json()
                    return url, data
            except requests.HTTPError as e:
                print(Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL)

    def _choice(self, choice):
        if choice.lower() in [variables.choice_yes, variables.choice_y]:
            return True