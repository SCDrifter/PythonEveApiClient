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


class GetCharactersCharacterIdOpportunities200Ok(object):
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
        'completed_at': 'datetime',
        'task_id': 'int'
    }

    attribute_map = {
        'completed_at': 'completed_at',
        'task_id': 'task_id'
    }

    def __init__(self, completed_at=None, task_id=None):  # noqa: E501
        """GetCharactersCharacterIdOpportunities200Ok - a model defined in Swagger"""  # noqa: E501

        self._completed_at = None
        self._task_id = None
        self.discriminator = None

        self.completed_at = completed_at
        self.task_id = task_id

    @property
    def completed_at(self):
        """Gets the completed_at of this GetCharactersCharacterIdOpportunities200Ok.  # noqa: E501

        completed_at string  # noqa: E501

        :return: The completed_at of this GetCharactersCharacterIdOpportunities200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this GetCharactersCharacterIdOpportunities200Ok.

        completed_at string  # noqa: E501

        :param completed_at: The completed_at of this GetCharactersCharacterIdOpportunities200Ok.  # noqa: E501
        :type: datetime
        """
        if completed_at is None:
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def task_id(self):
        """Gets the task_id of this GetCharactersCharacterIdOpportunities200Ok.  # noqa: E501

        task_id integer  # noqa: E501

        :return: The task_id of this GetCharactersCharacterIdOpportunities200Ok.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this GetCharactersCharacterIdOpportunities200Ok.

        task_id integer  # noqa: E501

        :param task_id: The task_id of this GetCharactersCharacterIdOpportunities200Ok.  # noqa: E501
        :type: int
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

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
        if issubclass(GetCharactersCharacterIdOpportunities200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdOpportunities200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
