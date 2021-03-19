import unittest
import PositionList

class TestPositionList(unittest.TestCase):
    def test_position(self):
        self.assertEqual(PositionList.search1([5,2,3,9,7],9), 3)

    def test_position2(self):
            self.assertEqual(PositionList.search1([5,2,3,9,7],200), -1)
    def test_no_encontrado(self):
        nums = [5,2,3,9,7]
        self.assertTrue(PositionList.search1(nums, 2) == 1)
        
    def test_No_Equals(self):
        self.assertNotEqual(PositionList.search1([5,2,3,9,7], 12), 1)

if __name__ == "__main__":
    unittest.main()
