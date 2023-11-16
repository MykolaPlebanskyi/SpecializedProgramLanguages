class Error:
    def check_widht(self, parameter):
        try:
            parameter = int(parameter)
            if parameter < 50:
                raise ValueError
        except ValueError:
            return ValueError()

    def check_color(self, number):
        try:
            number = int(number)
            if number <= 0 or number > 4:
                raise ValueError
        except ValueError:
            return ValueError()
