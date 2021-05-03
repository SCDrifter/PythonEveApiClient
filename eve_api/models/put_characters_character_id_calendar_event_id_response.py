# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutCharactersCharacterIdCalendarEventIdResponse(object):
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
        'response': 'str'
    }

    attribute_map = {
        'response': 'response'
    }

    def __init__(self, response=None):  # noqa: E501
        """PutCharactersCharacterIdCalendarEventIdResponse - a model defined in Swagger"""  # noqa: E501

        self._response = None
        self.discriminator = None

        self.response = response

    @property
    def response(self):
        """Gets the response of this PutCharactersCharacterIdCalendarEventIdResponse.  # noqa: E501

        response string  # noqa: E501

        :return: The response of this PutCharactersCharacterIdCalendarEventIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this PutCharactersCharacterIdCalendarEventIdResponse.

        response string  # noqa: E501

        :param response: The response of this PutCharactersCharacterIdCalendarEventIdResponse.  # noqa: E501
        :type: str
        """
        if response is None:
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501
        allowed_values = ["accepted", "declined", "tentative"]  # noqa: E501
        if response not in allowed_values:
            raise ValueError(
                "Invalid value for `response` ({0}), must be one of {1}"  # noqa: E501
                .format(response, allowed_values)
            )

        self._response = response

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
        if issubclass(PutCharactersCharacterIdCalendarEventIdResponse, dict):
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
        if not isinstance(other, PutCharactersCharacterIdCalendarEventIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
