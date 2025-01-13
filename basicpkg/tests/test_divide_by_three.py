# tests/test_divide_by_three.py

import unittest
from src.basicpkg.divide.by_three import divide_by_three

class TestDivideByThree(unittest.TestCase):
    def test_divide_by_three(self):
        self.assertEqual(divide_by_three(9), 3)
        self.assertEqual(divide_by_three(0), 0)
        self.assertEqual(divide_by_three(-9), -3)
        with self.assertRaises(ValueError):
            divide_by_three('a')  # Assuming the function raises error for non-numeric input

if __name__ == '__main__':
    unittest.main()