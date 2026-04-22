import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.evaluate("5 + 5")
        self.assertEqual(result, 10)

    def test_subtraction(self):
        result = self.calculator.evaluate("30 - 4")
        self.assertEqual(result, 26)

    def test_multiplication(self):
        result = self.calculator.evaluate("2 * 4")
        self.assertEqual(result, 8)

    def test_division(self):
        result = self.calculator.evaluate("30 / 2")
        self.assertEqual(result, 15)

    def test_nested_expression(self):
        result = self.calculator.evaluate("2 + 4 * 5")
        self.assertEqual(result, 22)

    def test_complex_expression(self):
        result = self.calculator.evaluate("2 + 2 - 8 / 2 + 5")
        self.assertEqual(result, 5)

    def test_empty_expression(self):
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("5 & 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 5")


if __name__ == "__main__":
    unittest.main()
