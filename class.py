import unittest

class SimpleMath:
    @staticmethod
    def addition(x, y):
        return x + y
    
    @staticmethod
    def subtraction(x, y):
        return x - y

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(2, 3)
        self.assertEqual(result, 5)
    def test_subtraction(self):
        result = SimpleMath.subtraction(5, 2)
        self.assertEqual(result, 3)
