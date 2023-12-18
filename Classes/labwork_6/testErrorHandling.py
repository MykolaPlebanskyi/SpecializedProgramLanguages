import unittest

from Classes.labwork_2.calculator import Calculator


class TestErrorHandling(unittest.TestCase):
    """
    A test case for error handling in the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_error_division_by_zero(self):
        """
        This function tests the error handling of the Calculator class.
        It specifically tests the case where the user attempts to divide by zero.

        Args:
            self (object): The instance of the class being tested.

        Raises:
            ZeroDivisionError: This exception is raised if the user attempts to divide by zero.

        Returns:
            None: This function does not return a value.
        """
        calculator = Calculator(first_number=10.0, operator='/', second_number=0.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.calculation()