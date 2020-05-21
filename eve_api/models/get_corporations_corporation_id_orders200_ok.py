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


class GetCorporationsCorporationIdOrders200Ok(object):
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
        'duration': 'int',
        'escrow': 'float',
        'is_buy_order': 'bool',
        'issued': 'datetime',
        'issued_by': 'int',
        'location_id': 'int',
        'min_volume': 'int',
        'order_id': 'int',
        'price': 'float',
        'range': 'str',
        'region_id': 'int',
        'type_id': 'int',
        'volume_remain': 'int',
        'volume_total': 'int',
        'wallet_division': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'escrow': 'escrow',
        'is_buy_order': 'is_buy_order',
        'issued': 'issued',
        'issued_by': 'issued_by',
        'location_id': 'location_id',
        'min_volume': 'min_volume',
        'order_id': 'order_id',
        'price': 'price',
        'range': 'range',
        'region_id': 'region_id',
        'type_id': 'type_id',
        'volume_remain': 'volume_remain',
        'volume_total': 'volume_total',
        'wallet_division': 'wallet_division'
    }

    def __init__(self, duration=None, escrow=None, is_buy_order=None, issued=None, issued_by=None, location_id=None, min_volume=None, order_id=None, price=None, range=None, region_id=None, type_id=None, volume_remain=None, volume_total=None, wallet_division=None):  # noqa: E501
        """GetCorporationsCorporationIdOrders200Ok - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._escrow = None
        self._is_buy_order = None
        self._issued = None
        self._issued_by = None
        self._location_id = None
        self._min_volume = None
        self._order_id = None
        self._price = None
        self._range = None
        self._region_id = None
        self._type_id = None
        self._volume_remain = None
        self._volume_total = None
        self._wallet_division = None
        self.discriminator = None

        self.duration = duration
        if escrow is not None:
            self.escrow = escrow
        if is_buy_order is not None:
            self.is_buy_order = is_buy_order
        self.issued = issued
        self.issued_by = issued_by
        self.location_id = location_id
        if min_volume is not None:
            self.min_volume = min_volume
        self.order_id = order_id
        self.price = price
        self.range = range
        self.region_id = region_id
        self.type_id = type_id
        self.volume_remain = volume_remain
        self.volume_total = volume_total
        self.wallet_division = wallet_division

    @property
    def duration(self):
        """Gets the duration of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Number of days for which order is valid (starting from the issued date). An order expires at time issued + duration  # noqa: E501

        :return: The duration of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GetCorporationsCorporationIdOrders200Ok.

        Number of days for which order is valid (starting from the issued date). An order expires at time issued + duration  # noqa: E501

        :param duration: The duration of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def escrow(self):
        """Gets the escrow of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        For buy orders, the amount of ISK in escrow  # noqa: E501

        :return: The escrow of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: float
        """
        return self._escrow

    @escrow.setter
    def escrow(self, escrow):
        """Sets the escrow of this GetCorporationsCorporationIdOrders200Ok.

        For buy orders, the amount of ISK in escrow  # noqa: E501

        :param escrow: The escrow of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: float
        """

        self._escrow = escrow

    @property
    def is_buy_order(self):
        """Gets the is_buy_order of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        True if the order is a bid (buy) order  # noqa: E501

        :return: The is_buy_order of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_buy_order

    @is_buy_order.setter
    def is_buy_order(self, is_buy_order):
        """Sets the is_buy_order of this GetCorporationsCorporationIdOrders200Ok.

        True if the order is a bid (buy) order  # noqa: E501

        :param is_buy_order: The is_buy_order of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: bool
        """

        self._is_buy_order = is_buy_order

    @property
    def issued(self):
        """Gets the issued of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Date and time when this order was issued  # noqa: E501

        :return: The issued of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """Sets the issued of this GetCorporationsCorporationIdOrders200Ok.

        Date and time when this order was issued  # noqa: E501

        :param issued: The issued of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: datetime
        """
        if issued is None:
            raise ValueError("Invalid value for `issued`, must not be `None`")  # noqa: E501

        self._issued = issued

    @property
    def issued_by(self):
        """Gets the issued_by of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        The character who issued this order  # noqa: E501

        :return: The issued_by of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """Sets the issued_by of this GetCorporationsCorporationIdOrders200Ok.

        The character who issued this order  # noqa: E501

        :param issued_by: The issued_by of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if issued_by is None:
            raise ValueError("Invalid value for `issued_by`, must not be `None`")  # noqa: E501

        self._issued_by = issued_by

    @property
    def location_id(self):
        """Gets the location_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        ID of the location where order was placed  # noqa: E501

        :return: The location_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCorporationsCorporationIdOrders200Ok.

        ID of the location where order was placed  # noqa: E501

        :param location_id: The location_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def min_volume(self):
        """Gets the min_volume of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        For buy orders, the minimum quantity that will be accepted in a matching sell order  # noqa: E501

        :return: The min_volume of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._min_volume

    @min_volume.setter
    def min_volume(self, min_volume):
        """Sets the min_volume of this GetCorporationsCorporationIdOrders200Ok.

        For buy orders, the minimum quantity that will be accepted in a matching sell order  # noqa: E501

        :param min_volume: The min_volume of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """

        self._min_volume = min_volume

    @property
    def order_id(self):
        """Gets the order_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Unique order ID  # noqa: E501

        :return: The order_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this GetCorporationsCorporationIdOrders200Ok.

        Unique order ID  # noqa: E501

        :param order_id: The order_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def price(self):
        """Gets the price of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Cost per unit for this order  # noqa: E501

        :return: The price of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GetCorporationsCorporationIdOrders200Ok.

        Cost per unit for this order  # noqa: E501

        :param price: The price of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def range(self):
        """Gets the range of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Valid order range, numbers are ranges in jumps  # noqa: E501

        :return: The range of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetCorporationsCorporationIdOrders200Ok.

        Valid order range, numbers are ranges in jumps  # noqa: E501

        :param range: The range of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: str
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        allowed_values = ["1", "10", "2", "20", "3", "30", "4", "40", "5", "region", "solarsystem", "station"]  # noqa: E501
        if range not in allowed_values:
            raise ValueError(
                "Invalid value for `range` ({0}), must be one of {1}"  # noqa: E501
                .format(range, allowed_values)
            )

        self._range = range

    @property
    def region_id(self):
        """Gets the region_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        ID of the region where order was placed  # noqa: E501

        :return: The region_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this GetCorporationsCorporationIdOrders200Ok.

        ID of the region where order was placed  # noqa: E501

        :param region_id: The region_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        The type ID of the item transacted in this order  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdOrders200Ok.

        The type ID of the item transacted in this order  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def volume_remain(self):
        """Gets the volume_remain of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Quantity of items still required or offered  # noqa: E501

        :return: The volume_remain of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._volume_remain

    @volume_remain.setter
    def volume_remain(self, volume_remain):
        """Sets the volume_remain of this GetCorporationsCorporationIdOrders200Ok.

        Quantity of items still required or offered  # noqa: E501

        :param volume_remain: The volume_remain of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if volume_remain is None:
            raise ValueError("Invalid value for `volume_remain`, must not be `None`")  # noqa: E501

        self._volume_remain = volume_remain

    @property
    def volume_total(self):
        """Gets the volume_total of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        Quantity of items required or offered at time order was placed  # noqa: E501

        :return: The volume_total of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._volume_total

    @volume_total.setter
    def volume_total(self, volume_total):
        """Sets the volume_total of this GetCorporationsCorporationIdOrders200Ok.

        Quantity of items required or offered at time order was placed  # noqa: E501

        :param volume_total: The volume_total of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if volume_total is None:
            raise ValueError("Invalid value for `volume_total`, must not be `None`")  # noqa: E501

        self._volume_total = volume_total

    @property
    def wallet_division(self):
        """Gets the wallet_division of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501

        The corporation wallet division used for this order.  # noqa: E501

        :return: The wallet_division of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._wallet_division

    @wallet_division.setter
    def wallet_division(self, wallet_division):
        """Sets the wallet_division of this GetCorporationsCorporationIdOrders200Ok.

        The corporation wallet division used for this order.  # noqa: E501

        :param wallet_division: The wallet_division of this GetCorporationsCorporationIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if wallet_division is None:
            raise ValueError("Invalid value for `wallet_division`, must not be `None`")  # noqa: E501
        if wallet_division is not None and wallet_division > 7:  # noqa: E501
            raise ValueError("Invalid value for `wallet_division`, must be a value less than or equal to `7`")  # noqa: E501
        if wallet_division is not None and wallet_division < 1:  # noqa: E501
            raise ValueError("Invalid value for `wallet_division`, must be a value greater than or equal to `1`")  # noqa: E501

        self._wallet_division = wallet_division

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
        if issubclass(GetCorporationsCorporationIdOrders200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdOrders200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
