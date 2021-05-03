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


class GetCorporationsCorporationIdKillmailsRecent200Ok(object):
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
        'killmail_hash': 'str',
        'killmail_id': 'int'
    }

    attribute_map = {
        'killmail_hash': 'killmail_hash',
        'killmail_id': 'killmail_id'
    }

    def __init__(self, killmail_hash=None, killmail_id=None):  # noqa: E501
        """GetCorporationsCorporationIdKillmailsRecent200Ok - a model defined in Swagger"""  # noqa: E501

        self._killmail_hash = None
        self._killmail_id = None
        self.discriminator = None

        self.killmail_hash = killmail_hash
        self.killmail_id = killmail_id

    @property
    def killmail_hash(self):
        """Gets the killmail_hash of this GetCorporationsCorporationIdKillmailsRecent200Ok.  # noqa: E501

        A hash of this killmail  # noqa: E501

        :return: The killmail_hash of this GetCorporationsCorporationIdKillmailsRecent200Ok.  # noqa: E501
        :rtype: str
        """
        return self._killmail_hash

    @killmail_hash.setter
    def killmail_hash(self, killmail_hash):
        """Sets the killmail_hash of this GetCorporationsCorporationIdKillmailsRecent200Ok.

        A hash of this killmail  # noqa: E501

        :param killmail_hash: The killmail_hash of this GetCorporationsCorporationIdKillmailsRecent200Ok.  # noqa: E501
        :type: str
        """
        if killmail_hash is None:
            raise ValueError("Invalid value for `killmail_hash`, must not be `None`")  # noqa: E501

        self._killmail_hash = killmail_hash

    @property
    def killmail_id(self):
        """Gets the killmail_id of this GetCorporationsCorporationIdKillmailsRecent200Ok.  # noqa: E501

        ID of this killmail  # noqa: E501

        :return: The killmail_id of this GetCorporationsCorporationIdKillmailsRecent200Ok.  # noqa: E501
        :rtype: int
        """
        return self._killmail_id

    @killmail_id.setter
    def killmail_id(self, killmail_id):
        """Sets the killmail_id of this GetCorporationsCorporationIdKillmailsRecent200Ok.

        ID of this killmail  # noqa: E501

        :param killmail_id: The killmail_id of this GetCorporationsCorporationIdKillmailsRecent200Ok.  # noqa: E501
        :type: int
        """
        if killmail_id is None:
            raise ValueError("Invalid value for `killmail_id`, must not be `None`")  # noqa: E501

        self._killmail_id = killmail_id

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
        if issubclass(GetCorporationsCorporationIdKillmailsRecent200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdKillmailsRecent200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
