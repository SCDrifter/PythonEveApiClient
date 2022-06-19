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


class GetCharactersCharacterIdTitles200Ok(object):
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
        'title_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'title_id': 'title_id'
    }

    def __init__(self, name=None, title_id=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdTitles200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._title_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if title_id is not None:
            self.title_id = title_id

    @property
    def name(self):
        """Gets the name of this GetCharactersCharacterIdTitles200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetCharactersCharacterIdTitles200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCharactersCharacterIdTitles200Ok.

        name string  # noqa: E501

        :param name: The name of this GetCharactersCharacterIdTitles200Ok.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title_id(self):
        """Gets the title_id of this GetCharactersCharacterIdTitles200Ok.  # noqa: E501

        title_id integer  # noqa: E501

        :return: The title_id of this GetCharactersCharacterIdTitles200Ok.  # noqa: E501
        :rtype: int
        """
        return self._title_id

    @title_id.setter
    def title_id(self, title_id):
        """Sets the title_id of this GetCharactersCharacterIdTitles200Ok.

        title_id integer  # noqa: E501

        :param title_id: The title_id of this GetCharactersCharacterIdTitles200Ok.  # noqa: E501
        :type: int
        """

        self._title_id = title_id

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
        if issubclass(GetCharactersCharacterIdTitles200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdTitles200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdTitles200Ok):
            return True

        return self.to_dict() != other.to_dict()
