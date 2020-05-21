# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.3.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCorporationsCorporationIdFwStatsOk(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enlisted_on': 'datetime',
        'faction_id': 'int',
        'kills': 'GetCorporationsCorporationIdFwStatsKills',
        'pilots': 'int',
        'victory_points': 'GetCorporationsCorporationIdFwStatsVictoryPoints'
    }

    attribute_map = {
        'enlisted_on': 'enlisted_on',
        'faction_id': 'faction_id',
        'kills': 'kills',
        'pilots': 'pilots',
        'victory_points': 'victory_points'
    }

    def __init__(self, enlisted_on=None, faction_id=None, kills=None, pilots=None, victory_points=None):  # noqa: E501
        """GetCorporationsCorporationIdFwStatsOk - a model defined in Swagger"""  # noqa: E501

        self._enlisted_on = None
        self._faction_id = None
        self._kills = None
        self._pilots = None
        self._victory_points = None
        self.discriminator = None

        if enlisted_on is not None:
            self.enlisted_on = enlisted_on
        if faction_id is not None:
            self.faction_id = faction_id
        self.kills = kills
        if pilots is not None:
            self.pilots = pilots
        self.victory_points = victory_points

    @property
    def enlisted_on(self):
        """Gets the enlisted_on of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501

        The enlistment date of the given corporation into faction warfare. Will not be included if corporation is not enlisted in faction warfare  # noqa: E501

        :return: The enlisted_on of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :rtype: datetime
        """
        return self._enlisted_on

    @enlisted_on.setter
    def enlisted_on(self, enlisted_on):
        """Sets the enlisted_on of this GetCorporationsCorporationIdFwStatsOk.

        The enlistment date of the given corporation into faction warfare. Will not be included if corporation is not enlisted in faction warfare  # noqa: E501

        :param enlisted_on: The enlisted_on of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :type: datetime
        """

        self._enlisted_on = enlisted_on

    @property
    def faction_id(self):
        """Gets the faction_id of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501

        The faction the given corporation is enlisted to fight for. Will not be included if corporation is not enlisted in faction warfare  # noqa: E501

        :return: The faction_id of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetCorporationsCorporationIdFwStatsOk.

        The faction the given corporation is enlisted to fight for. Will not be included if corporation is not enlisted in faction warfare  # noqa: E501

        :param faction_id: The faction_id of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :type: int
        """

        self._faction_id = faction_id

    @property
    def kills(self):
        """Gets the kills of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501


        :return: The kills of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :rtype: GetCorporationsCorporationIdFwStatsKills
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """Sets the kills of this GetCorporationsCorporationIdFwStatsOk.


        :param kills: The kills of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :type: GetCorporationsCorporationIdFwStatsKills
        """
        if kills is None:
            raise ValueError("Invalid value for `kills`, must not be `None`")  # noqa: E501

        self._kills = kills

    @property
    def pilots(self):
        """Gets the pilots of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501

        How many pilots the enlisted corporation has. Will not be included if corporation is not enlisted in faction warfare  # noqa: E501

        :return: The pilots of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :rtype: int
        """
        return self._pilots

    @pilots.setter
    def pilots(self, pilots):
        """Sets the pilots of this GetCorporationsCorporationIdFwStatsOk.

        How many pilots the enlisted corporation has. Will not be included if corporation is not enlisted in faction warfare  # noqa: E501

        :param pilots: The pilots of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :type: int
        """

        self._pilots = pilots

    @property
    def victory_points(self):
        """Gets the victory_points of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501


        :return: The victory_points of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :rtype: GetCorporationsCorporationIdFwStatsVictoryPoints
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """Sets the victory_points of this GetCorporationsCorporationIdFwStatsOk.


        :param victory_points: The victory_points of this GetCorporationsCorporationIdFwStatsOk.  # noqa: E501
        :type: GetCorporationsCorporationIdFwStatsVictoryPoints
        """
        if victory_points is None:
            raise ValueError("Invalid value for `victory_points`, must not be `None`")  # noqa: E501

        self._victory_points = victory_points

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetCorporationsCorporationIdFwStatsOk, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetCorporationsCorporationIdFwStatsOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
