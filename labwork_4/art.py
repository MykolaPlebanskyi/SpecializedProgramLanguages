from labwork_4 import fonts


class Art:
    def __init__(self):
        self.font = fonts.banner

    def create(self, direction_message):
        max_lines = max(len(self.font.get(letter, '').split('\n')) for letter in direction_message)
        art = ['' for _ in range(max_lines)]

        for letter in direction_message:
            letter_lines = self.font.get(letter, '').split('\n')
            art = [''.join([line1, line2]) for line1, line2 in zip(art, letter_lines)]

        return '\n'.join(art)


