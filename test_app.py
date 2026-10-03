import unittest
from app import add

class AddTests(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_handles_negative_numbers(self):
        self.assertEqual(add(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()
