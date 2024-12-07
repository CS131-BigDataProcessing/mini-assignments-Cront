# test_operations.py
import unittest
from math_functions import power, division


class TestOperations(unittest.TestCase):
    def test_power(self):
        # Test positive exponents
        self.assertEqual(power(2, 3), 8)
        # Test zero as an exponent
        self.assertEqual(power(2, 0), 1)
        # Test zero base with non-zero exponent
        self.assertEqual(power(0, 3), 0)
        # Test both zero base and exponent
        with self.assertRaises(ValueError):
            power(0, 0)
        # Test negative exponent
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_division(self):
        # Test normal division
        self.assertEqual(division(10, 2), 5)
        # Test division by zero
        with self.assertRaises(ValueError):
            division(10, 0)
        # Test division resulting in a float
        self.assertAlmostEqual(division(5, 2), 2.5)
        # Test division by negative number
        self.assertEqual(division(10, -2), -5)


if __name__ == "__main__":
    unittest.main()
