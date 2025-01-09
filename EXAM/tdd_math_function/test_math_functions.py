import unittest
from math_functions import absolute_value

class TestMathFunctions(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(absolute_value(5), 5)

    def test_negative_number(self):
        self.assertEqual(absolute_value(-5), 5)

    def test_zero(self):
        self.assertEqual(absolute_value(0), 0)

if __name__ == "__main__":
    unittest.main()