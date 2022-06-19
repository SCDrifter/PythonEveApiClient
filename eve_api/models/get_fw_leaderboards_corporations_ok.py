# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from eve_api.configuration import Configuration


class GetFwLeaderboardsCorporationsOk(object):
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
        'kills': 'GetFwLeaderboardsCorporationsKills',
        'victory_points': 'GetFwLeaderboardsCorporationsVictoryPoints'
    }

    attribute_map = {
        'kills': 'kills',
        'victory_points': 'victory_points'
    }

    def __init__(self, kills=None, victory_points=None, _configuration=None):  # noqa: E501
        """GetFwLeaderboardsCorporationsOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._kills = None
        self._victory_points = None
        self.discriminator = None

        self.kills = kills
        self.victory_points = victory_points

    @property
    def kills(self):
        """Gets the kills of this GetFwLeaderboardsCorporationsOk.  # noqa: E501


        :return: The kills of this GetFwLeaderboardsCorporationsOk.  # noqa: E501
        :rtype: GetFwLeaderboardsCorporationsKills
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """Sets the kills of this GetFwLeaderboardsCorporationsOk.


        :param kills: The kills of this GetFwLeaderboardsCorporationsOk.  # noqa: E501
        :type: GetFwLeaderboardsCorporationsKills
        """
        if self._configuration.client_side_validation and kills is None:
            raise ValueError("Invalid value for `kills`, must not be `None`")  # noqa: E501

        self._kills = kills

    @property
    def victory_points(self):
        """Gets the victory_points of this GetFwLeaderboardsCorporationsOk.  # noqa: E501


        :return: The victory_points of this GetFwLeaderboardsCorporationsOk.  # noqa: E501
        :rtype: GetFwLeaderboardsCorporationsVictoryPoints
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """Sets the victory_points of this GetFwLeaderboardsCorporationsOk.


        :param victory_points: The victory_points of this GetFwLeaderboardsCorporationsOk.  # noqa: E501
        :type: GetFwLeaderboardsCorporationsVictoryPoints
        """
        if self._configuration.client_side_validation and victory_points is None:
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
        if issubclass(GetFwLeaderboardsCorporationsOk, dict):
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
        if not isinstance(other, GetFwLeaderboardsCorporationsOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFwLeaderboardsCorporationsOk):
            return True

        return self.to_dict() != other.to_dict()
