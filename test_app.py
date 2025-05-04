# test_app.py

import unittest
from app import add, subtract, multiply

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(subtract(4, 5), -1)
        self.assertEqual(subtract(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()