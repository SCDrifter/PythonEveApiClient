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


class GetCharactersCharacterIdMailMailIdOk(object):
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
        'body': 'str',
        '_from': 'int',
        'labels': 'list[int]',
        'read': 'bool',
        'recipients': 'list[GetCharactersCharacterIdMailMailIdRecipient]',
        'subject': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'body': 'body',
        '_from': 'from',
        'labels': 'labels',
        'read': 'read',
        'recipients': 'recipients',
        'subject': 'subject',
        'timestamp': 'timestamp'
    }

    def __init__(self, body=None, _from=None, labels=None, read=None, recipients=None, subject=None, timestamp=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdMailMailIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self.__from = None
        self._labels = None
        self._read = None
        self._recipients = None
        self._subject = None
        self._timestamp = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if _from is not None:
            self._from = _from
        if labels is not None:
            self.labels = labels
        if read is not None:
            self.read = read
        if recipients is not None:
            self.recipients = recipients
        if subject is not None:
            self.subject = subject
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def body(self):
        """Gets the body of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        Mail's body  # noqa: E501

        :return: The body of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this GetCharactersCharacterIdMailMailIdOk.

        Mail's body  # noqa: E501

        :param body: The body of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        From whom the mail was sent  # noqa: E501

        :return: The _from of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this GetCharactersCharacterIdMailMailIdOk.

        From whom the mail was sent  # noqa: E501

        :param _from: The _from of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: int
        """

        self.__from = _from

    @property
    def labels(self):
        """Gets the labels of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        Labels attached to the mail  # noqa: E501

        :return: The labels of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GetCharactersCharacterIdMailMailIdOk.

        Labels attached to the mail  # noqa: E501

        :param labels: The labels of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: list[int]
        """

        self._labels = labels

    @property
    def read(self):
        """Gets the read of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        Whether the mail is flagged as read  # noqa: E501

        :return: The read of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this GetCharactersCharacterIdMailMailIdOk.

        Whether the mail is flagged as read  # noqa: E501

        :param read: The read of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def recipients(self):
        """Gets the recipients of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        Recipients of the mail  # noqa: E501

        :return: The recipients of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdMailMailIdRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this GetCharactersCharacterIdMailMailIdOk.

        Recipients of the mail  # noqa: E501

        :param recipients: The recipients of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: list[GetCharactersCharacterIdMailMailIdRecipient]
        """

        self._recipients = recipients

    @property
    def subject(self):
        """Gets the subject of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        Mail subject  # noqa: E501

        :return: The subject of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetCharactersCharacterIdMailMailIdOk.

        Mail subject  # noqa: E501

        :param subject: The subject of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def timestamp(self):
        """Gets the timestamp of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501

        When the mail was sent  # noqa: E501

        :return: The timestamp of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GetCharactersCharacterIdMailMailIdOk.

        When the mail was sent  # noqa: E501

        :param timestamp: The timestamp of this GetCharactersCharacterIdMailMailIdOk.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if issubclass(GetCharactersCharacterIdMailMailIdOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdMailMailIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdMailMailIdOk):
            return True

        return self.to_dict() != other.to_dict()
