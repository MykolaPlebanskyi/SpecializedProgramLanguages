from Classes.labwork_5.parallelepiped import Parallelepiped
from UI.MenuBuilder.menu_builder import Menu
from Shared.Choice.run_again import RunAgain


class ParallelepipedMenu(Menu):
    """
    A menu class for creating and displaying parallelepipeds.

    Attributes:
        parallelepiped (Parallelepiped): The parallelepiped object.
        run_again (RunAgain): The run again object.
        _config (dict): The configuration dictionary.

    Methods:
        run(): Runs the parallelepiped menu.
        input_colors(parallelepiped): Takes user input for parallelepiped colors.

    """

    def __init__(self):
        super().__init__()
        self.parallelepiped = Parallelepiped()
        self.run_again = RunAgain()
        self._config = self._config['labwork_5']

    def run(self):
        """
        Runs the parallelepiped menu.

        The menu prompts the user to enter the width, height, and length of the parallelepiped.
        Then, it asks for the colors of each side of the parallelepiped.
        The user can choose to display the parallelepiped with or without zoom.
        Finally, the parallelepiped is saved to a file.
        The menu can be run again if the user chooses to do so.

        """

        while True:
            width = self.parallelepiped.valid.get_input(self._config["user_width"], int)
            height = self.parallelepiped.valid.get_input(self._config["user_height"], int)
            length = self.parallelepiped.valid.get_input(self._config["user_length"], int)
            user_parallelepiped = Parallelepiped(width, height, length)
            self.parallelepiped.color_chooser.display_color_menu()
            colors = self.input_colors(self.parallelepiped)
            user_parallelepiped = user_parallelepiped.display_parallelepiped_without_zoom(user_parallelepiped,
                                                                                          colors=colors)

            choose_zoom = self.parallelepiped.valid.get_input(self._config["choose_zoom"], str)
            if choose_zoom == "yes":
                user_parallelepiped = Parallelepiped(width, height, length)
                user_parallelepiped = user_parallelepiped.display_parallelepiped_with_zoom(user_parallelepiped,
                                                                                           colors=colors)
            self.parallelepiped.save_to_file(user_parallelepiped)
            if self.run_again.get_choice():
                break

    def input_colors(self, parallelepiped):
        """
        Takes user input for parallelepiped colors.

        Args:
            parallelepiped (Parallelepiped): The parallelepiped object.

        Returns:
            dict: A dictionary containing the colors of each side of the parallelepiped.

        """

        color1 = self.parallelepiped.valid.get_input(self._config["color_left"], str, None) or \
                 parallelepiped.default_colors['color1']
        color2 = self.parallelepiped.valid.get_input(self._config["color_top"], str, None) or \
                 parallelepiped.default_colors['color2']
        color3 = self.parallelepiped.valid.get_input(self._config["color_front"], str, None) or \
                 parallelepiped.default_colors['color3']
        color4 = self.parallelepiped.valid.get_input(self._config["color_shadow"], str, None) or \
                 parallelepiped.default_colors['color4']

        parallelepiped_colors = {
            'color1': color1,
            'color2': color2,
            'color3': color3,
            'color4': color4
        }
        return parallelepiped_colors
