import unittest
import cube_volume

class testCaseCube(unittest.TestCase):
    def test1(self):
        result = cube_volume.cube(3)
        self.assertEqual(result, 27)

    def test2(self):
        result = cube_volume.cube(2.2)
        self.assertAlmostEqual(result, 10.648)

    def test3(self):
        self.assertRaises(TypeError, cube_volume.cube, "a")

    def test4(self):
        result = cube_volume.cube(1)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()