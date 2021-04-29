import unittest
import calc

class testCaseCalc(unittest.TestCase):
    def test1(self):
        result = calc.add(1, 4)
        self.assertEqual(result, 5)

    def test2(self):
        result = calc.subtract(1, 4)
        self.assertEqual(result, -3)

    def test3(self):
        result = calc.multiply(1, 4)
        self.assertEqual(result, 4)

    def test4(self):
        result = calc.divide(1, 4)
        self.assertEqual(result, 0.25)

    def test5(self):
        result = calc.add(1, 4)
        self.assertEqual(result, 6)

    def test6(self):
        result = calc.subtract(6, 4)
        self.assertEqual(result, 3)

    def test7(self):
        result = calc.multiply(2, 4)
        self.assertEqual(result, 4)

    def test8(self):
        result = calc.divide(4, 4)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()