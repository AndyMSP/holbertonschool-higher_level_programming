#!/usr/bin/python3
"""Unit tests for base"""


import unittest
from models.base import Base


class Test_1(unittest.TestCase):
    """Unit tests for task 1"""
    def test_id_without_input(self):
        """Test that id is properly generated without input"""
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
    def test_id_with_input(self):
        b3 = Base(10)
        self.assertAlmostEqual(b3.id, 10)
