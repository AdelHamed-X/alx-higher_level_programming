#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEquals(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [2, 4, 3, 7]
        self.assertEquals(max_integer(unordered), 7)

    def test_max_at_beginning(self):
        """Test an unordered list of integers."""
        max_at_beginning = [7, 4, 3, 2]
        self.assertEquals(max_integer(max_at_beginning), 7)

    def test_list_negative(self):
        """Test a list with a negative number."""
        list_neg = [-1, -2, -3, -4]
        self.assertEquals(max_integer(list_neg), -1)

    def test_empty_list(self):
        empty_list = []
        self.assertEquals(max_integer(empty_list), None)

    def test_one_element(self):
        one_element = [1]
        self.assertEquals(max_integer(one_element), 1)
