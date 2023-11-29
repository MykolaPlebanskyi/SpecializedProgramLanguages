import unittest

from labwork_2.calculator import Calculator


class TestCalculatorAddition(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_positive_add(self):
        result = self.calc._calculation(3, 5, '+')
        self.assertEqual(result, 8)

    def test_negative_add(self):
        result = self.calc._calculation(-3, -5, '+')
        self.assertEqual(result, -8)

