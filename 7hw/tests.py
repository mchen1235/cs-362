import unittest
import leap_year as ly
import fizzbuzz as fb

class testCaseYear(unittest.TestCase):
    def test_1(self):
        self.assertFalse(ly.leap_year(5))

    def test_2(self):
        self.assertTrue(ly.leap_year(4))

class testCaseFizzbuzz(unittest.TestCase):
    def test1(self):
        self.assertEqual(fb.fizzbuzz(0), "")

    def test2(self):
        self.assertEqual(fb.fizzbuzz(4), "1 2 Fizz 4 ")

    def test3(self):
        self.assertEqual(fb.fizzbuzz(6), "1 2 Fizz 4 Buzz Fizz ")
        
if __name__ == '__main__':
    unittest.main()