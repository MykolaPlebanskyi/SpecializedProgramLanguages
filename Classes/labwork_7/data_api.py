import pandas as pd
import requests
from colorama import Style
from tabulate import tabulate

from Shared.Choice.colors import ColorChooser
from Shared.Save.file_save import FileSaver
from Shared.Validate.validate import Validate


class DataDisplay:
    """
    A class that provides methods for displaying and manipulating data.

    Attributes:
    - file_save (FileSaver): An instance of the FileSaver class for saving data to files.
    - color_chooser (ColorChooser): An instance of the ColorChooser class for choosing colors.
    - valid (Validate): An instance of the Validate class for data validation.
    - user_requests (list): A list to store user requests.
    - urls (dict): A dictionary that maps choices to URLs.

    Methods:
    - display_data_as_table: Displays data as a table.
    - columns_table: Formats the columns of a DataFrame for table display.
    - display_data_as_list: Displays data as a list.
    - columns_list: Formats the columns of a DataFrame for list display.
    - choose_method: Returns the display method based on the user's choice.
    - display_data: Displays data based on the URL and display method.
    - url_choice: Returns the URL based on the user's choice.
    - choose_format: Returns the file format based on the user's choice.
    - show_request_history: Displays the user's request history.
    - add_to_request_history: Adds a URL to the user's request history.
    - check_api_data: Checks the validity of the API data.
    - save_to_file: Saves data to a file.
    """
    def __init__(self):
        self.file_save = FileSaver("Data/labwork_7")
        self.color_chooser = ColorChooser()
        self.valid = Validate()
        self.user_requests = []
        self.urls = {
            '1': "https://jsonplaceholder.org/users",
            '2': "https://jsonplaceholder.org/posts",
            '3': "https://jsonplaceholder.org/comments"
        }

    def display_data_as_table(self, data, color, choose):
        """
        Displays data as a table.

        Args:
        - data: The data to be displayed.
        - color: The color to be applied to the table headers.
        - choose: The user's choice for data manipulation.

        Returns:
        - The formatted table as a string.
        """
        if data:
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', 20)
            df = pd.DataFrame(data)
            if choose == 1:
                df['login'] = df['login'].apply(lambda x: x['username'])
                df['address'] = df['address'].apply(lambda x: x['street'])
                df['company'] = df['company'].apply(lambda x: x['name'])

                return self.columns_table(df, color)
            if choose == 2:
                return self.columns_table(df, color)
        else:
            return "No data to display."

    def columns_table(self, df, color):
        """
        Formats the columns of a DataFrame for table display.

        Args:
        - df: The DataFrame to be formatted.
        - color: The color to be applied to the table headers.

        Returns:
        - The formatted table as a string.
        """
        colored_columns = [f"{color}{col}{Style.RESET_ALL}" for col in df.columns]
        df = df.map(lambda x: x if isinstance(x, float) or len(str(x)) <= 20 else str(x)[:20 - 3] + '...')
        return tabulate(df, headers=colored_columns, tablefmt='psql', showindex=False)

    def display_data_as_list(self, data, color, choose):
        """
        Displays data as a list.

        Args:
        - data: The data to be displayed.
        - color: The color to be applied to the list items.
        - choose: The user's choice for data manipulation.

        Returns:
        - The formatted list as a string.
        """
        if data:
            df = pd.DataFrame(data)

            if choose == 1:
                df['login'] = df['login'].apply(lambda x: x['username'])
                df['address'] = df['address'].apply(lambda x: x['street'])
                df['company'] = df['company'].apply(lambda x: x['name'])
                return self.columns_list(df, color)
            if choose == 2:
                for col in df.columns:
                    if df[col].dtype == 'object':
                        df[col] = df[col].astype(str).str.slice(0, 50)
                return self.columns_list(df, color)
        else:
            return "No data to display."

    def columns_list(self, df, color):
        """
        Formats the columns of a DataFrame for list display.

        Args:
        - df: The DataFrame to be formatted.
        - color: The color to be applied to the list items.

        Returns:
        - The formatted list as a string.
        """
        result = ""
        for index, row in df.iterrows():
            for col, value in row.items():
                result += f"{color}{col}{Style.RESET_ALL}: {value}\n"
            result += "\n"
        return result

    def choose_method(self, method):
        """
        Returns the display method based on the user's choice.

        Args:
        - method: The user's choice for the display method.

        Returns:
        - The display method as a string.
        """
        if method == 1:
            return 'table'
        else:
            return 'list'

    def display_data(self, url, url_data, color, method="list"):
        """
        Displays data based on the URL and display method.

        Args:
        - url: The URL of the data source.
        - url_data: The data retrieved from the URL.
        - color: The color to be applied to the display.
        - method: The display method (default: "list").

        Returns:
        - The formatted data as a string.
        """
        print(f"Data displayed as a {method}:")
        if url.endswith("users"):
            if method == "table":
                data = self.display_data_as_table(url_data, color, 1)
            else:
                data = self.display_data_as_list(url_data, color, 1)
        else:
            if method == "table":
                data = self.display_data_as_table(url_data, color, 2)
            else:
                data = self.display_data_as_list(url_data, color, 2)
        print(data)
        return data

    def url_choice(self, url_choice):
        """
        Returns the URL based on the user's choice.

        Args:
        - url_choice: The user's choice for the URL.

        Returns:
        - The URL as a string.
        """
        if url_choice == 1:
            return "https://jsonplaceholder.org/users"
        elif url_choice == 2:
            return "https://jsonplaceholder.org/posts"
        else:
            return "https://jsonplaceholder.org/comments"

    def choose_format(self, format):
        """
        Returns the file format based on the user's choice.

        Args:
        - format: The user's choice for the file format.

        Returns:
        - The file format as a string.
        """
        if format == '1':
            return 'txt'
        elif format == '2':
            return 'json'
        else:
            return 'csv'

    def show_request_history(self):
        """
        Displays the user's request history.
        """
        if not self.user_requests:
            print("\nThe request history is empty")
        else:
            print("\nUser Requests History:")
            for index, request in enumerate(self.user_requests, start=1):
                print(f"{index}. {request}")

    def add_to_request_history(self, url):
        """
        Adds a URL to the user's request history.

        Args:
        - url: The URL to be added.
        """
        return self.user_requests.append(url)

    def check_api_data(self, url):
        """
        Checks the validity of the API data.

        Args:
        - url: The URL of the API.

        Returns:
        - The JSON response as a dictionary.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise requests.HTTPError() from e

    def save_to_file(self, name_file, data, format_file):
        """
        Saves data to a file.

        Args:
        - name_file: The name of the file.
        - data: The data to be saved.
        - format_file: The format of the file.
        """
        self.file_save.save_to_file(name_file, data, format_file)