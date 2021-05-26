import unittest
import leap_year as ly
import fizzbuzz as fb

class testCaseYear(unittest.TestCase):
    def test_1(self):
        self.assertFalse(ly.leap_year(5))

class testCaseFizzbuzz(unittest.TestCase):
    def test1(self):
        self.assertEqual(fb.fizzbuzz(0), "")

    def test2(self):
        self.assertEqual(fb.fizzbuzz(4), "1 2 Fizz 4 ")

if __name__ == '__main__':
    unittest.main()