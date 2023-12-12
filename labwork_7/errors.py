import requests
from colorama import Fore, Style
from labwork_7 import variables


class Error:
    def check_api_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise requests.HTTPError() from e


    def check_color(self, number):
        try:
            number = int(number)
            if number < 1 or number > 8:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_method(self, number):
        try:
            number = int(number)
            if number < 1 or number > 2:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_fomat(self, number):
        try:
            number = int(number)
            if number < 1 or number > 3:
                raise ValueError
        except ValueError:
            return ValueError()
