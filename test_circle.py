"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
from math import hypot, pi


class CircleTest(unittest.TestCase):
    """Tests for the circle class"""
    def setUp(self):
        self.circle = Circle(5)

    def test_add_positive_area_to_circle(self):
        """Add two circles together"""
        new_circle = self.circle.add_area(Circle(10))
        self.assertEqual((hypot(10.5)**2) * pi, new_circle.get_area())
        new_circle = self.circle.add_area(Circle(42))
        self.assertEqual(hypot(42, 5), new_circle.get_radius())

    def test_add_zero_to_circle(self):
        """Add a circle with radius zero to the circle"""
        new_circle = self.circle.add_area(Circle(0))
        self.assertEqual(self.circle.get_radius(), new_circle.get_radius())
        self.assertEqual(self.circle.get_area(), new_circle.get_area())

    def test_create_negative_radius_circle(self):
        """Circle should raise ValueError if radius is less than zero"""
        with self.assertRaises(ValueError):
            new_circle = Circle(-1)
