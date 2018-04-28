import unittest
from main import CompoundInterest


class TestCalculator(unittest.TestCase):
    def test_compound_interest_over_1_year(self):
        ci = CompoundInterest(1, 1000, 10)
        self.assertEqual(ci.calculate_term_total_repayment(), 1100)

    def test_compound_interest_over_2_years(self):
        ci = CompoundInterest(2, 1000, 10)
        self.assertEqual(ci.calculate_term_total_repayment(), 1210)

    def test_compound_interest_over_3_years(self):
        ci = CompoundInterest(3, 1000, 10)
        self.assertEqual(ci.calculate_term_total_repayment(), 1331)

    def test_compound_interest_over_4_years(self):
        ci = CompoundInterest(4, 1000, 10)
        self.assertEqual(ci.calculate_term_total_repayment(), 1464.1)

    def test_compound_interest_over_5_years(self):
        ci = CompoundInterest(5, 1000, 10)
        self.assertEqual(ci.calculate_term_total_repayment(), 1610.51)

    def test_compound_interest_at_different_rate(self):
        ci = CompoundInterest(3, 1000, 20)
        self.assertEqual(ci.calculate_term_total_repayment(), 1728)

    def test_compound_interest_at_different_principle(self):
        ci = CompoundInterest(5, 1234, 20)
        self.assertEqual(ci.calculate_term_total_repayment(), 3070.59)



if __name__ == "__main__":
    unittest.main()