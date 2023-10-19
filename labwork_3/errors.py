class Error:
    def check_widht(self, parameter):
        try:
            parameter = int(parameter)
            if parameter < 50:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_height(self, parameter):
        try:
            parameter = int(parameter)
            if parameter <= 0:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_font(self, number):
        try:
            number = int(number)
            if number <= 0 or number > 6:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_color(self, number):
        try:
            number = int(number)
            if number <= 0 or number > 8:
                raise ValueError
        except ValueError:
            return ValueError()
