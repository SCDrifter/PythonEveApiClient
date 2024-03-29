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


class GetCorporationsCorporationIdWalletsDivisionTransactions200Ok(object):
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
        'client_id': 'int',
        '_date': 'datetime',
        'is_buy': 'bool',
        'journal_ref_id': 'int',
        'location_id': 'int',
        'quantity': 'int',
        'transaction_id': 'int',
        'type_id': 'int',
        'unit_price': 'float'
    }

    attribute_map = {
        'client_id': 'client_id',
        '_date': 'date',
        'is_buy': 'is_buy',
        'journal_ref_id': 'journal_ref_id',
        'location_id': 'location_id',
        'quantity': 'quantity',
        'transaction_id': 'transaction_id',
        'type_id': 'type_id',
        'unit_price': 'unit_price'
    }

    def __init__(self, client_id=None, _date=None, is_buy=None, journal_ref_id=None, location_id=None, quantity=None, transaction_id=None, type_id=None, unit_price=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdWalletsDivisionTransactions200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_id = None
        self.__date = None
        self._is_buy = None
        self._journal_ref_id = None
        self._location_id = None
        self._quantity = None
        self._transaction_id = None
        self._type_id = None
        self._unit_price = None
        self.discriminator = None

        self.client_id = client_id
        self._date = _date
        self.is_buy = is_buy
        self.journal_ref_id = journal_ref_id
        self.location_id = location_id
        self.quantity = quantity
        self.transaction_id = transaction_id
        self.type_id = type_id
        self.unit_price = unit_price

    @property
    def client_id(self):
        """Gets the client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        client_id integer  # noqa: E501

        :return: The client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        client_id integer  # noqa: E501

        :param client_id: The client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def _date(self):
        """Gets the _date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        Date and time of transaction  # noqa: E501

        :return: The _date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        Date and time of transaction  # noqa: E501

        :param _date: The _date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def is_buy(self):
        """Gets the is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        is_buy boolean  # noqa: E501

        :return: The is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_buy

    @is_buy.setter
    def is_buy(self, is_buy):
        """Sets the is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        is_buy boolean  # noqa: E501

        :param is_buy: The is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_buy is None:
            raise ValueError("Invalid value for `is_buy`, must not be `None`")  # noqa: E501

        self._is_buy = is_buy

    @property
    def journal_ref_id(self):
        """Gets the journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        -1 if there is no corresponding wallet journal entry  # noqa: E501

        :return: The journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._journal_ref_id

    @journal_ref_id.setter
    def journal_ref_id(self, journal_ref_id):
        """Sets the journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        -1 if there is no corresponding wallet journal entry  # noqa: E501

        :param journal_ref_id: The journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and journal_ref_id is None:
            raise ValueError("Invalid value for `journal_ref_id`, must not be `None`")  # noqa: E501

        self._journal_ref_id = journal_ref_id

    @property
    def location_id(self):
        """Gets the location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def quantity(self):
        """Gets the quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def transaction_id(self):
        """Gets the transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        Unique transaction ID  # noqa: E501

        :return: The transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        Unique transaction ID  # noqa: E501

        :param transaction_id: The transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def unit_price(self):
        """Gets the unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501

        Amount paid per unit  # noqa: E501

        :return: The unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.

        Amount paid per unit  # noqa: E501

        :param unit_price: The unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

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
        if issubclass(GetCorporationsCorporationIdWalletsDivisionTransactions200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdWalletsDivisionTransactions200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdWalletsDivisionTransactions200Ok):
            return True

        return self.to_dict() != other.to_dict()
