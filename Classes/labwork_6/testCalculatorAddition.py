import unittest

from Classes.labwork_2.calculator import Calculator


class TestCalculatorAddition(unittest.TestCase):
    """
    This class contains unit tests for the addition operation of the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_positive_add(self):
        """
        This function tests the positive addition of two numbers.

        Parameters:
        first_number (float): the first number to be added
        operator (str): the addition operator
        second_number (float): the second number to be added

        Returns:
        None

        Raises:
        ValueError: if the operator is not '+'

        """
        calculator = Calculator(first_number=2.0, operator='+', second_number=2.0)
        result = calculator.calculation()
        self.assertEqual(result._result, 4.0)

    def test_negative_add(self):
        """
        This function tests the negative addition of two numbers.

        Parameters:
        first_number (float): the first number to be added
        operator (str): the addition operator
        second_number (float): the second number to be added

        Returns:
        None

        Raises:
        ValueError: if the operator is not '+'

        """
        calculator = Calculator(first_number=-3.0, operator='+', second_number=-5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, -8.0)
