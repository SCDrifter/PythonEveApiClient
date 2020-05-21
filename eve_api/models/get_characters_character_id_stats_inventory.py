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


class GetCharactersCharacterIdStatsInventory(object):
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
        'abandon_loot_quantity': 'int',
        'trash_item_quantity': 'int'
    }

    attribute_map = {
        'abandon_loot_quantity': 'abandon_loot_quantity',
        'trash_item_quantity': 'trash_item_quantity'
    }

    def __init__(self, abandon_loot_quantity=None, trash_item_quantity=None):  # noqa: E501
        """GetCharactersCharacterIdStatsInventory - a model defined in Swagger"""  # noqa: E501

        self._abandon_loot_quantity = None
        self._trash_item_quantity = None
        self.discriminator = None

        if abandon_loot_quantity is not None:
            self.abandon_loot_quantity = abandon_loot_quantity
        if trash_item_quantity is not None:
            self.trash_item_quantity = trash_item_quantity

    @property
    def abandon_loot_quantity(self):
        """Gets the abandon_loot_quantity of this GetCharactersCharacterIdStatsInventory.  # noqa: E501

        abandon_loot_quantity integer  # noqa: E501

        :return: The abandon_loot_quantity of this GetCharactersCharacterIdStatsInventory.  # noqa: E501
        :rtype: int
        """
        return self._abandon_loot_quantity

    @abandon_loot_quantity.setter
    def abandon_loot_quantity(self, abandon_loot_quantity):
        """Sets the abandon_loot_quantity of this GetCharactersCharacterIdStatsInventory.

        abandon_loot_quantity integer  # noqa: E501

        :param abandon_loot_quantity: The abandon_loot_quantity of this GetCharactersCharacterIdStatsInventory.  # noqa: E501
        :type: int
        """

        self._abandon_loot_quantity = abandon_loot_quantity

    @property
    def trash_item_quantity(self):
        """Gets the trash_item_quantity of this GetCharactersCharacterIdStatsInventory.  # noqa: E501

        trash_item_quantity integer  # noqa: E501

        :return: The trash_item_quantity of this GetCharactersCharacterIdStatsInventory.  # noqa: E501
        :rtype: int
        """
        return self._trash_item_quantity

    @trash_item_quantity.setter
    def trash_item_quantity(self, trash_item_quantity):
        """Sets the trash_item_quantity of this GetCharactersCharacterIdStatsInventory.

        trash_item_quantity integer  # noqa: E501

        :param trash_item_quantity: The trash_item_quantity of this GetCharactersCharacterIdStatsInventory.  # noqa: E501
        :type: int
        """

        self._trash_item_quantity = trash_item_quantity

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
        if issubclass(GetCharactersCharacterIdStatsInventory, dict):
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
        if not isinstance(other, GetCharactersCharacterIdStatsInventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other