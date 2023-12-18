import unittest

from Classes.labwork_2.calculator import Calculator


class TestCalculatorMultiplication(unittest.TestCase):
    """
    A test case for the multiplication functionality of the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_positive_multiplication(self):
        """
        A test case for the multiplication functionality of the Calculator class.

        This test case ensures that the Calculator class returns the correct result
        for positive multiplication operations.

        Parameters:
            self (object): The test case instance.

        Returns:
            None.

        Raises:
            AssertionError: If the result of the multiplication operation is not
            as expected.
        """
        calculator = Calculator(first_number=5.0, operator='*', second_number=5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, 25.0)

    def test_negative_multiplication(self):
        """
        A test case for the multiplication functionality of the Calculator class.

        This test case ensures that the Calculator class returns the correct result
        for negative multiplication operations.

        Parameters:
            self (object): The test case instance.

        Returns:
            None.

        Raises:
            AssertionError: If the result of the multiplication operation is not
            as expected.
        """
        calculator = Calculator(first_number=-5.0, operator='*', second_number=5.0)
        result = calculator.calculation()
        self.assertEqual(result._result, -25.0)

    def test_zero_multiplication(self):
        """
        A test case for the multiplication functionality of the Calculator class.

        This test case ensures that the Calculator class returns the correct result
        for zero multiplication operations.

        Parameters:
            self (object): The test case instance.

        Returns:
            None.

        Raises:
            AssertionError: If the result of the multiplication operation is not
            as expected.
        """
        calculator = Calculator(first_number=-5.0, operator='*', second_number=0)
        result = calculator.calculation()
        self.assertEqual(result._result, 0)
