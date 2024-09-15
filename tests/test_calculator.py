import unittest

from src.calculator import sum, substract, multiplication, division

class CalculatorTests(unittest.TestCase):

    def test_sum(self):     #Test suma
        assert sum(2, 3) == 5

    def test_substract(self):   # Test resta
        assert substract(10, 5) == 5
    
    def test_multiplication(self):  # Test multiplicación
        assert multiplication(10, 5) == 50
    
    def test_division(self):    # Test división
        assert division(10, 5) == 2
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(30, 0)
