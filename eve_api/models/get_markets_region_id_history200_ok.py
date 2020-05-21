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


class GetMarketsRegionIdHistory200Ok(object):
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
        'average': 'float',
        '_date': 'date',
        'highest': 'float',
        'lowest': 'float',
        'order_count': 'int',
        'volume': 'int'
    }

    attribute_map = {
        'average': 'average',
        '_date': 'date',
        'highest': 'highest',
        'lowest': 'lowest',
        'order_count': 'order_count',
        'volume': 'volume'
    }

    def __init__(self, average=None, _date=None, highest=None, lowest=None, order_count=None, volume=None):  # noqa: E501
        """GetMarketsRegionIdHistory200Ok - a model defined in Swagger"""  # noqa: E501

        self._average = None
        self.__date = None
        self._highest = None
        self._lowest = None
        self._order_count = None
        self._volume = None
        self.discriminator = None

        self.average = average
        self._date = _date
        self.highest = highest
        self.lowest = lowest
        self.order_count = order_count
        self.volume = volume

    @property
    def average(self):
        """Gets the average of this GetMarketsRegionIdHistory200Ok.  # noqa: E501

        average number  # noqa: E501

        :return: The average of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this GetMarketsRegionIdHistory200Ok.

        average number  # noqa: E501

        :param average: The average of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :type: float
        """
        if average is None:
            raise ValueError("Invalid value for `average`, must not be `None`")  # noqa: E501

        self._average = average

    @property
    def _date(self):
        """Gets the _date of this GetMarketsRegionIdHistory200Ok.  # noqa: E501

        The date of this historical statistic entry  # noqa: E501

        :return: The _date of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetMarketsRegionIdHistory200Ok.

        The date of this historical statistic entry  # noqa: E501

        :param _date: The _date of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def highest(self):
        """Gets the highest of this GetMarketsRegionIdHistory200Ok.  # noqa: E501

        highest number  # noqa: E501

        :return: The highest of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :rtype: float
        """
        return self._highest

    @highest.setter
    def highest(self, highest):
        """Sets the highest of this GetMarketsRegionIdHistory200Ok.

        highest number  # noqa: E501

        :param highest: The highest of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :type: float
        """
        if highest is None:
            raise ValueError("Invalid value for `highest`, must not be `None`")  # noqa: E501

        self._highest = highest

    @property
    def lowest(self):
        """Gets the lowest of this GetMarketsRegionIdHistory200Ok.  # noqa: E501

        lowest number  # noqa: E501

        :return: The lowest of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :rtype: float
        """
        return self._lowest

    @lowest.setter
    def lowest(self, lowest):
        """Sets the lowest of this GetMarketsRegionIdHistory200Ok.

        lowest number  # noqa: E501

        :param lowest: The lowest of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :type: float
        """
        if lowest is None:
            raise ValueError("Invalid value for `lowest`, must not be `None`")  # noqa: E501

        self._lowest = lowest

    @property
    def order_count(self):
        """Gets the order_count of this GetMarketsRegionIdHistory200Ok.  # noqa: E501

        Total number of orders happened that day  # noqa: E501

        :return: The order_count of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """Sets the order_count of this GetMarketsRegionIdHistory200Ok.

        Total number of orders happened that day  # noqa: E501

        :param order_count: The order_count of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :type: int
        """
        if order_count is None:
            raise ValueError("Invalid value for `order_count`, must not be `None`")  # noqa: E501

        self._order_count = order_count

    @property
    def volume(self):
        """Gets the volume of this GetMarketsRegionIdHistory200Ok.  # noqa: E501

        Total  # noqa: E501

        :return: The volume of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GetMarketsRegionIdHistory200Ok.

        Total  # noqa: E501

        :param volume: The volume of this GetMarketsRegionIdHistory200Ok.  # noqa: E501
        :type: int
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

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
        if issubclass(GetMarketsRegionIdHistory200Ok, dict):
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
        if not isinstance(other, GetMarketsRegionIdHistory200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other