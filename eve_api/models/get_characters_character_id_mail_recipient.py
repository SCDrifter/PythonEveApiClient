# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCharactersCharacterIdMailRecipient(object):
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
        'recipient_id': 'int',
        'recipient_type': 'str'
    }

    attribute_map = {
        'recipient_id': 'recipient_id',
        'recipient_type': 'recipient_type'
    }

    def __init__(self, recipient_id=None, recipient_type=None):  # noqa: E501
        """GetCharactersCharacterIdMailRecipient - a model defined in Swagger"""  # noqa: E501

        self._recipient_id = None
        self._recipient_type = None
        self.discriminator = None

        self.recipient_id = recipient_id
        self.recipient_type = recipient_type

    @property
    def recipient_id(self):
        """Gets the recipient_id of this GetCharactersCharacterIdMailRecipient.  # noqa: E501

        recipient_id integer  # noqa: E501

        :return: The recipient_id of this GetCharactersCharacterIdMailRecipient.  # noqa: E501
        :rtype: int
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this GetCharactersCharacterIdMailRecipient.

        recipient_id integer  # noqa: E501

        :param recipient_id: The recipient_id of this GetCharactersCharacterIdMailRecipient.  # noqa: E501
        :type: int
        """
        if recipient_id is None:
            raise ValueError("Invalid value for `recipient_id`, must not be `None`")  # noqa: E501

        self._recipient_id = recipient_id

    @property
    def recipient_type(self):
        """Gets the recipient_type of this GetCharactersCharacterIdMailRecipient.  # noqa: E501

        recipient_type string  # noqa: E501

        :return: The recipient_type of this GetCharactersCharacterIdMailRecipient.  # noqa: E501
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """Sets the recipient_type of this GetCharactersCharacterIdMailRecipient.

        recipient_type string  # noqa: E501

        :param recipient_type: The recipient_type of this GetCharactersCharacterIdMailRecipient.  # noqa: E501
        :type: str
        """
        if recipient_type is None:
            raise ValueError("Invalid value for `recipient_type`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance", "character", "corporation", "mailing_list"]  # noqa: E501
        if recipient_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recipient_type` ({0}), must be one of {1}"  # noqa: E501
                .format(recipient_type, allowed_values)
            )

        self._recipient_type = recipient_type

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
        if issubclass(GetCharactersCharacterIdMailRecipient, dict):
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
        if not isinstance(other, GetCharactersCharacterIdMailRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
