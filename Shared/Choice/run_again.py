from Shared.Validate.validate import Validate
from logger import logging

class RunAgain:
    def __init__(self):
        self._valid = Validate()
        self.run_again = "Do you want to run the program again? (yes/no): "

    def get_choice(self):
        """
        Get user choice.

        Returns:
            bool: True if the user wants to run the program again, False otherwise.
        """
        logging.info(f"User run again program")

        return self._valid.get_input(self.run_again, str).lower() != 'yes'
