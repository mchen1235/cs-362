import unittest
import list_average as la

class testCaseAverage(unittest.TestCase):
    def test1(self):
        result = la.list_average([1, 2, 3])
        self.assertEqual(result, 2)

    def test2(self):
        result = la.list_average([1,2])
        self.assertAlmostEqual(result, 1.5)

    def test3(self):
        self.assertRaises(ZeroDivisionError, la.list_average, [])

    def test4(self):
        result = la.list_average([5])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()