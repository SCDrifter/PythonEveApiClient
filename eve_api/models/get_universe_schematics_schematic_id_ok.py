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


class GetUniverseSchematicsSchematicIdOk(object):
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
        'cycle_time': 'int',
        'schematic_name': 'str'
    }

    attribute_map = {
        'cycle_time': 'cycle_time',
        'schematic_name': 'schematic_name'
    }

    def __init__(self, cycle_time=None, schematic_name=None, _configuration=None):  # noqa: E501
        """GetUniverseSchematicsSchematicIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cycle_time = None
        self._schematic_name = None
        self.discriminator = None

        self.cycle_time = cycle_time
        self.schematic_name = schematic_name

    @property
    def cycle_time(self):
        """Gets the cycle_time of this GetUniverseSchematicsSchematicIdOk.  # noqa: E501

        Time in seconds to process a run  # noqa: E501

        :return: The cycle_time of this GetUniverseSchematicsSchematicIdOk.  # noqa: E501
        :rtype: int
        """
        return self._cycle_time

    @cycle_time.setter
    def cycle_time(self, cycle_time):
        """Sets the cycle_time of this GetUniverseSchematicsSchematicIdOk.

        Time in seconds to process a run  # noqa: E501

        :param cycle_time: The cycle_time of this GetUniverseSchematicsSchematicIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and cycle_time is None:
            raise ValueError("Invalid value for `cycle_time`, must not be `None`")  # noqa: E501

        self._cycle_time = cycle_time

    @property
    def schematic_name(self):
        """Gets the schematic_name of this GetUniverseSchematicsSchematicIdOk.  # noqa: E501

        schematic_name string  # noqa: E501

        :return: The schematic_name of this GetUniverseSchematicsSchematicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._schematic_name

    @schematic_name.setter
    def schematic_name(self, schematic_name):
        """Sets the schematic_name of this GetUniverseSchematicsSchematicIdOk.

        schematic_name string  # noqa: E501

        :param schematic_name: The schematic_name of this GetUniverseSchematicsSchematicIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and schematic_name is None:
            raise ValueError("Invalid value for `schematic_name`, must not be `None`")  # noqa: E501

        self._schematic_name = schematic_name

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
        if issubclass(GetUniverseSchematicsSchematicIdOk, dict):
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
        if not isinstance(other, GetUniverseSchematicsSchematicIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseSchematicsSchematicIdOk):
            return True

        return self.to_dict() != other.to_dict()
