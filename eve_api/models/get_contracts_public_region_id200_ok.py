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


class GetContractsPublicRegionId200Ok(object):
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
        'buyout': 'float',
        'collateral': 'float',
        'contract_id': 'int',
        'date_expired': 'datetime',
        'date_issued': 'datetime',
        'days_to_complete': 'int',
        'end_location_id': 'int',
        'for_corporation': 'bool',
        'issuer_corporation_id': 'int',
        'issuer_id': 'int',
        'price': 'float',
        'reward': 'float',
        'start_location_id': 'int',
        'title': 'str',
        'type': 'str',
        'volume': 'float'
    }

    attribute_map = {
        'buyout': 'buyout',
        'collateral': 'collateral',
        'contract_id': 'contract_id',
        'date_expired': 'date_expired',
        'date_issued': 'date_issued',
        'days_to_complete': 'days_to_complete',
        'end_location_id': 'end_location_id',
        'for_corporation': 'for_corporation',
        'issuer_corporation_id': 'issuer_corporation_id',
        'issuer_id': 'issuer_id',
        'price': 'price',
        'reward': 'reward',
        'start_location_id': 'start_location_id',
        'title': 'title',
        'type': 'type',
        'volume': 'volume'
    }

    def __init__(self, buyout=None, collateral=None, contract_id=None, date_expired=None, date_issued=None, days_to_complete=None, end_location_id=None, for_corporation=None, issuer_corporation_id=None, issuer_id=None, price=None, reward=None, start_location_id=None, title=None, type=None, volume=None, _configuration=None):  # noqa: E501
        """GetContractsPublicRegionId200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._buyout = None
        self._collateral = None
        self._contract_id = None
        self._date_expired = None
        self._date_issued = None
        self._days_to_complete = None
        self._end_location_id = None
        self._for_corporation = None
        self._issuer_corporation_id = None
        self._issuer_id = None
        self._price = None
        self._reward = None
        self._start_location_id = None
        self._title = None
        self._type = None
        self._volume = None
        self.discriminator = None

        if buyout is not None:
            self.buyout = buyout
        if collateral is not None:
            self.collateral = collateral
        self.contract_id = contract_id
        self.date_expired = date_expired
        self.date_issued = date_issued
        if days_to_complete is not None:
            self.days_to_complete = days_to_complete
        if end_location_id is not None:
            self.end_location_id = end_location_id
        if for_corporation is not None:
            self.for_corporation = for_corporation
        self.issuer_corporation_id = issuer_corporation_id
        self.issuer_id = issuer_id
        if price is not None:
            self.price = price
        if reward is not None:
            self.reward = reward
        if start_location_id is not None:
            self.start_location_id = start_location_id
        if title is not None:
            self.title = title
        self.type = type
        if volume is not None:
            self.volume = volume

    @property
    def buyout(self):
        """Gets the buyout of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Buyout price (for Auctions only)  # noqa: E501

        :return: The buyout of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: float
        """
        return self._buyout

    @buyout.setter
    def buyout(self, buyout):
        """Sets the buyout of this GetContractsPublicRegionId200Ok.

        Buyout price (for Auctions only)  # noqa: E501

        :param buyout: The buyout of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: float
        """

        self._buyout = buyout

    @property
    def collateral(self):
        """Gets the collateral of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Collateral price (for Couriers only)  # noqa: E501

        :return: The collateral of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: float
        """
        return self._collateral

    @collateral.setter
    def collateral(self, collateral):
        """Sets the collateral of this GetContractsPublicRegionId200Ok.

        Collateral price (for Couriers only)  # noqa: E501

        :param collateral: The collateral of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: float
        """

        self._collateral = collateral

    @property
    def contract_id(self):
        """Gets the contract_id of this GetContractsPublicRegionId200Ok.  # noqa: E501

        contract_id integer  # noqa: E501

        :return: The contract_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this GetContractsPublicRegionId200Ok.

        contract_id integer  # noqa: E501

        :param contract_id: The contract_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and contract_id is None:
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def date_expired(self):
        """Gets the date_expired of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Expiration date of the contract  # noqa: E501

        :return: The date_expired of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._date_expired

    @date_expired.setter
    def date_expired(self, date_expired):
        """Sets the date_expired of this GetContractsPublicRegionId200Ok.

        Expiration date of the contract  # noqa: E501

        :param date_expired: The date_expired of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and date_expired is None:
            raise ValueError("Invalid value for `date_expired`, must not be `None`")  # noqa: E501

        self._date_expired = date_expired

    @property
    def date_issued(self):
        """Gets the date_issued of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Сreation date of the contract  # noqa: E501

        :return: The date_issued of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._date_issued

    @date_issued.setter
    def date_issued(self, date_issued):
        """Sets the date_issued of this GetContractsPublicRegionId200Ok.

        Сreation date of the contract  # noqa: E501

        :param date_issued: The date_issued of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and date_issued is None:
            raise ValueError("Invalid value for `date_issued`, must not be `None`")  # noqa: E501

        self._date_issued = date_issued

    @property
    def days_to_complete(self):
        """Gets the days_to_complete of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Number of days to perform the contract  # noqa: E501

        :return: The days_to_complete of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._days_to_complete

    @days_to_complete.setter
    def days_to_complete(self, days_to_complete):
        """Sets the days_to_complete of this GetContractsPublicRegionId200Ok.

        Number of days to perform the contract  # noqa: E501

        :param days_to_complete: The days_to_complete of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: int
        """

        self._days_to_complete = days_to_complete

    @property
    def end_location_id(self):
        """Gets the end_location_id of this GetContractsPublicRegionId200Ok.  # noqa: E501

        End location ID (for Couriers contract)  # noqa: E501

        :return: The end_location_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._end_location_id

    @end_location_id.setter
    def end_location_id(self, end_location_id):
        """Sets the end_location_id of this GetContractsPublicRegionId200Ok.

        End location ID (for Couriers contract)  # noqa: E501

        :param end_location_id: The end_location_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: int
        """

        self._end_location_id = end_location_id

    @property
    def for_corporation(self):
        """Gets the for_corporation of this GetContractsPublicRegionId200Ok.  # noqa: E501

        true if the contract was issued on behalf of the issuer's corporation  # noqa: E501

        :return: The for_corporation of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._for_corporation

    @for_corporation.setter
    def for_corporation(self, for_corporation):
        """Sets the for_corporation of this GetContractsPublicRegionId200Ok.

        true if the contract was issued on behalf of the issuer's corporation  # noqa: E501

        :param for_corporation: The for_corporation of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: bool
        """

        self._for_corporation = for_corporation

    @property
    def issuer_corporation_id(self):
        """Gets the issuer_corporation_id of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Character's corporation ID for the issuer  # noqa: E501

        :return: The issuer_corporation_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._issuer_corporation_id

    @issuer_corporation_id.setter
    def issuer_corporation_id(self, issuer_corporation_id):
        """Sets the issuer_corporation_id of this GetContractsPublicRegionId200Ok.

        Character's corporation ID for the issuer  # noqa: E501

        :param issuer_corporation_id: The issuer_corporation_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and issuer_corporation_id is None:
            raise ValueError("Invalid value for `issuer_corporation_id`, must not be `None`")  # noqa: E501

        self._issuer_corporation_id = issuer_corporation_id

    @property
    def issuer_id(self):
        """Gets the issuer_id of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Character ID for the issuer  # noqa: E501

        :return: The issuer_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this GetContractsPublicRegionId200Ok.

        Character ID for the issuer  # noqa: E501

        :param issuer_id: The issuer_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and issuer_id is None:
            raise ValueError("Invalid value for `issuer_id`, must not be `None`")  # noqa: E501

        self._issuer_id = issuer_id

    @property
    def price(self):
        """Gets the price of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Price of contract (for ItemsExchange and Auctions)  # noqa: E501

        :return: The price of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GetContractsPublicRegionId200Ok.

        Price of contract (for ItemsExchange and Auctions)  # noqa: E501

        :param price: The price of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def reward(self):
        """Gets the reward of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Remuneration for contract (for Couriers only)  # noqa: E501

        :return: The reward of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: float
        """
        return self._reward

    @reward.setter
    def reward(self, reward):
        """Sets the reward of this GetContractsPublicRegionId200Ok.

        Remuneration for contract (for Couriers only)  # noqa: E501

        :param reward: The reward of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: float
        """

        self._reward = reward

    @property
    def start_location_id(self):
        """Gets the start_location_id of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Start location ID (for Couriers contract)  # noqa: E501

        :return: The start_location_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._start_location_id

    @start_location_id.setter
    def start_location_id(self, start_location_id):
        """Sets the start_location_id of this GetContractsPublicRegionId200Ok.

        Start location ID (for Couriers contract)  # noqa: E501

        :param start_location_id: The start_location_id of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: int
        """

        self._start_location_id = start_location_id

    @property
    def title(self):
        """Gets the title of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Title of the contract  # noqa: E501

        :return: The title of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetContractsPublicRegionId200Ok.

        Title of the contract  # noqa: E501

        :param title: The title of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Type of the contract  # noqa: E501

        :return: The type of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetContractsPublicRegionId200Ok.

        Type of the contract  # noqa: E501

        :param type: The type of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "item_exchange", "auction", "courier", "loan"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def volume(self):
        """Gets the volume of this GetContractsPublicRegionId200Ok.  # noqa: E501

        Volume of items in the contract  # noqa: E501

        :return: The volume of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GetContractsPublicRegionId200Ok.

        Volume of items in the contract  # noqa: E501

        :param volume: The volume of this GetContractsPublicRegionId200Ok.  # noqa: E501
        :type: float
        """

        self._volume = volume

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
        if issubclass(GetContractsPublicRegionId200Ok, dict):
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
        if not isinstance(other, GetContractsPublicRegionId200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetContractsPublicRegionId200Ok):
            return True

        return self.to_dict() != other.to_dict()
