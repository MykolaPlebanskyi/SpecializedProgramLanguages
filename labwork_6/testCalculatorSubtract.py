import unittest

from labwork_2.calculator import Calculator


class TestCalculatorSubtraction(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_positive_subtract(self):
        result = self.calc._calculation(10, 5, '-')
        self.assertEqual(result, 5)

    def test_negative_subtract(self):
        result = self.calc._calculation(-10, -5, '-')
        self.assertEqual(result, -5)