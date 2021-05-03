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


class GetFwWars200Ok(object):
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
        'against_id': 'int',
        'faction_id': 'int'
    }

    attribute_map = {
        'against_id': 'against_id',
        'faction_id': 'faction_id'
    }

    def __init__(self, against_id=None, faction_id=None):  # noqa: E501
        """GetFwWars200Ok - a model defined in Swagger"""  # noqa: E501

        self._against_id = None
        self._faction_id = None
        self.discriminator = None

        self.against_id = against_id
        self.faction_id = faction_id

    @property
    def against_id(self):
        """Gets the against_id of this GetFwWars200Ok.  # noqa: E501

        The faction ID of the enemy faction.  # noqa: E501

        :return: The against_id of this GetFwWars200Ok.  # noqa: E501
        :rtype: int
        """
        return self._against_id

    @against_id.setter
    def against_id(self, against_id):
        """Sets the against_id of this GetFwWars200Ok.

        The faction ID of the enemy faction.  # noqa: E501

        :param against_id: The against_id of this GetFwWars200Ok.  # noqa: E501
        :type: int
        """
        if against_id is None:
            raise ValueError("Invalid value for `against_id`, must not be `None`")  # noqa: E501

        self._against_id = against_id

    @property
    def faction_id(self):
        """Gets the faction_id of this GetFwWars200Ok.  # noqa: E501

        faction_id integer  # noqa: E501

        :return: The faction_id of this GetFwWars200Ok.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetFwWars200Ok.

        faction_id integer  # noqa: E501

        :param faction_id: The faction_id of this GetFwWars200Ok.  # noqa: E501
        :type: int
        """
        if faction_id is None:
            raise ValueError("Invalid value for `faction_id`, must not be `None`")  # noqa: E501

        self._faction_id = faction_id

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
        if issubclass(GetFwWars200Ok, dict):
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
        if not isinstance(other, GetFwWars200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
