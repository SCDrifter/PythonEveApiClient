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


class PostCharactersCharacterIdFittingsCreated(object):
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
        'fitting_id': 'int'
    }

    attribute_map = {
        'fitting_id': 'fitting_id'
    }

    def __init__(self, fitting_id=None):  # noqa: E501
        """PostCharactersCharacterIdFittingsCreated - a model defined in Swagger"""  # noqa: E501

        self._fitting_id = None
        self.discriminator = None

        self.fitting_id = fitting_id

    @property
    def fitting_id(self):
        """Gets the fitting_id of this PostCharactersCharacterIdFittingsCreated.  # noqa: E501

        fitting_id integer  # noqa: E501

        :return: The fitting_id of this PostCharactersCharacterIdFittingsCreated.  # noqa: E501
        :rtype: int
        """
        return self._fitting_id

    @fitting_id.setter
    def fitting_id(self, fitting_id):
        """Sets the fitting_id of this PostCharactersCharacterIdFittingsCreated.

        fitting_id integer  # noqa: E501

        :param fitting_id: The fitting_id of this PostCharactersCharacterIdFittingsCreated.  # noqa: E501
        :type: int
        """
        if fitting_id is None:
            raise ValueError("Invalid value for `fitting_id`, must not be `None`")  # noqa: E501

        self._fitting_id = fitting_id

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
        if issubclass(PostCharactersCharacterIdFittingsCreated, dict):
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
        if not isinstance(other, PostCharactersCharacterIdFittingsCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
