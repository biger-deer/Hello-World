"""
Author: Administrator
Date: 2025/2/17
Description: 
"""

import unittest
from add_zl import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    # def test_github_status_check(self):
    #     self.assertEqual(1, 0)

if __name__ == '__main__':
    unittest.main()

