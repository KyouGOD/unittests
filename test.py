import unittest
from main import interest_rate, deposit_term, starting_capital


class TestSite(unittest.TestCase):

    def test_float(self):
        self.assertEqual(type(interest_rate(1)), float, "Error")
        self.assertEqual(type(starting_capital(1)), float, "Error")
        self.assertEqual(type(deposit_term(1)), float, "Error")
