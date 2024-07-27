#!/usr/bin/env python3
"""Test file for utils"""

import unittest.mock
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Test utils.access_nested_map class"""

    @parameterized.expand([
        (
            "test1",
            {'a': 1},
            ('a',),
            1
        ),
        (
            'test2',
            {'a': {'b': 2}},
            ('a',),
            {'b': 2}
        ),
        (
            'test3',
            {'a': {'b': 2}},
            ('a', 'b'),
            2
        )
    ])
    def test_access_nested_map(self, name, input1, input2, expected) -> None:
        """Test utils.access_nested_map method"""
        self.assertEqual(utils.access_nested_map(input1, input2), expected)

    @parameterized.expand([
        ('test1', {}, ('a',), KeyError),
        ('test2', {'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, name, input1,
                                         input2,
                                         expected) -> None:
        """Test utils.access_nested_map_exception method"""
        with self.assertRaises(KeyError, msg=f"KeyError: '{input2}'"):
            utils.access_nested_map(input1, input2)


class TestGetJson(unittest.TestCase):
    """Test utils.get_json class"""

    @parameterized.expand([
        ('test1', 'http://example.com', {"payload": True}),
        ('test2', 'http://holberton.io', {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, name, input, expected, mock_get: Mock) -> None:
        """Test utils.get_json method"""
        mock_response: Mock = unittest.mock.Mock()
        mock_response.json.return_value = expected

        mock_get.return_value = mock_response

        actual_result = utils.get_json(input)

        self.assertEqual(actual_result, expected)

        mock_get.assert_called_once_with(input)


if __name__ == '__main__':
    unittest.main()
