import unittest
import fizzbuzz as fb

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