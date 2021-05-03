# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetFwLeaderboardsCharactersYesterdayYesterday(object):
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
        'amount': 'int',
        'character_id': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'character_id': 'character_id'
    }

    def __init__(self, amount=None, character_id=None):  # noqa: E501
        """GetFwLeaderboardsCharactersYesterdayYesterday - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._character_id = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if character_id is not None:
            self.character_id = character_id

    @property
    def amount(self):
        """Gets the amount of this GetFwLeaderboardsCharactersYesterdayYesterday.  # noqa: E501

        Amount of kills  # noqa: E501

        :return: The amount of this GetFwLeaderboardsCharactersYesterdayYesterday.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetFwLeaderboardsCharactersYesterdayYesterday.

        Amount of kills  # noqa: E501

        :param amount: The amount of this GetFwLeaderboardsCharactersYesterdayYesterday.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def character_id(self):
        """Gets the character_id of this GetFwLeaderboardsCharactersYesterdayYesterday.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetFwLeaderboardsCharactersYesterdayYesterday.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetFwLeaderboardsCharactersYesterdayYesterday.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetFwLeaderboardsCharactersYesterdayYesterday.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

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
        if issubclass(GetFwLeaderboardsCharactersYesterdayYesterday, dict):
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
        if not isinstance(other, GetFwLeaderboardsCharactersYesterdayYesterday):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
