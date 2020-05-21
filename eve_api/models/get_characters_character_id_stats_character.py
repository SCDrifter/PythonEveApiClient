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


class GetCharactersCharacterIdStatsCharacter(object):
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
        'days_of_activity': 'int',
        'minutes': 'int',
        'sessions_started': 'int'
    }

    attribute_map = {
        'days_of_activity': 'days_of_activity',
        'minutes': 'minutes',
        'sessions_started': 'sessions_started'
    }

    def __init__(self, days_of_activity=None, minutes=None, sessions_started=None):  # noqa: E501
        """GetCharactersCharacterIdStatsCharacter - a model defined in Swagger"""  # noqa: E501

        self._days_of_activity = None
        self._minutes = None
        self._sessions_started = None
        self.discriminator = None

        if days_of_activity is not None:
            self.days_of_activity = days_of_activity
        if minutes is not None:
            self.minutes = minutes
        if sessions_started is not None:
            self.sessions_started = sessions_started

    @property
    def days_of_activity(self):
        """Gets the days_of_activity of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501

        days_of_activity integer  # noqa: E501

        :return: The days_of_activity of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501
        :rtype: int
        """
        return self._days_of_activity

    @days_of_activity.setter
    def days_of_activity(self, days_of_activity):
        """Sets the days_of_activity of this GetCharactersCharacterIdStatsCharacter.

        days_of_activity integer  # noqa: E501

        :param days_of_activity: The days_of_activity of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501
        :type: int
        """

        self._days_of_activity = days_of_activity

    @property
    def minutes(self):
        """Gets the minutes of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501

        minutes integer  # noqa: E501

        :return: The minutes of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this GetCharactersCharacterIdStatsCharacter.

        minutes integer  # noqa: E501

        :param minutes: The minutes of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def sessions_started(self):
        """Gets the sessions_started of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501

        sessions_started integer  # noqa: E501

        :return: The sessions_started of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501
        :rtype: int
        """
        return self._sessions_started

    @sessions_started.setter
    def sessions_started(self, sessions_started):
        """Sets the sessions_started of this GetCharactersCharacterIdStatsCharacter.

        sessions_started integer  # noqa: E501

        :param sessions_started: The sessions_started of this GetCharactersCharacterIdStatsCharacter.  # noqa: E501
        :type: int
        """

        self._sessions_started = sessions_started

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
        if issubclass(GetCharactersCharacterIdStatsCharacter, dict):
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
        if not isinstance(other, GetCharactersCharacterIdStatsCharacter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
