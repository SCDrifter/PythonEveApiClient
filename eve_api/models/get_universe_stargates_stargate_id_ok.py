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


class GetUniverseStargatesStargateIdOk(object):
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
        'destination': 'GetUniverseStargatesStargateIdDestination',
        'name': 'str',
        'position': 'GetUniverseStargatesStargateIdPosition',
        'stargate_id': 'int',
        'system_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'destination': 'destination',
        'name': 'name',
        'position': 'position',
        'stargate_id': 'stargate_id',
        'system_id': 'system_id',
        'type_id': 'type_id'
    }

    def __init__(self, destination=None, name=None, position=None, stargate_id=None, system_id=None, type_id=None, _configuration=None):  # noqa: E501
        """GetUniverseStargatesStargateIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination = None
        self._name = None
        self._position = None
        self._stargate_id = None
        self._system_id = None
        self._type_id = None
        self.discriminator = None

        self.destination = destination
        self.name = name
        self.position = position
        self.stargate_id = stargate_id
        self.system_id = system_id
        self.type_id = type_id

    @property
    def destination(self):
        """Gets the destination of this GetUniverseStargatesStargateIdOk.  # noqa: E501


        :return: The destination of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: GetUniverseStargatesStargateIdDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this GetUniverseStargatesStargateIdOk.


        :param destination: The destination of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: GetUniverseStargatesStargateIdDestination
        """
        if self._configuration.client_side_validation and destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def name(self):
        """Gets the name of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseStargatesStargateIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def position(self):
        """Gets the position of this GetUniverseStargatesStargateIdOk.  # noqa: E501


        :return: The position of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: GetUniverseStargatesStargateIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GetUniverseStargatesStargateIdOk.


        :param position: The position of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: GetUniverseStargatesStargateIdPosition
        """
        if self._configuration.client_side_validation and position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def stargate_id(self):
        """Gets the stargate_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        stargate_id integer  # noqa: E501

        :return: The stargate_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: int
        """
        return self._stargate_id

    @stargate_id.setter
    def stargate_id(self, stargate_id):
        """Sets the stargate_id of this GetUniverseStargatesStargateIdOk.

        stargate_id integer  # noqa: E501

        :param stargate_id: The stargate_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and stargate_id is None:
            raise ValueError("Invalid value for `stargate_id`, must not be `None`")  # noqa: E501

        self._stargate_id = stargate_id

    @property
    def system_id(self):
        """Gets the system_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        The solar system this stargate is in  # noqa: E501

        :return: The system_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetUniverseStargatesStargateIdOk.

        The solar system this stargate is in  # noqa: E501

        :param system_id: The system_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetUniverseStargatesStargateIdOk.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type_id is None:
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
        if issubclass(GetUniverseStargatesStargateIdOk, dict):
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
        if not isinstance(other, GetUniverseStargatesStargateIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseStargatesStargateIdOk):
            return True

        return self.to_dict() != other.to_dict()
