import unittest
import leap_year as ly

class testCaseCalc(unittest.TestCase):
    def test_1(self):
        result = ly.leap_year(400)
        self.assertTrue(result)

    def test_2(self):
        result = ly.leap_year(401)
        self.assertFalse(result)

    def test_3(self):
        result = ly.leap_year(404)
        self.assertTrue(result)

    def test_4(self):
        result = ly.leap_year(500)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()