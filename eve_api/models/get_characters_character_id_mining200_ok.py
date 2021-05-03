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


class GetCharactersCharacterIdMining200Ok(object):
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
        '_date': 'date',
        'quantity': 'int',
        'solar_system_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'quantity': 'quantity',
        'solar_system_id': 'solar_system_id',
        'type_id': 'type_id'
    }

    def __init__(self, _date=None, quantity=None, solar_system_id=None, type_id=None):  # noqa: E501
        """GetCharactersCharacterIdMining200Ok - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._quantity = None
        self._solar_system_id = None
        self._type_id = None
        self.discriminator = None

        self._date = _date
        self.quantity = quantity
        self.solar_system_id = solar_system_id
        self.type_id = type_id

    @property
    def _date(self):
        """Gets the _date of this GetCharactersCharacterIdMining200Ok.  # noqa: E501

        date string  # noqa: E501

        :return: The _date of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetCharactersCharacterIdMining200Ok.

        date string  # noqa: E501

        :param _date: The _date of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def quantity(self):
        """Gets the quantity of this GetCharactersCharacterIdMining200Ok.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCharactersCharacterIdMining200Ok.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetCharactersCharacterIdMining200Ok.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetCharactersCharacterIdMining200Ok.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCharactersCharacterIdMining200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCharactersCharacterIdMining200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCharactersCharacterIdMining200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

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
        if issubclass(GetCharactersCharacterIdMining200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdMining200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
