import unittest
import primeNumber

class TestPrimeNum(unittest.TestCase):
    def test_NumPrime(self):
        self.assertEqual(primeNumber.is_prime(2), True)
        self.assertNotEqual(primeNumber.is_prime(9), True)
if __name__ == "main":
    unittest.main()