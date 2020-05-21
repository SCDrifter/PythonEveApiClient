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


class GetContractsPublicBidsContractId200Ok(object):
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
        'amount': 'float',
        'bid_id': 'int',
        'date_bid': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'bid_id': 'bid_id',
        'date_bid': 'date_bid'
    }

    def __init__(self, amount=None, bid_id=None, date_bid=None):  # noqa: E501
        """GetContractsPublicBidsContractId200Ok - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._bid_id = None
        self._date_bid = None
        self.discriminator = None

        self.amount = amount
        self.bid_id = bid_id
        self.date_bid = date_bid

    @property
    def amount(self):
        """Gets the amount of this GetContractsPublicBidsContractId200Ok.  # noqa: E501

        The amount bid, in ISK  # noqa: E501

        :return: The amount of this GetContractsPublicBidsContractId200Ok.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetContractsPublicBidsContractId200Ok.

        The amount bid, in ISK  # noqa: E501

        :param amount: The amount of this GetContractsPublicBidsContractId200Ok.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def bid_id(self):
        """Gets the bid_id of this GetContractsPublicBidsContractId200Ok.  # noqa: E501

        Unique ID for the bid  # noqa: E501

        :return: The bid_id of this GetContractsPublicBidsContractId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._bid_id

    @bid_id.setter
    def bid_id(self, bid_id):
        """Sets the bid_id of this GetContractsPublicBidsContractId200Ok.

        Unique ID for the bid  # noqa: E501

        :param bid_id: The bid_id of this GetContractsPublicBidsContractId200Ok.  # noqa: E501
        :type: int
        """
        if bid_id is None:
            raise ValueError("Invalid value for `bid_id`, must not be `None`")  # noqa: E501

        self._bid_id = bid_id

    @property
    def date_bid(self):
        """Gets the date_bid of this GetContractsPublicBidsContractId200Ok.  # noqa: E501

        Datetime when the bid was placed  # noqa: E501

        :return: The date_bid of this GetContractsPublicBidsContractId200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._date_bid

    @date_bid.setter
    def date_bid(self, date_bid):
        """Sets the date_bid of this GetContractsPublicBidsContractId200Ok.

        Datetime when the bid was placed  # noqa: E501

        :param date_bid: The date_bid of this GetContractsPublicBidsContractId200Ok.  # noqa: E501
        :type: datetime
        """
        if date_bid is None:
            raise ValueError("Invalid value for `date_bid`, must not be `None`")  # noqa: E501

        self._date_bid = date_bid

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
        if issubclass(GetContractsPublicBidsContractId200Ok, dict):
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
        if not isinstance(other, GetContractsPublicBidsContractId200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other