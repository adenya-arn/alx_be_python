import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(5, 5)
        self.assertEqual(result, 10)
        result1 = self.calc.add(-5, 10)
        self.assertEqual(result1, 5)

    def test_subtraction(self):
        result1 = self.calc.subtract(10, 9)
        self.assertEqual(result1, 1)
        result2 = self.calc.subtract(-12, 10)
        self.assertEqual(result2, -22)

    def test_divide(self):
        result = self.calc.divide(10, 5)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(10, 10)
        self.assertEqual(result, 100)
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == "__main__":
    unittest.main()

