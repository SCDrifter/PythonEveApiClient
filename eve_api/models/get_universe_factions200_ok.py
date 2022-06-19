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


class GetUniverseFactions200Ok(object):
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
        'corporation_id': 'int',
        'description': 'str',
        'faction_id': 'int',
        'is_unique': 'bool',
        'militia_corporation_id': 'int',
        'name': 'str',
        'size_factor': 'float',
        'solar_system_id': 'int',
        'station_count': 'int',
        'station_system_count': 'int'
    }

    attribute_map = {
        'corporation_id': 'corporation_id',
        'description': 'description',
        'faction_id': 'faction_id',
        'is_unique': 'is_unique',
        'militia_corporation_id': 'militia_corporation_id',
        'name': 'name',
        'size_factor': 'size_factor',
        'solar_system_id': 'solar_system_id',
        'station_count': 'station_count',
        'station_system_count': 'station_system_count'
    }

    def __init__(self, corporation_id=None, description=None, faction_id=None, is_unique=None, militia_corporation_id=None, name=None, size_factor=None, solar_system_id=None, station_count=None, station_system_count=None, _configuration=None):  # noqa: E501
        """GetUniverseFactions200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._corporation_id = None
        self._description = None
        self._faction_id = None
        self._is_unique = None
        self._militia_corporation_id = None
        self._name = None
        self._size_factor = None
        self._solar_system_id = None
        self._station_count = None
        self._station_system_count = None
        self.discriminator = None

        if corporation_id is not None:
            self.corporation_id = corporation_id
        self.description = description
        self.faction_id = faction_id
        self.is_unique = is_unique
        if militia_corporation_id is not None:
            self.militia_corporation_id = militia_corporation_id
        self.name = name
        self.size_factor = size_factor
        if solar_system_id is not None:
            self.solar_system_id = solar_system_id
        self.station_count = station_count
        self.station_system_count = station_system_count

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetUniverseFactions200Ok.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetUniverseFactions200Ok.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetUniverseFactions200Ok.  # noqa: E501
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def description(self):
        """Gets the description of this GetUniverseFactions200Ok.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetUniverseFactions200Ok.

        description string  # noqa: E501

        :param description: The description of this GetUniverseFactions200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def faction_id(self):
        """Gets the faction_id of this GetUniverseFactions200Ok.  # noqa: E501

        faction_id integer  # noqa: E501

        :return: The faction_id of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetUniverseFactions200Ok.

        faction_id integer  # noqa: E501

        :param faction_id: The faction_id of this GetUniverseFactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and faction_id is None:
            raise ValueError("Invalid value for `faction_id`, must not be `None`")  # noqa: E501

        self._faction_id = faction_id

    @property
    def is_unique(self):
        """Gets the is_unique of this GetUniverseFactions200Ok.  # noqa: E501

        is_unique boolean  # noqa: E501

        :return: The is_unique of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique):
        """Sets the is_unique of this GetUniverseFactions200Ok.

        is_unique boolean  # noqa: E501

        :param is_unique: The is_unique of this GetUniverseFactions200Ok.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_unique is None:
            raise ValueError("Invalid value for `is_unique`, must not be `None`")  # noqa: E501

        self._is_unique = is_unique

    @property
    def militia_corporation_id(self):
        """Gets the militia_corporation_id of this GetUniverseFactions200Ok.  # noqa: E501

        militia_corporation_id integer  # noqa: E501

        :return: The militia_corporation_id of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._militia_corporation_id

    @militia_corporation_id.setter
    def militia_corporation_id(self, militia_corporation_id):
        """Sets the militia_corporation_id of this GetUniverseFactions200Ok.

        militia_corporation_id integer  # noqa: E501

        :param militia_corporation_id: The militia_corporation_id of this GetUniverseFactions200Ok.  # noqa: E501
        :type: int
        """

        self._militia_corporation_id = militia_corporation_id

    @property
    def name(self):
        """Gets the name of this GetUniverseFactions200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseFactions200Ok.

        name string  # noqa: E501

        :param name: The name of this GetUniverseFactions200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size_factor(self):
        """Gets the size_factor of this GetUniverseFactions200Ok.  # noqa: E501

        size_factor number  # noqa: E501

        :return: The size_factor of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: float
        """
        return self._size_factor

    @size_factor.setter
    def size_factor(self, size_factor):
        """Sets the size_factor of this GetUniverseFactions200Ok.

        size_factor number  # noqa: E501

        :param size_factor: The size_factor of this GetUniverseFactions200Ok.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and size_factor is None:
            raise ValueError("Invalid value for `size_factor`, must not be `None`")  # noqa: E501

        self._size_factor = size_factor

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetUniverseFactions200Ok.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetUniverseFactions200Ok.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetUniverseFactions200Ok.  # noqa: E501
        :type: int
        """

        self._solar_system_id = solar_system_id

    @property
    def station_count(self):
        """Gets the station_count of this GetUniverseFactions200Ok.  # noqa: E501

        station_count integer  # noqa: E501

        :return: The station_count of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._station_count

    @station_count.setter
    def station_count(self, station_count):
        """Sets the station_count of this GetUniverseFactions200Ok.

        station_count integer  # noqa: E501

        :param station_count: The station_count of this GetUniverseFactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and station_count is None:
            raise ValueError("Invalid value for `station_count`, must not be `None`")  # noqa: E501

        self._station_count = station_count

    @property
    def station_system_count(self):
        """Gets the station_system_count of this GetUniverseFactions200Ok.  # noqa: E501

        station_system_count integer  # noqa: E501

        :return: The station_system_count of this GetUniverseFactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._station_system_count

    @station_system_count.setter
    def station_system_count(self, station_system_count):
        """Sets the station_system_count of this GetUniverseFactions200Ok.

        station_system_count integer  # noqa: E501

        :param station_system_count: The station_system_count of this GetUniverseFactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and station_system_count is None:
            raise ValueError("Invalid value for `station_system_count`, must not be `None`")  # noqa: E501

        self._station_system_count = station_system_count

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
        if issubclass(GetUniverseFactions200Ok, dict):
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
        if not isinstance(other, GetUniverseFactions200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseFactions200Ok):
            return True

        return self.to_dict() != other.to_dict()
