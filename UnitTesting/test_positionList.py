import unittest
import PositionList

class TestPositionList(unittest.TestCase):
    def test_position(self):
        self.assertEqual(PositionList.search([5,2,3,9,7],9), 3)
def test_position(self):
        self.assertEqual(PositionList.search1([5,2,3,9,7],200), -1)

if __name__ == "__main__":
    unittest.main()
