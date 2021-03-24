import unittest
import evenOdd

class TestEvenOddNum(unittest.TestCase):
    def test_evenOddNum(self):
        self.assertEqual(evenOdd.EvenOdd(2), True)
        self.assertNotEqual(evenOdd.EvenOdd(2), False)

if __name__ == "main":
    unittest.main()