import unittest
from tests.homework.h_strings import test_strings

suite = unittest.TestLoader().loadTestsFromModule(test_strings)
unittest.TextTestRunner(verbosity=2).run(suite)
