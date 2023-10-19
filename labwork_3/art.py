import pyfiglet


class Art:
    def __init__(self):
        self.font = 'banner'
        self.justify = 'center'

    def _create_ascii_art(self, text, width, character):
        ascii_art = pyfiglet.figlet_format(text, justify=f'{self.justify}', font=self.font, width=width)

        lines = ascii_art.split('\n')

        for i in range(len(lines)):
            line = lines[i]
            new_line = ''
            for char in line:
                if char != ' ':
                    new_line += character
                else:
                    new_line += ' '
            lines[i] = new_line

        modified_ascii_art = '\n'.join(lines)

        return modified_ascii_art
