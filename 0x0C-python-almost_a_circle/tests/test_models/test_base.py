#!/usr/bin/python3
"""
Unit test for class Base
"""
import unittest
import sys

Base = sys.path.append('/models/base.py')


class TestBase_Init(unittest.TestCase):
    """
    unittest for testing Base class
    """
    def test_init(self):
        b1 = Base()


