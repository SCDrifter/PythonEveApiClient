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


class GetWarsWarIdDefender(object):
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
        'alliance_id': 'int',
        'corporation_id': 'int',
        'isk_destroyed': 'float',
        'ships_killed': 'int'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'corporation_id': 'corporation_id',
        'isk_destroyed': 'isk_destroyed',
        'ships_killed': 'ships_killed'
    }

    def __init__(self, alliance_id=None, corporation_id=None, isk_destroyed=None, ships_killed=None, _configuration=None):  # noqa: E501
        """GetWarsWarIdDefender - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alliance_id = None
        self._corporation_id = None
        self._isk_destroyed = None
        self._ships_killed = None
        self.discriminator = None

        if alliance_id is not None:
            self.alliance_id = alliance_id
        if corporation_id is not None:
            self.corporation_id = corporation_id
        self.isk_destroyed = isk_destroyed
        self.ships_killed = ships_killed

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetWarsWarIdDefender.  # noqa: E501

        Alliance ID if and only if the defender is an alliance  # noqa: E501

        :return: The alliance_id of this GetWarsWarIdDefender.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetWarsWarIdDefender.

        Alliance ID if and only if the defender is an alliance  # noqa: E501

        :param alliance_id: The alliance_id of this GetWarsWarIdDefender.  # noqa: E501
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetWarsWarIdDefender.  # noqa: E501

        Corporation ID if and only if the defender is a corporation  # noqa: E501

        :return: The corporation_id of this GetWarsWarIdDefender.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetWarsWarIdDefender.

        Corporation ID if and only if the defender is a corporation  # noqa: E501

        :param corporation_id: The corporation_id of this GetWarsWarIdDefender.  # noqa: E501
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def isk_destroyed(self):
        """Gets the isk_destroyed of this GetWarsWarIdDefender.  # noqa: E501

        ISK value of ships the defender has killed  # noqa: E501

        :return: The isk_destroyed of this GetWarsWarIdDefender.  # noqa: E501
        :rtype: float
        """
        return self._isk_destroyed

    @isk_destroyed.setter
    def isk_destroyed(self, isk_destroyed):
        """Sets the isk_destroyed of this GetWarsWarIdDefender.

        ISK value of ships the defender has killed  # noqa: E501

        :param isk_destroyed: The isk_destroyed of this GetWarsWarIdDefender.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and isk_destroyed is None:
            raise ValueError("Invalid value for `isk_destroyed`, must not be `None`")  # noqa: E501

        self._isk_destroyed = isk_destroyed

    @property
    def ships_killed(self):
        """Gets the ships_killed of this GetWarsWarIdDefender.  # noqa: E501

        The number of ships the defender has killed  # noqa: E501

        :return: The ships_killed of this GetWarsWarIdDefender.  # noqa: E501
        :rtype: int
        """
        return self._ships_killed

    @ships_killed.setter
    def ships_killed(self, ships_killed):
        """Sets the ships_killed of this GetWarsWarIdDefender.

        The number of ships the defender has killed  # noqa: E501

        :param ships_killed: The ships_killed of this GetWarsWarIdDefender.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ships_killed is None:
            raise ValueError("Invalid value for `ships_killed`, must not be `None`")  # noqa: E501

        self._ships_killed = ships_killed

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
        if issubclass(GetWarsWarIdDefender, dict):
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
        if not isinstance(other, GetWarsWarIdDefender):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetWarsWarIdDefender):
            return True

        return self.to_dict() != other.to_dict()
