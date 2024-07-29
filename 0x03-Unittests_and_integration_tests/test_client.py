#!/usr/bin/env python3
"""Test file for client.py"""

import unittest.mock
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


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

    def test_public_repos_url(self):
        """Test Method for GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': "https://example.com"}
            org = GithubOrgClient('abc')

            actual_result = org._public_repos_url
            self.assertEqual(actual_result, "https://example.com")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock):
        """Test Method for GithubOrgClient.public_repos"""
        mock_get_json.return_value = [
            {'name': 'Real life'},
            {'name': 'Fake life'}
        ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = 'https://example.com'
            org = GithubOrgClient('abc')

            actual_result = org.public_repos()
            self.assertEqual(actual_result, ['Real life', 'Fake life'])
            mock_get_json.assert_called_once()
            mock_repos.assert_called_once()

    @parameterized.expand([
        ('case1', {
            'input1': {'license': {'key': 'my_license'}},
            'input2': 'my_license',
            'expected': True,
        }),
        ('case2', {
            'input1': {"license": {"key": "other_license"}},
            'input2': "my_license",
            'expected': False,
        })
    ])
    def test_has_license(self, name, test_data):
        """Test Method to test GithubOrgClient.has_license"""
        actual_result = GithubOrgClient.has_license(
            test_data['input1'],
            test_data['input2'],
        )
        self.assertEqual(actual_result, test_data['expected'])
