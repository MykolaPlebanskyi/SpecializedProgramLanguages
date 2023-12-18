import unittest

from Classes.labwork_2.calculator import Calculator


class TestCalculatorSubtraction(unittest.TestCase):
    """
    A test case for the subtraction functionality of the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_positive_subtract(self):
        """
        A test case for the positive subtraction functionality of the Calculator class.

        Parameters:
        first_number (float): the first number in the subtraction operation
        operator (str): the subtraction operator
        second_number (float): the second number in the subtraction operation

        Returns:
        float: the result of the subtraction operation

        Raises:
        ValueError: if the first_number or second_number is not a float
        """
        calculator = Calculator(first_number=10.0, operator='-', second_number=5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, 5.0)

    def test_negative_subtract(self):
        """
        A test case for the negative subtraction functionality of the Calculator class.

        Parameters:
        first_number (float): the first number in the subtraction operation
        operator (str): the subtraction operator
        second_number (float): the second number in the subtraction operation

        Returns:
        float: the result of the subtraction operation

        Raises:
        ValueError: if the first_number or second_number is not a float
        """
        calculator = Calculator(first_number=-10.0, operator='-', second_number=-5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, -5.0)