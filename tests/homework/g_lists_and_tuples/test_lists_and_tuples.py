import sys
import os

# Fix the path to src (go up 3 levels)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

import unittest
from src.homework.g_lists_and_t_tuples.lists import get_lowest_list_value, get_highest_list_value


class TestConfig(unittest.TestCase):
    def test_get_lowest_list_value(self):
        numbers = [8, 10, 1, 50, 20]
        result = get_lowest_list_value(numbers)
        self.assertEqual(result, 1)

    def test_get_highest_list_value(self):
        numbers = [8, 10, 1, 50, 20]
        result = get_highest_list_value(numbers)
        self.assertEqual(result, 50)


if __name__ == '__main__':
    unittest.main()
