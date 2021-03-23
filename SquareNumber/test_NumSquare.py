import unittest
import NumSquare

class TestSquareNum(unittest.TestCase):
    def test_Square(self):
        self.assertEqual(NumSquare.squareNum(5,1,1,2),25)
        self.assertNotEqual(NumSquare.squareNum(5,1,1,2),58)
if __name__ == "__main__":
    unittest.main()