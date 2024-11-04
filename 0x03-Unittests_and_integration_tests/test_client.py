#!/usr/bin/env python3
"""Test for client file"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """"Test for the GithubOrgClient class"""
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test for the org method"""
        client = GithubOrgClient(org_name)
        result = client.org

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        self.assertEqual(result, {"login": "mocked_org"})

    def test_public_repos_url(self):
        """Tests methods public_repos_url"""
        mocked_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }
        with patch.object(
            GithubOrgClient, 'org',
            new_callable=PropertyMock,
            return_value=mocked_payload
        ):
            client = GithubOrgClient("test_org")

            result = client._public_repos_url

            self.assertEqual(
                result, "https://api.github.com/orgs/test_org/repos"
            )
