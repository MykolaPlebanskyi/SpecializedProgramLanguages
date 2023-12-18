from typing import Any, Iterable
from logger import logging


class Validate:

    def get_input(self, prompt: str, type_: type = None, valid_input: Iterable = None) -> Any:
        """
        A function that prompts the user for input and ensures that the input is of the correct type and within a specified set of valid options.

        Parameters:
        prompt (str): The prompt to display to the user.
        type_ (type, optional): The type of input to expect. If not specified, the input will not be type-checked.
        valid_input (Iterable, optional): A collection of valid input options. If the input is not within this collection, the user will be prompted to enter a valid option.

        Returns:
        Any: The input value.

        Raises:
        ValueError: If the input is not of the correct type and valid_input is not specified or the input is not within the valid_input collection.
        """
        while True:
            logging.info(f"User validate input")
            value = input(prompt)
            if type_:
                try:
                    value = type_(value)
                except ValueError:
                    logging.error("User have invalid input")
                    print(f"Invalid input. Please enter a {type_.__name__} value.")
                    continue
            if valid_input and value not in valid_input:
                logging.error("User have invalid input")
                print(f"Invalid input. Please enter one of the following: {', '.join(map(str, valid_input))}")
                continue
            return value
