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
from eve_api.api.faction_warfare_api import FactionWarfareApi  # noqa: E501
from eve_api.rest import ApiException


class TestFactionWarfareApi(unittest.TestCase):
    """FactionWarfareApi unit test stubs"""

    def setUp(self):
        self.api = eve_api.api.faction_warfare_api.FactionWarfareApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id_fw_stats(self):
        """Test case for get_characters_character_id_fw_stats

        Overview of a character involved in faction warfare  # noqa: E501
        """
        pass

    def test_get_corporations_corporation_id_fw_stats(self):
        """Test case for get_corporations_corporation_id_fw_stats

        Overview of a corporation involved in faction warfare  # noqa: E501
        """
        pass

    def test_get_fw_leaderboards(self):
        """Test case for get_fw_leaderboards

        List of the top factions in faction warfare  # noqa: E501
        """
        pass

    def test_get_fw_leaderboards_characters(self):
        """Test case for get_fw_leaderboards_characters

        List of the top pilots in faction warfare  # noqa: E501
        """
        pass

    def test_get_fw_leaderboards_corporations(self):
        """Test case for get_fw_leaderboards_corporations

        List of the top corporations in faction warfare  # noqa: E501
        """
        pass

    def test_get_fw_stats(self):
        """Test case for get_fw_stats

        An overview of statistics about factions involved in faction warfare  # noqa: E501
        """
        pass

    def test_get_fw_systems(self):
        """Test case for get_fw_systems

        Ownership of faction warfare systems  # noqa: E501
        """
        pass

    def test_get_fw_wars(self):
        """Test case for get_fw_wars

        Data about which NPC factions are at war  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
