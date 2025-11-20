import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_factorial_4(self):
        self.assertEqual(get_factorial(4), 24)

    def test_factorial_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_factorial_6(self):
        self.assertEqual(get_factorial(6), 720)

    def test_sum_odd_7(self):
        self.assertEqual(sum_odd_numbers(7), 16)

    def test_sum_odd_9(self):
        self.assertEqual(sum_odd_numbers(9), 25)

    def test_sum_odd_10(self):
        self.assertEqual(sum_odd_numbers(10), 25)
