import unittest

from labwork_2.calculator import Calculator


class TestCalculatorMultiplication(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_positive_multiplication(self):
        result = self.calc._calculation(5, 5, '*')
        self.assertEqual(result, 25)

    def test_negative_multiplication(self):
        result = self.calc._calculation(-5, 5, '*')
        self.assertEqual(result, -25)

    def test_zero_multiplication(self):
        result = self.calc._calculation(-5, 0, '*')
        self.assertEqual(result, 0)
