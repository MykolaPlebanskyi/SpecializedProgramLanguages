from colorama import Fore, Back


class Function:

    def _choose_color(self, user_color):
        if user_color == '1':
            return Fore.LIGHTBLACK_EX + Back.WHITE
        elif user_color == '2':
            return Fore.BLACK + Back.WHITE
        elif user_color == '3':
            return Fore.WHITE + Back.BLACK
        elif user_color == '4':
            return Fore.WHITE + Back.LIGHTBLACK_EX
