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


class GetUniverseSystemJumps200Ok(object):
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
        'ship_jumps': 'int',
        'system_id': 'int'
    }

    attribute_map = {
        'ship_jumps': 'ship_jumps',
        'system_id': 'system_id'
    }

    def __init__(self, ship_jumps=None, system_id=None):  # noqa: E501
        """GetUniverseSystemJumps200Ok - a model defined in Swagger"""  # noqa: E501

        self._ship_jumps = None
        self._system_id = None
        self.discriminator = None

        self.ship_jumps = ship_jumps
        self.system_id = system_id

    @property
    def ship_jumps(self):
        """Gets the ship_jumps of this GetUniverseSystemJumps200Ok.  # noqa: E501

        ship_jumps integer  # noqa: E501

        :return: The ship_jumps of this GetUniverseSystemJumps200Ok.  # noqa: E501
        :rtype: int
        """
        return self._ship_jumps

    @ship_jumps.setter
    def ship_jumps(self, ship_jumps):
        """Sets the ship_jumps of this GetUniverseSystemJumps200Ok.

        ship_jumps integer  # noqa: E501

        :param ship_jumps: The ship_jumps of this GetUniverseSystemJumps200Ok.  # noqa: E501
        :type: int
        """
        if ship_jumps is None:
            raise ValueError("Invalid value for `ship_jumps`, must not be `None`")  # noqa: E501

        self._ship_jumps = ship_jumps

    @property
    def system_id(self):
        """Gets the system_id of this GetUniverseSystemJumps200Ok.  # noqa: E501

        system_id integer  # noqa: E501

        :return: The system_id of this GetUniverseSystemJumps200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetUniverseSystemJumps200Ok.

        system_id integer  # noqa: E501

        :param system_id: The system_id of this GetUniverseSystemJumps200Ok.  # noqa: E501
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

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
        if issubclass(GetUniverseSystemJumps200Ok, dict):
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
        if not isinstance(other, GetUniverseSystemJumps200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
