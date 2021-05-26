import unittest
import leap_year as ly

class testCaseCalc(unittest.TestCase):
    def test_1(self):
        self.assertFalse(ly.leap_year(5))

    def test_2(self):
        self.assertTrue(ly.leap_year(4))

    def test_3(self):
        self.assertTrue(ly.leap_year(400))

    def test_4(self):
        self.assertFalse(ly.leap_year(500))

if __name__ == '__main__':
    unittest.main()