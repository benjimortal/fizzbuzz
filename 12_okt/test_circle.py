from math import pi
from unittest import TestCase
from circle_0 import circle_area

class TestCircle(TestCase):
    def test_radius_1(self):
        self.assertAlmostEqual(circle_area(1), pi)

    def test_radius_0(self):
        self.assertEqual(circle_area(0), 0)

    def test_radius_10(self):
        self.assertEqual(circle_area(10), 314.1592653589793)

    def test_radius_negative(self):
        self.assertRaises(ValueError, circle_area, -10)

    def test_radius_bool(self):
        self.assertRaises(TypeError, circle_area, True)

    def test_radius_complex(self):
        self.assertRaises(TypeError, circle_area, 2+5j)

    def test_radius_string(self):
        self.assertRaises(TypeError, circle_area, 'radius')
