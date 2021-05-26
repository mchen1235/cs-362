import unittest
import leap_year as ly
import fizzbuzz as fb

class testCaseYear(unittest.TestCase):
    def test_1(self):
        self.assertFalse(ly.leap_year(5))

    def test_2(self):
        self.assertTrue(ly.leap_year(4))

    def test_3(self):
        self.assertFalse(ly.leap_year(500))

    def test_4(self):
        self.assertTrue(ly.leap_year(400))

class testCaseFizzbuzz(unittest.TestCase):
    def test1(self):
        self.assertEqual(fb.fizzbuzz(0), "")

    def test2(self):
        self.assertEqual(fb.fizzbuzz(4), "1 2 Fizz 4 ")

    def test3(self):
        self.assertEqual(fb.fizzbuzz(6), "1 2 Fizz 4 Buzz Fizz ")

    def test4(self):
        self.assertEqual(fb.fizzbuzz(16), "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 ")

if __name__ == '__main__':
    unittest.main()