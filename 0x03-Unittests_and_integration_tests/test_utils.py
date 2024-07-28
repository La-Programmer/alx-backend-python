#!/usr/bin/env python3
"""Test file for utils"""

import unittest.mock
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
import utils
from utils import memoize


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


class TestMemoize(unittest.TestCase):
    """Test utils.memoize class"""
    def test_memoize(self) -> int:
        """Test utils.memoize method"""
        class TestClass:
            """Test Class for utils.memoize"""

            def a_method(self) -> int:
                """Return an integer"""
                return 42

            @memoize
            def a_property(self) -> int:
                """Return an integer"""
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42

            test_obj = TestClass()
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
