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


class GetUniverseRegionsRegionIdOk(object):
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
        'constellations': 'list[int]',
        'description': 'str',
        'name': 'str',
        'region_id': 'int'
    }

    attribute_map = {
        'constellations': 'constellations',
        'description': 'description',
        'name': 'name',
        'region_id': 'region_id'
    }

    def __init__(self, constellations=None, description=None, name=None, region_id=None, _configuration=None):  # noqa: E501
        """GetUniverseRegionsRegionIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._constellations = None
        self._description = None
        self._name = None
        self._region_id = None
        self.discriminator = None

        self.constellations = constellations
        if description is not None:
            self.description = description
        self.name = name
        self.region_id = region_id

    @property
    def constellations(self):
        """Gets the constellations of this GetUniverseRegionsRegionIdOk.  # noqa: E501

        constellations array  # noqa: E501

        :return: The constellations of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :rtype: list[int]
        """
        return self._constellations

    @constellations.setter
    def constellations(self, constellations):
        """Sets the constellations of this GetUniverseRegionsRegionIdOk.

        constellations array  # noqa: E501

        :param constellations: The constellations of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and constellations is None:
            raise ValueError("Invalid value for `constellations`, must not be `None`")  # noqa: E501

        self._constellations = constellations

    @property
    def description(self):
        """Gets the description of this GetUniverseRegionsRegionIdOk.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetUniverseRegionsRegionIdOk.

        description string  # noqa: E501

        :param description: The description of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this GetUniverseRegionsRegionIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseRegionsRegionIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this GetUniverseRegionsRegionIdOk.  # noqa: E501

        region_id integer  # noqa: E501

        :return: The region_id of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this GetUniverseRegionsRegionIdOk.

        region_id integer  # noqa: E501

        :param region_id: The region_id of this GetUniverseRegionsRegionIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

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
        if issubclass(GetUniverseRegionsRegionIdOk, dict):
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
        if not isinstance(other, GetUniverseRegionsRegionIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseRegionsRegionIdOk):
            return True

        return self.to_dict() != other.to_dict()
