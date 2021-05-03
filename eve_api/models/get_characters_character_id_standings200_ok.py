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


class GetCharactersCharacterIdStandings200Ok(object):
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
        'from_id': 'int',
        'from_type': 'str',
        'standing': 'float'
    }

    attribute_map = {
        'from_id': 'from_id',
        'from_type': 'from_type',
        'standing': 'standing'
    }

    def __init__(self, from_id=None, from_type=None, standing=None):  # noqa: E501
        """GetCharactersCharacterIdStandings200Ok - a model defined in Swagger"""  # noqa: E501

        self._from_id = None
        self._from_type = None
        self._standing = None
        self.discriminator = None

        self.from_id = from_id
        self.from_type = from_type
        self.standing = standing

    @property
    def from_id(self):
        """Gets the from_id of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501

        from_id integer  # noqa: E501

        :return: The from_id of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501
        :rtype: int
        """
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        """Sets the from_id of this GetCharactersCharacterIdStandings200Ok.

        from_id integer  # noqa: E501

        :param from_id: The from_id of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501
        :type: int
        """
        if from_id is None:
            raise ValueError("Invalid value for `from_id`, must not be `None`")  # noqa: E501

        self._from_id = from_id

    @property
    def from_type(self):
        """Gets the from_type of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501

        from_type string  # noqa: E501

        :return: The from_type of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501
        :rtype: str
        """
        return self._from_type

    @from_type.setter
    def from_type(self, from_type):
        """Sets the from_type of this GetCharactersCharacterIdStandings200Ok.

        from_type string  # noqa: E501

        :param from_type: The from_type of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501
        :type: str
        """
        if from_type is None:
            raise ValueError("Invalid value for `from_type`, must not be `None`")  # noqa: E501
        allowed_values = ["agent", "npc_corp", "faction"]  # noqa: E501
        if from_type not in allowed_values:
            raise ValueError(
                "Invalid value for `from_type` ({0}), must be one of {1}"  # noqa: E501
                .format(from_type, allowed_values)
            )

        self._from_type = from_type

    @property
    def standing(self):
        """Gets the standing of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501

        standing number  # noqa: E501

        :return: The standing of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501
        :rtype: float
        """
        return self._standing

    @standing.setter
    def standing(self, standing):
        """Sets the standing of this GetCharactersCharacterIdStandings200Ok.

        standing number  # noqa: E501

        :param standing: The standing of this GetCharactersCharacterIdStandings200Ok.  # noqa: E501
        :type: float
        """
        if standing is None:
            raise ValueError("Invalid value for `standing`, must not be `None`")  # noqa: E501

        self._standing = standing

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
        if issubclass(GetCharactersCharacterIdStandings200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdStandings200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
