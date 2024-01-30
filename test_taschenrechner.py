import unittest
from taschenrechner import addieren, subtrahieren  # Annahme: Dein Skript heißt 'calculator.py'

class TestCalculator(unittest.TestCase):

    def test_addieren(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)

    def test_subtrahieren(self):
        self.assertEqual(subtrahieren(10, 5), 5)
        self.assertEqual(subtrahieren(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
