import unittest
from src.e_functions.value_return_functions import (
    get_gross_pay,
    get_fica_tax,
    get_federal_tax
)

class TestFunctions(unittest.TestCase):

    def test_payroll_case1(self):
        hours = 40
        rate = 10
        gross = get_gross_pay(hours, rate)
        self.assertEqual(gross, 400)
        self.assertAlmostEqual(get_fica_tax(gross), 30.6, places=2)
        self.assertAlmostEqual(get_federal_tax(gross), 32.0, places=2)

    def test_payroll_case2(self):
        hours = 45
        rate = 10
        gross = get_gross_pay(hours, rate)
        self.assertEqual(gross, 475)
        self.assertAlmostEqual(get_fica_tax(gross), 36.34, places=2)
        self.assertAlmostEqual(get_federal_tax(gross), 38.0, places=2)

    def test_payroll_case3(self):
        hours = 30
        rate = 10
        gross = get_gross_pay(hours, rate)
        self.assertEqual(gross, 300)
        self.assertAlmostEqual(get_fica_tax(gross), 22.95, places=2)
        self.assertAlmostEqual(get_federal_tax(gross), 24.0, places=2)
