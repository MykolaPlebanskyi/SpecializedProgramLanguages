import unittest

from Classes.labwork_2.calculator import Calculator


class TestCalculatorDivision(unittest.TestCase):
    """
    A test case class for testing the division functionality of the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_positive_division(self):
        """
        This function tests the positive division functionality of the Calculator class.

        Parameters:
        first_number (float): the first number in the division operation
        operator (str): the division operator
        second_number (float): the second number in the division operation

        Returns:
        None

        Raises:
        ValueError: if the second number is zero

        Example:
        >>> calculator = Calculator(first_number=25.0, operator='/', second_number=5.0)
        >>> result = calculator.calculation()
        >>> self.assertEqual(result._result, 5.0)
        """
        calculator = Calculator(first_number=25.0, operator='/', second_number=5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, 5.0)

    def test_negative_division(self):
        """
        This function tests the negative division functionality of the Calculator class.

        Parameters:
        first_number (float): the first number in the division operation
        operator (str): the division operator
        second_number (float): the second number in the division operation

        Returns:
        None

        Raises:
        ValueError: if the second number is zero

        Example:
        >>> calculator = Calculator(first_number=25.0, operator='/', second_number=5.0)
        >>> result = calculator.calculation()
        >>> self.assertEqual(result._result, 5.0)
        """
        calculator = Calculator(first_number=-25.0, operator='/', second_number=5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, -5.0)
    def test_zero_division(self):
        """
        This function tests the zero division functionality of the Calculator class.
        Parameters:
        first_number (float): the first number in the division operation
        operator (str): the division operator
        second_number (float): the second number in the division operation

        Returns:
        None

        Raises:
        ValueError: if the second number is zero

        Example:
        >>> calculator = Calculator(first_number=5.0, operator='/', second_number=0)
        >>> result = calculator.calculation()
        >>> self.assertEqual(result._result, 0)
        """
        calculator = Calculator(first_number=5.0, operator='/', second_number=0)
        result = calculator.calculation()
        self.assertEqual(result._result, 0)