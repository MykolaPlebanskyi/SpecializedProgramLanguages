import unittest

import requests

from labwork_7.errors import Error


class Test(unittest.TestCase):

    def setUp(self):
        self.error = Error()

    def test_without_errors(self):
        urls = [
            "https://jsonplaceholder.org/users",
            "https://jsonplaceholder.org/posts",
            "https://jsonplaceholder.org/comments"
        ]

        for url in urls:
            with self.subTest(url=url):
                self.error.check_api_data(url)

    def test_with_errors(self):
        urls = [
            None,
            1234567689,
            "https://empty"
        ]

        for url in urls:
            with self.subTest(url=url):
                with self.assertRaises(requests.HTTPError):
                    self.error.check_api_data(url)
