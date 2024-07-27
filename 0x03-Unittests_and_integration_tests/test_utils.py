#!/usr/bin/env python3
"""Test file for utils"""

from parameterized import parameterized
import unittest
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


if __name__ == '__main__':
    unittest.main()
