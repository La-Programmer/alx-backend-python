#!/usr/bin/env python3
"""Test file for client.py"""

import unittest.mock
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
import json


class TestGithubOrgClient(unittest.TestCase):
    """Test Class for GithubOrgClient class"""
    @parameterized.expand([
        ('case1', {"input": 'google', "expected": {
            'login': 'google',
        }}),
        ('case2', {"input": 'abc', 'expected': {
            'message': 'Not Found',
            'status': '404'
        }})
    ])
    @patch('client.get_json')
    def test_org(self, name, test_data, mock_get: Mock):
        """Test Method for GithubOrgClient.org"""
        mock_get.return_value = test_data['expected']

        org = GithubOrgClient(test_data['input'])
        actual_result = org.org
        self.assertEqual(actual_result, test_data['expected'])
        arg = f"https://api.github.com/orgs/{test_data['input']}"
        mock_get.assert_called_once_with(arg)
