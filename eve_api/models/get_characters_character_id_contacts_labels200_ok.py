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


class GetCharactersCharacterIdContactsLabels200Ok(object):
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
        'label_id': 'int',
        'label_name': 'str'
    }

    attribute_map = {
        'label_id': 'label_id',
        'label_name': 'label_name'
    }

    def __init__(self, label_id=None, label_name=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdContactsLabels200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._label_id = None
        self._label_name = None
        self.discriminator = None

        self.label_id = label_id
        self.label_name = label_name

    @property
    def label_id(self):
        """Gets the label_id of this GetCharactersCharacterIdContactsLabels200Ok.  # noqa: E501

        label_id integer  # noqa: E501

        :return: The label_id of this GetCharactersCharacterIdContactsLabels200Ok.  # noqa: E501
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this GetCharactersCharacterIdContactsLabels200Ok.

        label_id integer  # noqa: E501

        :param label_id: The label_id of this GetCharactersCharacterIdContactsLabels200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and label_id is None:
            raise ValueError("Invalid value for `label_id`, must not be `None`")  # noqa: E501

        self._label_id = label_id

    @property
    def label_name(self):
        """Gets the label_name of this GetCharactersCharacterIdContactsLabels200Ok.  # noqa: E501

        label_name string  # noqa: E501

        :return: The label_name of this GetCharactersCharacterIdContactsLabels200Ok.  # noqa: E501
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this GetCharactersCharacterIdContactsLabels200Ok.

        label_name string  # noqa: E501

        :param label_name: The label_name of this GetCharactersCharacterIdContactsLabels200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and label_name is None:
            raise ValueError("Invalid value for `label_name`, must not be `None`")  # noqa: E501

        self._label_name = label_name

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
        if issubclass(GetCharactersCharacterIdContactsLabels200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdContactsLabels200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdContactsLabels200Ok):
            return True

        return self.to_dict() != other.to_dict()
