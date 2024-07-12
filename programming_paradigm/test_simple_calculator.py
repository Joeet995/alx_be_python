import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculater(unittest.TestCase):

    def setup(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(-5,3),-8)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,2),10)
        self.assertEqual(self.calc.multiply(-3,1),-3)
        self.assertEqual(self.calc.multiply(5,0),0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10,5),2)
        self.assertEqual(self.calc.divide(10,0),None)
        self.assertEqual(self.calc.divide(-10,5),-2)
        self.assertEqual(self.calc.divide(0,5),0)