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


class GetUniversePlanetsPlanetIdOk(object):
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
        'name': 'str',
        'planet_id': 'int',
        'position': 'GetUniversePlanetsPlanetIdPosition',
        'system_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'planet_id': 'planet_id',
        'position': 'position',
        'system_id': 'system_id',
        'type_id': 'type_id'
    }

    def __init__(self, name=None, planet_id=None, position=None, system_id=None, type_id=None):  # noqa: E501
        """GetUniversePlanetsPlanetIdOk - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._planet_id = None
        self._position = None
        self._system_id = None
        self._type_id = None
        self.discriminator = None

        self.name = name
        self.planet_id = planet_id
        self.position = position
        self.system_id = system_id
        self.type_id = type_id

    @property
    def name(self):
        """Gets the name of this GetUniversePlanetsPlanetIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniversePlanetsPlanetIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def planet_id(self):
        """Gets the planet_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501

        planet_id integer  # noqa: E501

        :return: The planet_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """Sets the planet_id of this GetUniversePlanetsPlanetIdOk.

        planet_id integer  # noqa: E501

        :param planet_id: The planet_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :type: int
        """
        if planet_id is None:
            raise ValueError("Invalid value for `planet_id`, must not be `None`")  # noqa: E501

        self._planet_id = planet_id

    @property
    def position(self):
        """Gets the position of this GetUniversePlanetsPlanetIdOk.  # noqa: E501


        :return: The position of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :rtype: GetUniversePlanetsPlanetIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GetUniversePlanetsPlanetIdOk.


        :param position: The position of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :type: GetUniversePlanetsPlanetIdPosition
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def system_id(self):
        """Gets the system_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501

        The solar system this planet is in  # noqa: E501

        :return: The system_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetUniversePlanetsPlanetIdOk.

        The solar system this planet is in  # noqa: E501

        :param system_id: The system_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetUniversePlanetsPlanetIdOk.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetUniversePlanetsPlanetIdOk.  # noqa: E501
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
        if issubclass(GetUniversePlanetsPlanetIdOk, dict):
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
        if not isinstance(other, GetUniversePlanetsPlanetIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
