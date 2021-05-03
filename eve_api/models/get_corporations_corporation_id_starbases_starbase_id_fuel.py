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


class GetCorporationsCorporationIdStarbasesStarbaseIdFuel(object):
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
        'quantity': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'quantity': 'quantity',
        'type_id': 'type_id'
    }

    def __init__(self, quantity=None, type_id=None):  # noqa: E501
        """GetCorporationsCorporationIdStarbasesStarbaseIdFuel - a model defined in Swagger"""  # noqa: E501

        self._quantity = None
        self._type_id = None
        self.discriminator = None

        self.quantity = quantity
        self.type_id = type_id

    @property
    def quantity(self):
        """Gets the quantity of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdStarbasesStarbaseIdFuel.  # noqa: E501
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
        if issubclass(GetCorporationsCorporationIdStarbasesStarbaseIdFuel, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdStarbasesStarbaseIdFuel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
