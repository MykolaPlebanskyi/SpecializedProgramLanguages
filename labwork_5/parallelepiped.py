class Parallelepiped:
    def __init__(self, width=None, height=None, length=None):
        self.width = width if width is not None else 10
        self.height = height if height is not None else 10
        self.save_height = self.height
        self.length = length if length is not None else 15
        self.oblique = '\\'
        self.top = '+'
        self.column = '|'
        self.transform = '\n'
        self.space_count = 0
        self.increment_count = 1

        self.default_colors = {
            'color1': 'yellow',
            'color2': 'blue',
            'color3': 'green',
            'color4': 'white'
        }
        self.gap = ' '
        self.line = '—'

    def custom_background_color(self, text, color):
        colors = {
            'black': '\033[40m',
            'red': '\033[41m',
            'green': '\033[42m',
            'yellow': '\033[43m',
            'blue': '\033[44m',
            'magenta': '\033[45m',
            'cyan': '\033[46m',
            'white': '\033[47m',
        }

        reset_color = '\033[0m'
        background_color = colors.get(color.lower(), '\033[47m')
        return f"{background_color}{text}{reset_color}"

    def display_parallelepiped(self, number, colors=None):
        colors = colors if colors else self.default_colors
        if number == 1:
            art = self.generate_layer(
                self.custom_background_color(' ', colors['color1']),
                self.custom_background_color(' ', colors['color2']),
                self.custom_background_color(' ', colors['color3']),
                self.custom_background_color(' ', colors['color4']),
                gap=self.gap,
                line=self.line
            )
        else:
            art = self.generate_layer(
                self.custom_background_color('  ', colors['color1']),
                self.custom_background_color('  ', colors['color2']),
                self.custom_background_color('  ', colors['color3']),
                self.custom_background_color('  ', colors['color4']),
                gap='  ',
                line='——'
            )
        return art

    def generate_layer(self, color1, color2, color3, color4, gap, line):
        shadow = color4 * self.save_height
        art = self.save_height * gap + self.top + line * (self.width - 2) + self.top + self.transform
        for i in range(self.length - 4, 0, -1):
            if self.height > 2:
                art = self._generate_multi_height_layer(color1, color2, gap, art)
            if self.height == 2:
                art = self._generate_two_height_layer(color1, color2, shadow, art)
            if self.height == 1:
                art = self._generate_one_height_layer(color1, color2, gap, shadow, art)
            if i == 1:
                art = self._generate_final_layer(color1, color3, color4, gap, line, shadow, art)
        return art

    def _generate_multi_height_layer(self, color1, color2, gap, art):
        art += self.save_height * gap + self.column + color1 * self.space_count + self.oblique + (
                color2 * (self.width - 2)) + self.oblique + self.transform
        self.reduction_height_and_magnification_count()
        return art

    def _generate_two_height_layer(self, color1, color2, shadow, art):
        art += shadow + self.top + self.space_count * color1 + self.oblique + (
                color2 * (self.width - 2)) + self.oblique + self.transform
        self.reduction_height_and_magnification_count()
        return art

    def _generate_one_height_layer(self, color1, color2, gap, shadow, art):
        art += gap * self.increment_count + shadow + self.oblique + (self.space_count - 1) * color1 + self.oblique + (
                color2 * (self.width - 2)) + self.oblique + self.transform
        self.update_increment()
        return art

    def _generate_final_layer(self, color1, color3, color4, gap, line, shadow, art):
        art += gap * self.increment_count + shadow + self.oblique + (self.space_count - 1) * color1 + self.top + (
                line * (self.width - 2)) + self.top + self.transform
        self.update_increment()
        for i in range(self.space_count, 0, -1):
            art += (gap * self.increment_count + shadow + self.oblique + color1 * (self.space_count - 2) +
                    self.column + color3 * (self.width - 2) + self.column + self.transform)
            self.reduction_count_and__height()
            self.update_increment()
            if self.space_count == 1:
                art += (gap * self.increment_count + color4 * self.save_height + self.top + line *
                        (self.width - 2) + self.top + self.transform)
                # self.height -= 1
                break
        return art

    def reduction_height_and_magnification_count(self):
        self.height -= 1
        self.space_count += 1

    def update_increment(self):
        self.increment_count += 1

    def reduction_count_and__height(self):
        self.height -= 1
        self.space_count -= 1
