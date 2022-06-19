#!/usr/bin/env python3
"""Unit tests for base"""


import unittest
from models.base import Base


class Test_1(unittest.TestCase):
    """Unit tests for task 1"""
    def test_id(self):
        """Test that id is properly generated"""
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base(10)
        self.assertAlmostEqual(b3.id, 10)
