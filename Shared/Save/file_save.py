import os
import re
from logger import logging


class FileSaver:
    """
    A class that provides methods to save files.

    Args:
        relative_directory (str): The relative directory where the files will be saved.

    Attributes:
        directory (str): The absolute directory path where the files will be saved.

    Methods:
        save_to_txt(file_name, content): Saves content to a text file.
        save_to_file(file_name, data, format): Saves data to a file in the specified format.
        remove_color_tags(text): Removes color tags from the given text.
    """

    def __init__(self, relative_directory):
        base_dir = os.getcwd()
        self.directory = os.path.join(base_dir, relative_directory)

    def save_to_txt(self, file_name, content):
        """
        Saves the given content to a text file with the given file name.

        Args:
            file_name (str): The name of the file to be saved.
            content (str): The content to be saved in the file.

        Returns:
            None

        Raises:
            ValueError: If the given file name is empty.
            OSError: If the file could not be saved.
        """
        logging.info(f"User save file")


        file_path = os.path.join(self.directory, f"{file_name}.txt")
        with open(file_path, "w") as file:
            file.write(content)        

    def save_to_file(self, file_name: str, data: str, format: str) -> None:
        """
        Saves the given data to a file with the given file name and format.

        Args:
            file_name (str): The name of the file to be saved.
            data (str): The data to be saved in the file.
            format (str): The format of the file to be saved.

        Returns:
            None

        Raises:
            ValueError: If the given file name or format is empty.
            OSError: If the file could not be saved.
        """
        logging.info(f"User save file")

        file_path = os.path.join(self.directory, f"{file_name}.{format}")

        cleaned_text = self.remove_color_tags(data)

        with open(file_path, "w") as file:
            file.write(cleaned_text)


    def remove_color_tags(self, text: str) -> str:
        """
        Removes color tags from the given text.

        Args:
            text (str): The text containing the color tags.

        Returns:
            str: The text without the color tags.

        Raises:
            ValueError: If the given text is empty.
        """

        logging.info(f"User remove color tags")

        clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)

        return clean_text   