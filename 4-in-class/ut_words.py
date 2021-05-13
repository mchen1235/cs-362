import unittest
import words

class testCaseCalc(unittest.TestCase):
    def test1(self):
        result = words.words("Hello There")
        self.assertEqual(result, 2)

    def test2(self):
        result = words.words(" Hello   There ")
        self.assertEqual(result, 2)

    def test3(self):
        result = words.words("")
        self.assertEqual(result, 0)

    def test4(self):
        result = words.words("  Hello  ")
        self.assertEqual(result, 1)

    def test5(self):
        result = words.words("Hello")
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()