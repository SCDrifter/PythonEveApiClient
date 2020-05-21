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


class GetCharactersCharacterIdPlanetsPlanetIdHead(object):
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
        'head_id': 'int',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'head_id': 'head_id',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, head_id=None, latitude=None, longitude=None):  # noqa: E501
        """GetCharactersCharacterIdPlanetsPlanetIdHead - a model defined in Swagger"""  # noqa: E501

        self._head_id = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        self.head_id = head_id
        self.latitude = latitude
        self.longitude = longitude

    @property
    def head_id(self):
        """Gets the head_id of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501

        head_id integer  # noqa: E501

        :return: The head_id of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501
        :rtype: int
        """
        return self._head_id

    @head_id.setter
    def head_id(self, head_id):
        """Sets the head_id of this GetCharactersCharacterIdPlanetsPlanetIdHead.

        head_id integer  # noqa: E501

        :param head_id: The head_id of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501
        :type: int
        """
        if head_id is None:
            raise ValueError("Invalid value for `head_id`, must not be `None`")  # noqa: E501
        if head_id is not None and head_id > 9:  # noqa: E501
            raise ValueError("Invalid value for `head_id`, must be a value less than or equal to `9`")  # noqa: E501
        if head_id is not None and head_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `head_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._head_id = head_id

    @property
    def latitude(self):
        """Gets the latitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501

        latitude number  # noqa: E501

        :return: The latitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.

        latitude number  # noqa: E501

        :param latitude: The latitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501
        :type: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501

        longitude number  # noqa: E501

        :return: The longitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.

        longitude number  # noqa: E501

        :param longitude: The longitude of this GetCharactersCharacterIdPlanetsPlanetIdHead.  # noqa: E501
        :type: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

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
        if issubclass(GetCharactersCharacterIdPlanetsPlanetIdHead, dict):
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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdHead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
