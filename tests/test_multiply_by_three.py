# tests/test_multiply_by_three.py

import unittest
from src.basicpkg.multiply.by_three import multiply_by_three

class TestMultiplyByThree(unittest.TestCase):
    def test_multiply_by_three(self):
        self.assertEqual(multiply_by_three(3), 9)
        self.assertEqual(multiply_by_three(0), 0)
        self.assertEqual(multiply_by_three(-3), -9)
        with self.assertRaises(ValueError):
            multiply_by_three('a')  # Assuming the function raises error for non-numeric input

if __name__ == '__main__':
    unittest.main()