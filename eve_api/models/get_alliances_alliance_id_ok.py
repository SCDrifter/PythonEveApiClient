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


class GetAlliancesAllianceIdOk(object):
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
        'creator_corporation_id': 'int',
        'creator_id': 'int',
        'date_founded': 'datetime',
        'executor_corporation_id': 'int',
        'faction_id': 'int',
        'name': 'str',
        'ticker': 'str'
    }

    attribute_map = {
        'creator_corporation_id': 'creator_corporation_id',
        'creator_id': 'creator_id',
        'date_founded': 'date_founded',
        'executor_corporation_id': 'executor_corporation_id',
        'faction_id': 'faction_id',
        'name': 'name',
        'ticker': 'ticker'
    }

    def __init__(self, creator_corporation_id=None, creator_id=None, date_founded=None, executor_corporation_id=None, faction_id=None, name=None, ticker=None, _configuration=None):  # noqa: E501
        """GetAlliancesAllianceIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creator_corporation_id = None
        self._creator_id = None
        self._date_founded = None
        self._executor_corporation_id = None
        self._faction_id = None
        self._name = None
        self._ticker = None
        self.discriminator = None

        self.creator_corporation_id = creator_corporation_id
        self.creator_id = creator_id
        self.date_founded = date_founded
        if executor_corporation_id is not None:
            self.executor_corporation_id = executor_corporation_id
        if faction_id is not None:
            self.faction_id = faction_id
        self.name = name
        self.ticker = ticker

    @property
    def creator_corporation_id(self):
        """Gets the creator_corporation_id of this GetAlliancesAllianceIdOk.  # noqa: E501

        ID of the corporation that created the alliance  # noqa: E501

        :return: The creator_corporation_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: int
        """
        return self._creator_corporation_id

    @creator_corporation_id.setter
    def creator_corporation_id(self, creator_corporation_id):
        """Sets the creator_corporation_id of this GetAlliancesAllianceIdOk.

        ID of the corporation that created the alliance  # noqa: E501

        :param creator_corporation_id: The creator_corporation_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and creator_corporation_id is None:
            raise ValueError("Invalid value for `creator_corporation_id`, must not be `None`")  # noqa: E501

        self._creator_corporation_id = creator_corporation_id

    @property
    def creator_id(self):
        """Gets the creator_id of this GetAlliancesAllianceIdOk.  # noqa: E501

        ID of the character that created the alliance  # noqa: E501

        :return: The creator_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this GetAlliancesAllianceIdOk.

        ID of the character that created the alliance  # noqa: E501

        :param creator_id: The creator_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def date_founded(self):
        """Gets the date_founded of this GetAlliancesAllianceIdOk.  # noqa: E501

        date_founded string  # noqa: E501

        :return: The date_founded of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._date_founded

    @date_founded.setter
    def date_founded(self, date_founded):
        """Sets the date_founded of this GetAlliancesAllianceIdOk.

        date_founded string  # noqa: E501

        :param date_founded: The date_founded of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and date_founded is None:
            raise ValueError("Invalid value for `date_founded`, must not be `None`")  # noqa: E501

        self._date_founded = date_founded

    @property
    def executor_corporation_id(self):
        """Gets the executor_corporation_id of this GetAlliancesAllianceIdOk.  # noqa: E501

        the executor corporation ID, if this alliance is not closed  # noqa: E501

        :return: The executor_corporation_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: int
        """
        return self._executor_corporation_id

    @executor_corporation_id.setter
    def executor_corporation_id(self, executor_corporation_id):
        """Sets the executor_corporation_id of this GetAlliancesAllianceIdOk.

        the executor corporation ID, if this alliance is not closed  # noqa: E501

        :param executor_corporation_id: The executor_corporation_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: int
        """

        self._executor_corporation_id = executor_corporation_id

    @property
    def faction_id(self):
        """Gets the faction_id of this GetAlliancesAllianceIdOk.  # noqa: E501

        Faction ID this alliance is fighting for, if this alliance is enlisted in factional warfare  # noqa: E501

        :return: The faction_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetAlliancesAllianceIdOk.

        Faction ID this alliance is fighting for, if this alliance is enlisted in factional warfare  # noqa: E501

        :param faction_id: The faction_id of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: int
        """

        self._faction_id = faction_id

    @property
    def name(self):
        """Gets the name of this GetAlliancesAllianceIdOk.  # noqa: E501

        the full name of the alliance  # noqa: E501

        :return: The name of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAlliancesAllianceIdOk.

        the full name of the alliance  # noqa: E501

        :param name: The name of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this GetAlliancesAllianceIdOk.  # noqa: E501

        the short name of the alliance  # noqa: E501

        :return: The ticker of this GetAlliancesAllianceIdOk.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this GetAlliancesAllianceIdOk.

        the short name of the alliance  # noqa: E501

        :param ticker: The ticker of this GetAlliancesAllianceIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

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
        if issubclass(GetAlliancesAllianceIdOk, dict):
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
        if not isinstance(other, GetAlliancesAllianceIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAlliancesAllianceIdOk):
            return True

        return self.to_dict() != other.to_dict()
