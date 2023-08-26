#!/usr/bin/env python3
"""Testing access_nested_map"""


from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """ Testing accessible_neted_map"""
    @parameterized.expand([

        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """testing access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """ testing access_nested_map exception"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)
