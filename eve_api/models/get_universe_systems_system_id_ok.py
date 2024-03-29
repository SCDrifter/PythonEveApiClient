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


class GetUniverseSystemsSystemIdOk(object):
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
        'constellation_id': 'int',
        'name': 'str',
        'planets': 'list[GetUniverseSystemsSystemIdPlanet]',
        'position': 'GetUniverseSystemsSystemIdPosition',
        'security_class': 'str',
        'security_status': 'float',
        'star_id': 'int',
        'stargates': 'list[int]',
        'stations': 'list[int]',
        'system_id': 'int'
    }

    attribute_map = {
        'constellation_id': 'constellation_id',
        'name': 'name',
        'planets': 'planets',
        'position': 'position',
        'security_class': 'security_class',
        'security_status': 'security_status',
        'star_id': 'star_id',
        'stargates': 'stargates',
        'stations': 'stations',
        'system_id': 'system_id'
    }

    def __init__(self, constellation_id=None, name=None, planets=None, position=None, security_class=None, security_status=None, star_id=None, stargates=None, stations=None, system_id=None, _configuration=None):  # noqa: E501
        """GetUniverseSystemsSystemIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._constellation_id = None
        self._name = None
        self._planets = None
        self._position = None
        self._security_class = None
        self._security_status = None
        self._star_id = None
        self._stargates = None
        self._stations = None
        self._system_id = None
        self.discriminator = None

        self.constellation_id = constellation_id
        self.name = name
        if planets is not None:
            self.planets = planets
        self.position = position
        if security_class is not None:
            self.security_class = security_class
        self.security_status = security_status
        if star_id is not None:
            self.star_id = star_id
        if stargates is not None:
            self.stargates = stargates
        if stations is not None:
            self.stations = stations
        self.system_id = system_id

    @property
    def constellation_id(self):
        """Gets the constellation_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        The constellation this solar system is in  # noqa: E501

        :return: The constellation_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: int
        """
        return self._constellation_id

    @constellation_id.setter
    def constellation_id(self, constellation_id):
        """Sets the constellation_id of this GetUniverseSystemsSystemIdOk.

        The constellation this solar system is in  # noqa: E501

        :param constellation_id: The constellation_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and constellation_id is None:
            raise ValueError("Invalid value for `constellation_id`, must not be `None`")  # noqa: E501

        self._constellation_id = constellation_id

    @property
    def name(self):
        """Gets the name of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseSystemsSystemIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def planets(self):
        """Gets the planets of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        planets array  # noqa: E501

        :return: The planets of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: list[GetUniverseSystemsSystemIdPlanet]
        """
        return self._planets

    @planets.setter
    def planets(self, planets):
        """Sets the planets of this GetUniverseSystemsSystemIdOk.

        planets array  # noqa: E501

        :param planets: The planets of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: list[GetUniverseSystemsSystemIdPlanet]
        """

        self._planets = planets

    @property
    def position(self):
        """Gets the position of this GetUniverseSystemsSystemIdOk.  # noqa: E501


        :return: The position of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: GetUniverseSystemsSystemIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GetUniverseSystemsSystemIdOk.


        :param position: The position of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: GetUniverseSystemsSystemIdPosition
        """
        if self._configuration.client_side_validation and position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def security_class(self):
        """Gets the security_class of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        security_class string  # noqa: E501

        :return: The security_class of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: str
        """
        return self._security_class

    @security_class.setter
    def security_class(self, security_class):
        """Sets the security_class of this GetUniverseSystemsSystemIdOk.

        security_class string  # noqa: E501

        :param security_class: The security_class of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: str
        """

        self._security_class = security_class

    @property
    def security_status(self):
        """Gets the security_status of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        security_status number  # noqa: E501

        :return: The security_status of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: float
        """
        return self._security_status

    @security_status.setter
    def security_status(self, security_status):
        """Sets the security_status of this GetUniverseSystemsSystemIdOk.

        security_status number  # noqa: E501

        :param security_status: The security_status of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and security_status is None:
            raise ValueError("Invalid value for `security_status`, must not be `None`")  # noqa: E501

        self._security_status = security_status

    @property
    def star_id(self):
        """Gets the star_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        star_id integer  # noqa: E501

        :return: The star_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: int
        """
        return self._star_id

    @star_id.setter
    def star_id(self, star_id):
        """Sets the star_id of this GetUniverseSystemsSystemIdOk.

        star_id integer  # noqa: E501

        :param star_id: The star_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: int
        """

        self._star_id = star_id

    @property
    def stargates(self):
        """Gets the stargates of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        stargates array  # noqa: E501

        :return: The stargates of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: list[int]
        """
        return self._stargates

    @stargates.setter
    def stargates(self, stargates):
        """Sets the stargates of this GetUniverseSystemsSystemIdOk.

        stargates array  # noqa: E501

        :param stargates: The stargates of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: list[int]
        """

        self._stargates = stargates

    @property
    def stations(self):
        """Gets the stations of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        stations array  # noqa: E501

        :return: The stations of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: list[int]
        """
        return self._stations

    @stations.setter
    def stations(self, stations):
        """Sets the stations of this GetUniverseSystemsSystemIdOk.

        stations array  # noqa: E501

        :param stations: The stations of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: list[int]
        """

        self._stations = stations

    @property
    def system_id(self):
        """Gets the system_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501

        system_id integer  # noqa: E501

        :return: The system_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetUniverseSystemsSystemIdOk.

        system_id integer  # noqa: E501

        :param system_id: The system_id of this GetUniverseSystemsSystemIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and system_id is None:
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
        if issubclass(GetUniverseSystemsSystemIdOk, dict):
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
        if not isinstance(other, GetUniverseSystemsSystemIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseSystemsSystemIdOk):
            return True

        return self.to_dict() != other.to_dict()
