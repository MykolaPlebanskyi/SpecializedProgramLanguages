import math
from labwork_2.calculator import Calculator


class AdvancedCalculator(Calculator):

    def _calculation(self, first_number, second_number, operator):
        if operator == 'sin':
            return math.sin(math.radians(first_number))
        elif operator == 'cos':
            return math.cos(math.radians(first_number))
        elif operator == 'tan':
            return math.tan(math.radians(first_number))
        else:
            return super()._calculation(first_number, second_number, operator)
