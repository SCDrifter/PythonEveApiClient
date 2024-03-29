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


class GetCharactersCharacterIdPlanetsPlanetIdPin(object):
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
        'contents': 'list[GetCharactersCharacterIdPlanetsPlanetIdContent]',
        'expiry_time': 'datetime',
        'extractor_details': 'GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails',
        'factory_details': 'GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails',
        'install_time': 'datetime',
        'last_cycle_start': 'datetime',
        'latitude': 'float',
        'longitude': 'float',
        'pin_id': 'int',
        'schematic_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'contents': 'contents',
        'expiry_time': 'expiry_time',
        'extractor_details': 'extractor_details',
        'factory_details': 'factory_details',
        'install_time': 'install_time',
        'last_cycle_start': 'last_cycle_start',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'pin_id': 'pin_id',
        'schematic_id': 'schematic_id',
        'type_id': 'type_id'
    }

    def __init__(self, contents=None, expiry_time=None, extractor_details=None, factory_details=None, install_time=None, last_cycle_start=None, latitude=None, longitude=None, pin_id=None, schematic_id=None, type_id=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdPlanetsPlanetIdPin - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._contents = None
        self._expiry_time = None
        self._extractor_details = None
        self._factory_details = None
        self._install_time = None
        self._last_cycle_start = None
        self._latitude = None
        self._longitude = None
        self._pin_id = None
        self._schematic_id = None
        self._type_id = None
        self.discriminator = None

        if contents is not None:
            self.contents = contents
        if expiry_time is not None:
            self.expiry_time = expiry_time
        if extractor_details is not None:
            self.extractor_details = extractor_details
        if factory_details is not None:
            self.factory_details = factory_details
        if install_time is not None:
            self.install_time = install_time
        if last_cycle_start is not None:
            self.last_cycle_start = last_cycle_start
        self.latitude = latitude
        self.longitude = longitude
        self.pin_id = pin_id
        if schematic_id is not None:
            self.schematic_id = schematic_id
        self.type_id = type_id

    @property
    def contents(self):
        """Gets the contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        contents array  # noqa: E501

        :return: The contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdPlanetsPlanetIdContent]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        contents array  # noqa: E501

        :param contents: The contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: list[GetCharactersCharacterIdPlanetsPlanetIdContent]
        """

        self._contents = contents

    @property
    def expiry_time(self):
        """Gets the expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        expiry_time string  # noqa: E501

        :return: The expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        expiry_time string  # noqa: E501

        :param expiry_time: The expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: datetime
        """

        self._expiry_time = expiry_time

    @property
    def extractor_details(self):
        """Gets the extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501


        :return: The extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
        """
        return self._extractor_details

    @extractor_details.setter
    def extractor_details(self, extractor_details):
        """Sets the extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.


        :param extractor_details: The extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
        """

        self._extractor_details = extractor_details

    @property
    def factory_details(self):
        """Gets the factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501


        :return: The factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
        """
        return self._factory_details

    @factory_details.setter
    def factory_details(self, factory_details):
        """Sets the factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.


        :param factory_details: The factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
        """

        self._factory_details = factory_details

    @property
    def install_time(self):
        """Gets the install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        install_time string  # noqa: E501

        :return: The install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: datetime
        """
        return self._install_time

    @install_time.setter
    def install_time(self, install_time):
        """Sets the install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        install_time string  # noqa: E501

        :param install_time: The install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: datetime
        """

        self._install_time = install_time

    @property
    def last_cycle_start(self):
        """Gets the last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        last_cycle_start string  # noqa: E501

        :return: The last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: datetime
        """
        return self._last_cycle_start

    @last_cycle_start.setter
    def last_cycle_start(self, last_cycle_start):
        """Sets the last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        last_cycle_start string  # noqa: E501

        :param last_cycle_start: The last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: datetime
        """

        self._last_cycle_start = last_cycle_start

    @property
    def latitude(self):
        """Gets the latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        latitude number  # noqa: E501

        :return: The latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        latitude number  # noqa: E501

        :param latitude: The latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        longitude number  # noqa: E501

        :return: The longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        longitude number  # noqa: E501

        :param longitude: The longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def pin_id(self):
        """Gets the pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        pin_id integer  # noqa: E501

        :return: The pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: int
        """
        return self._pin_id

    @pin_id.setter
    def pin_id(self, pin_id):
        """Sets the pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        pin_id integer  # noqa: E501

        :param pin_id: The pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and pin_id is None:
            raise ValueError("Invalid value for `pin_id`, must not be `None`")  # noqa: E501

        self._pin_id = pin_id

    @property
    def schematic_id(self):
        """Gets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        schematic_id integer  # noqa: E501

        :return: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: int
        """
        return self._schematic_id

    @schematic_id.setter
    def schematic_id(self, schematic_id):
        """Sets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        schematic_id integer  # noqa: E501

        :param schematic_id: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :type: int
        """

        self._schematic_id = schematic_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.  # noqa: E501
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
        if issubclass(GetCharactersCharacterIdPlanetsPlanetIdPin, dict):
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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdPin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdPin):
            return True

        return self.to_dict() != other.to_dict()
