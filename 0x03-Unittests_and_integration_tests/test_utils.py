#!/usr/bin/env python3
"""Testing access_nested_map"""


from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """ testing get json with a mock request """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_requests_get.return_value = mock_response

        data = get_json(test_url)

        self.assertEqual(data, test_payload)

        mock_requests_get.assert_called_once_with(test_url)
