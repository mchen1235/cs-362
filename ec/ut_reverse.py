import unittest
import reverse as r

class testCaseReverse(unittest.TestCase):
    def test_1(self):
        self.assertEqual(r.reverse("Hello World."), "World Hello.")

    def test_2(self):
        self.assertEqual(r.reverse(""), "")

    def test_3(self):
        self.assertEqual(r.reverse("There is no period"), "period no is There")

    def test_4(self):
        self.assertEqual(r.reverse("Double  space single"), "single space  Double")

if __name__ == '__main__':
    unittest.main()
