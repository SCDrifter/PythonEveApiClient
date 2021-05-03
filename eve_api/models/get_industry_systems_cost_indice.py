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


class GetIndustrySystemsCostIndice(object):
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
        'activity': 'str',
        'cost_index': 'float'
    }

    attribute_map = {
        'activity': 'activity',
        'cost_index': 'cost_index'
    }

    def __init__(self, activity=None, cost_index=None):  # noqa: E501
        """GetIndustrySystemsCostIndice - a model defined in Swagger"""  # noqa: E501

        self._activity = None
        self._cost_index = None
        self.discriminator = None

        self.activity = activity
        self.cost_index = cost_index

    @property
    def activity(self):
        """Gets the activity of this GetIndustrySystemsCostIndice.  # noqa: E501

        activity string  # noqa: E501

        :return: The activity of this GetIndustrySystemsCostIndice.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this GetIndustrySystemsCostIndice.

        activity string  # noqa: E501

        :param activity: The activity of this GetIndustrySystemsCostIndice.  # noqa: E501
        :type: str
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501
        allowed_values = ["copying", "duplicating", "invention", "manufacturing", "none", "reaction", "researching_material_efficiency", "researching_technology", "researching_time_efficiency", "reverse_engineering"]  # noqa: E501
        if activity not in allowed_values:
            raise ValueError(
                "Invalid value for `activity` ({0}), must be one of {1}"  # noqa: E501
                .format(activity, allowed_values)
            )

        self._activity = activity

    @property
    def cost_index(self):
        """Gets the cost_index of this GetIndustrySystemsCostIndice.  # noqa: E501

        cost_index number  # noqa: E501

        :return: The cost_index of this GetIndustrySystemsCostIndice.  # noqa: E501
        :rtype: float
        """
        return self._cost_index

    @cost_index.setter
    def cost_index(self, cost_index):
        """Sets the cost_index of this GetIndustrySystemsCostIndice.

        cost_index number  # noqa: E501

        :param cost_index: The cost_index of this GetIndustrySystemsCostIndice.  # noqa: E501
        :type: float
        """
        if cost_index is None:
            raise ValueError("Invalid value for `cost_index`, must not be `None`")  # noqa: E501

        self._cost_index = cost_index

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
        if issubclass(GetIndustrySystemsCostIndice, dict):
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
        if not isinstance(other, GetIndustrySystemsCostIndice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
