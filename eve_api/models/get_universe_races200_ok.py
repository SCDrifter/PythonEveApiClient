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


class GetUniverseRaces200Ok(object):
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
        'alliance_id': 'int',
        'description': 'str',
        'name': 'str',
        'race_id': 'int'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'description': 'description',
        'name': 'name',
        'race_id': 'race_id'
    }

    def __init__(self, alliance_id=None, description=None, name=None, race_id=None, _configuration=None):  # noqa: E501
        """GetUniverseRaces200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alliance_id = None
        self._description = None
        self._name = None
        self._race_id = None
        self.discriminator = None

        self.alliance_id = alliance_id
        self.description = description
        self.name = name
        self.race_id = race_id

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetUniverseRaces200Ok.  # noqa: E501

        The alliance generally associated with this race  # noqa: E501

        :return: The alliance_id of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetUniverseRaces200Ok.

        The alliance generally associated with this race  # noqa: E501

        :param alliance_id: The alliance_id of this GetUniverseRaces200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and alliance_id is None:
            raise ValueError("Invalid value for `alliance_id`, must not be `None`")  # noqa: E501

        self._alliance_id = alliance_id

    @property
    def description(self):
        """Gets the description of this GetUniverseRaces200Ok.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetUniverseRaces200Ok.

        description string  # noqa: E501

        :param description: The description of this GetUniverseRaces200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this GetUniverseRaces200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseRaces200Ok.

        name string  # noqa: E501

        :param name: The name of this GetUniverseRaces200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def race_id(self):
        """Gets the race_id of this GetUniverseRaces200Ok.  # noqa: E501

        race_id integer  # noqa: E501

        :return: The race_id of this GetUniverseRaces200Ok.  # noqa: E501
        :rtype: int
        """
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        """Sets the race_id of this GetUniverseRaces200Ok.

        race_id integer  # noqa: E501

        :param race_id: The race_id of this GetUniverseRaces200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and race_id is None:
            raise ValueError("Invalid value for `race_id`, must not be `None`")  # noqa: E501

        self._race_id = race_id

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
        if issubclass(GetUniverseRaces200Ok, dict):
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
        if not isinstance(other, GetUniverseRaces200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseRaces200Ok):
            return True

        return self.to_dict() != other.to_dict()
