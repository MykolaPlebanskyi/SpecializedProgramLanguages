import unittest

from labwork_2.calculator import Calculator


class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_positive_division(self):
        result = self.calc._calculation(25, 5, '/')
        self.assertEqual(result, 5)

    def test_negative_division(self):
        result = self.calc._calculation(-25, 5, '/')
        self.assertEqual(result, -5)

    def test_zero_division(self):
        result = self.calc._calculation(-5, 0, '/')
        self.assertEqual(result, 0)