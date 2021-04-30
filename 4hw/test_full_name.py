import unittest
import full_name as fn

class testCaseName(unittest.TestCase):
    def test1(self):
        result = fn.full_name("Michael", "Chen")
        self.assertEqual(result, "Michael Chen")

    def test2(self):
        self.assertRaises(TypeError, fn.full_name, "Michael")

    def test3(self):
        self.assertRaises(TypeError, fn.full_name, "Michael", "1233")

if __name__ == '__main__':
    unittest.main()