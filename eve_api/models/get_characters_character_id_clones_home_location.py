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


class GetCharactersCharacterIdClonesHomeLocation(object):
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
        'location_id': 'int',
        'location_type': 'str'
    }

    attribute_map = {
        'location_id': 'location_id',
        'location_type': 'location_type'
    }

    def __init__(self, location_id=None, location_type=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdClonesHomeLocation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._location_id = None
        self._location_type = None
        self.discriminator = None

        if location_id is not None:
            self.location_id = location_id
        if location_type is not None:
            self.location_type = location_type

    @property
    def location_id(self):
        """Gets the location_id of this GetCharactersCharacterIdClonesHomeLocation.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetCharactersCharacterIdClonesHomeLocation.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCharactersCharacterIdClonesHomeLocation.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetCharactersCharacterIdClonesHomeLocation.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def location_type(self):
        """Gets the location_type of this GetCharactersCharacterIdClonesHomeLocation.  # noqa: E501

        location_type string  # noqa: E501

        :return: The location_type of this GetCharactersCharacterIdClonesHomeLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this GetCharactersCharacterIdClonesHomeLocation.

        location_type string  # noqa: E501

        :param location_type: The location_type of this GetCharactersCharacterIdClonesHomeLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["station", "structure"]  # noqa: E501
        if (self._configuration.client_side_validation and
                location_type not in allowed_values):
            raise ValueError(
                "Invalid value for `location_type` ({0}), must be one of {1}"  # noqa: E501
                .format(location_type, allowed_values)
            )

        self._location_type = location_type

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
        if issubclass(GetCharactersCharacterIdClonesHomeLocation, dict):
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
        if not isinstance(other, GetCharactersCharacterIdClonesHomeLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdClonesHomeLocation):
            return True

        return self.to_dict() != other.to_dict()
