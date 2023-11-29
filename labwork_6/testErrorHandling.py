import unittest

from labwork_2.calculator import Calculator


class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_error_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc._calculation(10, 0, '/')
