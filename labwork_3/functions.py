from colorama import Fore
from labwork_3.art import Art


class Function(Art):

    def _choose_font(self, user_font):
        if user_font == '1':
            return "5lineoblique"
        elif user_font == '2':
            return "banner"
        elif user_font == '3':
            return "slant"
        elif user_font == '4':
            return "doom"
        elif user_font == '5':
            return "cyberlarge"
        elif user_font == '6':
            return "big"

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

    def _scale_ascii_art_height(self, art, height_scale):
        lines = art.split('\n')
        scaled_lines = []

        for line in lines:
            scaled_lines.extend([line] * height_scale)

        return '\n'.join(scaled_lines)
