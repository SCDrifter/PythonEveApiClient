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


class GetSovereigntyCampaignsParticipant(object):
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
        'score': 'float'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'score': 'score'
    }

    def __init__(self, alliance_id=None, score=None, _configuration=None):  # noqa: E501
        """GetSovereigntyCampaignsParticipant - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alliance_id = None
        self._score = None
        self.discriminator = None

        self.alliance_id = alliance_id
        self.score = score

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetSovereigntyCampaignsParticipant.  # noqa: E501

        alliance_id integer  # noqa: E501

        :return: The alliance_id of this GetSovereigntyCampaignsParticipant.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetSovereigntyCampaignsParticipant.

        alliance_id integer  # noqa: E501

        :param alliance_id: The alliance_id of this GetSovereigntyCampaignsParticipant.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and alliance_id is None:
            raise ValueError("Invalid value for `alliance_id`, must not be `None`")  # noqa: E501

        self._alliance_id = alliance_id

    @property
    def score(self):
        """Gets the score of this GetSovereigntyCampaignsParticipant.  # noqa: E501

        score number  # noqa: E501

        :return: The score of this GetSovereigntyCampaignsParticipant.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this GetSovereigntyCampaignsParticipant.

        score number  # noqa: E501

        :param score: The score of this GetSovereigntyCampaignsParticipant.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

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
        if issubclass(GetSovereigntyCampaignsParticipant, dict):
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
        if not isinstance(other, GetSovereigntyCampaignsParticipant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSovereigntyCampaignsParticipant):
            return True

        return self.to_dict() != other.to_dict()
