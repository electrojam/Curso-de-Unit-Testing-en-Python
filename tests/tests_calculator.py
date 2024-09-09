import unittest

from src.calculator import sum, substract

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2 ,3) == 6

    def test_substract(self):
        assert substract(10 ,5) == 5