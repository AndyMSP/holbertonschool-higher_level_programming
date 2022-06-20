#!/usr/bin/python3
"""Unit tests for Rectangle"""


import unittest
from models.rectangle import Rectangle


class Test_2(unittest.TestCase):
    """Unit tests for task 2"""
    def test_rect_instantiation(self):
        """Test that Rectangle object can be instantiated given various inputs"""
        Rectangle.reset()
        r1 = Rectangle(2, 3, 4, 5, 6)
        r2 = Rectangle(7, 8)
        self.assertAlmostEqual(r1.id, 6)
        self.assertAlmostEqual(r1.width, 2)
        self.assertAlmostEqual(r1.height, 3)
        self.assertAlmostEqual(r1.x, 4)
        self.assertAlmostEqual(r1.y, 5)
        self.assertAlmostEqual(r2.id, 1)
        self.assertAlmostEqual(r2.width, 7)
        self.assertAlmostEqual(r2.height, 8)
        self.assertAlmostEqual(r2.x, 0)
        self.assertAlmostEqual(r2.y, 0)

class Test_3(unittest.TestCase):
    """Unit tests for task 3"""
    def test_validate_input(self):
        """Test that bad input raises errors"""
        Rectangle.reset()
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(10, 'hello')
