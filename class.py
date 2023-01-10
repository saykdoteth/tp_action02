class SimpleMath:
    @staticmethod
    def addition(x, y):
        return x + y

import unittest

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(2, 3)
        self.assertEqual(result, 5)
