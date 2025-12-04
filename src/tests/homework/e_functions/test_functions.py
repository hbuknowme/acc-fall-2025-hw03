import unittest
from src.e_functions.value_return_functions import (
    get_gross_pay,
    get_fica_tax,
    get_federal_tax
)

class TestPayrollFunctions(unittest.TestCase):
    def test_payroll_case1(self):
        hours = 40
        rate = 10
        gross = get_gross_pay(hours, rate)
        fica = get_fica_tax(gross)
        federal = get_federal_tax(gross)
        self.assertEqual(round(gross, 2), 400.00)
        self.assertEqual(round(fica, 2), 30.60)
        self.assertEqual(round(federal, 2), 32.00)

    def test_payroll_case2(self):
        hours = 45
        rate = 10
        gross = get_gross_pay(hours, rate)
        fica = get_fica_tax(gross)
        federal = get_federal_tax(gross)
        self.assertEqual(round(gross, 2), 475.00)
        self.assertEqual(round(fica, 2), 36.34)
        self.assertEqual(round(federal, 2), 38.00)

    def test_payroll_case3(self):
        hours = 30
        rate = 10
        gross = get_gross_pay(hours, rate)
        fica = get_fica_tax(gross)
        federal = get_federal_tax(gross)
        self.assertEqual(round(gross, 2), 300.00)
        self.assertEqual(round(fica, 2), 22.95)
        self.assertEqual(round(federal, 2), 24.00)

if __name__ == "__main__":
    unittest.main()
