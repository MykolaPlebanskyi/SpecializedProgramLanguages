class Error:
    def check_empty(self, value):
        return bool(value)

    def check_width_and_height(self, parameter):
        try:
            parameter = int(parameter)
            if parameter < 8:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_length(self, height, length):
        try:
            height = int(height)
            length = int(length)
            if length - height < 4:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_color(self, number):
        try:
            str(number)
        except ValueError:
            return ValueError()