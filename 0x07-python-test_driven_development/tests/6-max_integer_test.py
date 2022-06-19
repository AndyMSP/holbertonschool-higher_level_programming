#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class to test max_integer function"""
    def test_answer(self):
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
