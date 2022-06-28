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
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r2 = Rectangle(10, 2)
            r2.width = -10
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r3 = Rectangle(1, 2)
            r3.x = {}
        self.assertAlmostEqual(r3.id, 2)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r4 = Rectangle('hi', 6)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r5 = Rectangle(6, 7, 'hey')
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r6 = Rectangle(6, 7, 8, 'howdy')
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r7 = Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r8 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r9 = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r10 = Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r11 = Rectangle(1, 2, 3, -4)
