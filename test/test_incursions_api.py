# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.3.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import eve_api
from eve_api.api.incursions_api import IncursionsApi  # noqa: E501
from eve_api.rest import ApiException


class TestIncursionsApi(unittest.TestCase):
    """IncursionsApi unit test stubs"""

    def setUp(self):
        self.api = eve_api.api.incursions_api.IncursionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_incursions(self):
        """Test case for get_incursions

        List incursions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
