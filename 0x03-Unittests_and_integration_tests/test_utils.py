#!/usr/bin/env python3
"""Testing for file utils.py"""


from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test function for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), "'{}'".format(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            response = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)
