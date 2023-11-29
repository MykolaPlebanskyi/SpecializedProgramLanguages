class Error:

    def number_input_check(self, number):
        try:
            number = int(number)
            if number < 1 or number > 5:
                raise ValueError
        except ValueError:
            return ValueError()
