import sys, os, time
import unittest

sys.path.append(os.getcwd())
from vector3d import *
from ray import *


class VectorsTest(unittest.TestCase):
    """There are vectors tests"""
    def setUp(self):
        self.vector1 = Vector(1.0, 2.0, 3.0)
        self.vector2 = Vector(4.0, 5.0, 6.0)

    def test_add(self):
        self.assertEqual((self.vector1 + self.vector2).v0, 5.0)

    def test_sub(self):
        self.assertEqual((self.vector1 - self.vector2).v1, -3.0)

    def test_mul(self):
        self.assertEqual((self.vector1 * 6.0).v2, 18.0)

    def test_truediv(self):
        self.assertEqual((self.vector1 / 1.5).v2, 2.0)
        self.assertEqual((self.vector1 / 0.0).v2, math.inf)

    def test_dot(self):
        self.assertEqual(self.vector1.dot(self.vector2), 32.0)

    def test_norma(self):
        self.assertEqual(self.vector1.norma(), math.sqrt(self.vector1.dot(self.vector1)))

    def test_normalization(self):
        self.assertEqual(self.vector1.normalization().v2, 3.0 / math.sqrt(14))


class RayTest(unittest.TestCase):
    """There are rays tests"""
    def setUp(self):
        origin = (1.0, 2.0, 3.0)
        basis = (4.0, 5.0, 6.0)
        self.ray = Ray(origin, basis)

    def test_basis_add_origin(self):
        self.assertEqual((self.ray.origin + self.ray.basis).v0, 5.0)


if __name__ == '__main__':
    unittest.main()