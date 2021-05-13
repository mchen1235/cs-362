import unittest
import palindrome

class testCaseCalc(unittest.TestCase):
    def test1(self):
        result = palindrome.palindrome("abba")
        self.assertTrue(result)

    def test2(self):
        result = palindrome.palindrome("ababa")
        self.assertTrue(result)

    def test3(self):
        result = palindrome.palindrome("")
        self.assertTrue(result)

    def test4(self):
        result = palindrome.palindrome("abbbaaaaaa")
        self.assertFalse(result)

    def test5(self):
        result = palindrome.palindrome(" b a b ")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()