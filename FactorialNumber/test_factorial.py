import unittest
import factorialNum

class TestFactorialNum(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(factorialNum.factorial(2,1), 2 )
        self.assertNotEqual(factorialNum.factorial(2,1), 45)
if __name__ == "main":
    unittest.main()