from Shared.Validate.validate import Validate


class Test:
    """
    This class represents a test.

    Attributes:
        _valid (Validate): An instance of the Validate class.
        _choice (str): The prompt for user input.
    """

    def __init__(self):
        self._valid = Validate()
        self._choice = "Please choose what you want: "

    def get_input(self):
        """
        Get user input.

        Returns:
            str: The user input.
        """
        return self._valid.get_input(self._choice, str, valid_input=["1", "2", "3", "4", "5", "6"])
