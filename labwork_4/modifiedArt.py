from labwork_4 import variables
from labwork_4.art import Art
from labwork_4.functions import Function


class CustomArt(Art):

    def __init__(self):
        super().__init__()
        self.alignment = 'center'
        self.width = 50
        self.character = '*'
        self.art = Art()
        self.functions = Function()

    def default_character(self, character):
        if character is None or character.strip() == "":
            character = self.character
            return character
        else:
            return character

    def default_alignment(self, alignment):
        if (alignment is None or alignment.strip() == ""
                or (alignment != 'left' and alignment != 'right')):
            alignment = self.alignment
            return alignment
        else:
            return alignment

    def default_width(self, width):
        if width is None or width <= 0:
            width = self.width
            return width
        else:
            return width

    def _check_parameters(self, width, alignment, character):
        width = self.default_width(width)
        alignment = self.default_alignment(alignment)
        character = self.default_character(character)
        return width, alignment, character

    def create_all(self, direction_message, width, alignment, character):
        width, alignment, character = self._check_parameters(width, alignment, character)
        art_with_width = self._create_width(direction_message, width)
        art_with_alignment = self._create_alignment(art_with_width, width, alignment)
        art_with_character = self._create_character(art_with_alignment, character)
        return art_with_character

    def _create_width(self, direction_message, max_width):
        max_lines = max(len(self.font.get(letter, '').split('\n')) for letter in direction_message)
        alignment_func = str.center

        line = [""] * max_lines
        line_width = 0
        art = []

        for word in direction_message:
            letter_lines = self.font.get(word, '').split('\n')
            word_width = len(letter_lines[0]) + 1

            if line_width + word_width <= max_width:
                for i in range(max_lines):
                    line[i] += alignment_func(letter_lines[i], word_width)
                line_width += word_width
            else:
                art.append('\n'.join(line))
                line = [""] * max_lines
                for i in range(max_lines):
                    line[i] += alignment_func(letter_lines[i], word_width)
                line_width = word_width

        art.append('\n'.join(line))
        output = '\n'.join(art)
        return output

    def _create_alignment(self, direction_message, width, alignment):

        output_lines = direction_message.split('\n')
        aligned_output_lines = []

        for line in output_lines:
            if alignment == variables.alignment_left:
                aligned_line = f"{' '}{line}"
            elif alignment == variables.alignment_right:
                aligned_line = f"{line.rjust(width)}"
            elif alignment == variables.alignment_center:
                aligned_line = f"{line.center(width)}"
            else:
                aligned_line = line

            aligned_output_lines.append(aligned_line)

        aligned_output = '\n'.join(aligned_output_lines)

        return aligned_output

    def _create_character(self, direction_message, character):

        lines = direction_message.split('\n')

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
