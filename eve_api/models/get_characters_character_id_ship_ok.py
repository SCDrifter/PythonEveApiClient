# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCharactersCharacterIdShipOk(object):
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
        'ship_item_id': 'int',
        'ship_name': 'str',
        'ship_type_id': 'int'
    }

    attribute_map = {
        'ship_item_id': 'ship_item_id',
        'ship_name': 'ship_name',
        'ship_type_id': 'ship_type_id'
    }

    def __init__(self, ship_item_id=None, ship_name=None, ship_type_id=None):  # noqa: E501
        """GetCharactersCharacterIdShipOk - a model defined in Swagger"""  # noqa: E501

        self._ship_item_id = None
        self._ship_name = None
        self._ship_type_id = None
        self.discriminator = None

        self.ship_item_id = ship_item_id
        self.ship_name = ship_name
        self.ship_type_id = ship_type_id

    @property
    def ship_item_id(self):
        """Gets the ship_item_id of this GetCharactersCharacterIdShipOk.  # noqa: E501

        Item id's are unique to a ship and persist until it is repackaged. This value can be used to track repeated uses of a ship, or detect when a pilot changes into a different instance of the same ship type.  # noqa: E501

        :return: The ship_item_id of this GetCharactersCharacterIdShipOk.  # noqa: E501
        :rtype: int
        """
        return self._ship_item_id

    @ship_item_id.setter
    def ship_item_id(self, ship_item_id):
        """Sets the ship_item_id of this GetCharactersCharacterIdShipOk.

        Item id's are unique to a ship and persist until it is repackaged. This value can be used to track repeated uses of a ship, or detect when a pilot changes into a different instance of the same ship type.  # noqa: E501

        :param ship_item_id: The ship_item_id of this GetCharactersCharacterIdShipOk.  # noqa: E501
        :type: int
        """
        if ship_item_id is None:
            raise ValueError("Invalid value for `ship_item_id`, must not be `None`")  # noqa: E501

        self._ship_item_id = ship_item_id

    @property
    def ship_name(self):
        """Gets the ship_name of this GetCharactersCharacterIdShipOk.  # noqa: E501

        ship_name string  # noqa: E501

        :return: The ship_name of this GetCharactersCharacterIdShipOk.  # noqa: E501
        :rtype: str
        """
        return self._ship_name

    @ship_name.setter
    def ship_name(self, ship_name):
        """Sets the ship_name of this GetCharactersCharacterIdShipOk.

        ship_name string  # noqa: E501

        :param ship_name: The ship_name of this GetCharactersCharacterIdShipOk.  # noqa: E501
        :type: str
        """
        if ship_name is None:
            raise ValueError("Invalid value for `ship_name`, must not be `None`")  # noqa: E501

        self._ship_name = ship_name

    @property
    def ship_type_id(self):
        """Gets the ship_type_id of this GetCharactersCharacterIdShipOk.  # noqa: E501

        ship_type_id integer  # noqa: E501

        :return: The ship_type_id of this GetCharactersCharacterIdShipOk.  # noqa: E501
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """Sets the ship_type_id of this GetCharactersCharacterIdShipOk.

        ship_type_id integer  # noqa: E501

        :param ship_type_id: The ship_type_id of this GetCharactersCharacterIdShipOk.  # noqa: E501
        :type: int
        """
        if ship_type_id is None:
            raise ValueError("Invalid value for `ship_type_id`, must not be `None`")  # noqa: E501

        self._ship_type_id = ship_type_id

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
        if issubclass(GetCharactersCharacterIdShipOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdShipOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
