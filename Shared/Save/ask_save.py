from Shared.Validate.validate import Validate
from logger import logging


class AskSave:
    """
    Class that handles asking the user if they want to save data and saving it if requested.

    Attributes:
        _valid (Validate): An instance of the Validate class for input validation.
        _ask_save (str): The prompt to ask the user if they want to save the data.
        _file_name (str): The prompt to ask the user for the file name.

    Methods:
        ask_save(dictionary, data_to_save): Asks the user if they want to save the data and saves it if requested.
    """

    def __init__(self):
        self._valid = Validate()
        self._ask_save = "Do you want save the art? (Yes/No): "
        self._file_name = "Please enter file name: "

    def ask_save(self, dictionary, data_to_save):
        """
        Asks the user if they want to save the data and saves it if requested.

        Args:
            dictionary (Dictionary): The dictionary object to save the data from.
            data_to_save (str): The data to be saved.

        Returns:
            bool: True if the data was saved, False otherwise.
        """
        logging.info(f"User use: ask_save")
        change_selection = self._valid.get_input(self._ask_save)
        if change_selection == 'yes':
            name_file = self._valid.get_input(self._file_name)
            dictionary.save_to_txt(name_file, data_to_save)
            logging.info(f"User save file")
            return True
