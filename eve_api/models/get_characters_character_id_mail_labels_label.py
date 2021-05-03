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


class GetCharactersCharacterIdMailLabelsLabel(object):
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
        'color': 'str',
        'label_id': 'int',
        'name': 'str',
        'unread_count': 'int'
    }

    attribute_map = {
        'color': 'color',
        'label_id': 'label_id',
        'name': 'name',
        'unread_count': 'unread_count'
    }

    def __init__(self, color='#ffffff', label_id=None, name=None, unread_count=None):  # noqa: E501
        """GetCharactersCharacterIdMailLabelsLabel - a model defined in Swagger"""  # noqa: E501

        self._color = None
        self._label_id = None
        self._name = None
        self._unread_count = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if label_id is not None:
            self.label_id = label_id
        if name is not None:
            self.name = name
        if unread_count is not None:
            self.unread_count = unread_count

    @property
    def color(self):
        """Gets the color of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501

        color string  # noqa: E501

        :return: The color of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this GetCharactersCharacterIdMailLabelsLabel.

        color string  # noqa: E501

        :param color: The color of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :type: str
        """
        allowed_values = ["#0000fe", "#006634", "#0099ff", "#00ff33", "#01ffff", "#349800", "#660066", "#666666", "#999999", "#99ffff", "#9a0000", "#ccff9a", "#e6e6e6", "#fe0000", "#ff6600", "#ffff01", "#ffffcd", "#ffffff"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def label_id(self):
        """Gets the label_id of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501

        label_id integer  # noqa: E501

        :return: The label_id of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this GetCharactersCharacterIdMailLabelsLabel.

        label_id integer  # noqa: E501

        :param label_id: The label_id of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :type: int
        """
        if label_id is not None and label_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `label_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._label_id = label_id

    @property
    def name(self):
        """Gets the name of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCharactersCharacterIdMailLabelsLabel.

        name string  # noqa: E501

        :param name: The name of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 40:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `40`")  # noqa: E501

        self._name = name

    @property
    def unread_count(self):
        """Gets the unread_count of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501

        unread_count integer  # noqa: E501

        :return: The unread_count of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :rtype: int
        """
        return self._unread_count

    @unread_count.setter
    def unread_count(self, unread_count):
        """Sets the unread_count of this GetCharactersCharacterIdMailLabelsLabel.

        unread_count integer  # noqa: E501

        :param unread_count: The unread_count of this GetCharactersCharacterIdMailLabelsLabel.  # noqa: E501
        :type: int
        """
        if unread_count is not None and unread_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `unread_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._unread_count = unread_count

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
        if issubclass(GetCharactersCharacterIdMailLabelsLabel, dict):
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
        if not isinstance(other, GetCharactersCharacterIdMailLabelsLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
