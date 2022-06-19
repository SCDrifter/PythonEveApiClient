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


class GetKillmailsKillmailIdKillmailHashItem(object):
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
        'flag': 'int',
        'item_type_id': 'int',
        'items': 'list[GetKillmailsKillmailIdKillmailHashItemsItem]',
        'quantity_destroyed': 'int',
        'quantity_dropped': 'int',
        'singleton': 'int'
    }

    attribute_map = {
        'flag': 'flag',
        'item_type_id': 'item_type_id',
        'items': 'items',
        'quantity_destroyed': 'quantity_destroyed',
        'quantity_dropped': 'quantity_dropped',
        'singleton': 'singleton'
    }

    def __init__(self, flag=None, item_type_id=None, items=None, quantity_destroyed=None, quantity_dropped=None, singleton=None, _configuration=None):  # noqa: E501
        """GetKillmailsKillmailIdKillmailHashItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._flag = None
        self._item_type_id = None
        self._items = None
        self._quantity_destroyed = None
        self._quantity_dropped = None
        self._singleton = None
        self.discriminator = None

        self.flag = flag
        self.item_type_id = item_type_id
        if items is not None:
            self.items = items
        if quantity_destroyed is not None:
            self.quantity_destroyed = quantity_destroyed
        if quantity_dropped is not None:
            self.quantity_dropped = quantity_dropped
        self.singleton = singleton

    @property
    def flag(self):
        """Gets the flag of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501

        Flag for the location of the item   # noqa: E501

        :return: The flag of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :rtype: int
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this GetKillmailsKillmailIdKillmailHashItem.

        Flag for the location of the item   # noqa: E501

        :param flag: The flag of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and flag is None:
            raise ValueError("Invalid value for `flag`, must not be `None`")  # noqa: E501

        self._flag = flag

    @property
    def item_type_id(self):
        """Gets the item_type_id of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501

        item_type_id integer  # noqa: E501

        :return: The item_type_id of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :rtype: int
        """
        return self._item_type_id

    @item_type_id.setter
    def item_type_id(self, item_type_id):
        """Sets the item_type_id of this GetKillmailsKillmailIdKillmailHashItem.

        item_type_id integer  # noqa: E501

        :param item_type_id: The item_type_id of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and item_type_id is None:
            raise ValueError("Invalid value for `item_type_id`, must not be `None`")  # noqa: E501

        self._item_type_id = item_type_id

    @property
    def items(self):
        """Gets the items of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501

        items array  # noqa: E501

        :return: The items of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :rtype: list[GetKillmailsKillmailIdKillmailHashItemsItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GetKillmailsKillmailIdKillmailHashItem.

        items array  # noqa: E501

        :param items: The items of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :type: list[GetKillmailsKillmailIdKillmailHashItemsItem]
        """

        self._items = items

    @property
    def quantity_destroyed(self):
        """Gets the quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501

        How many of the item were destroyed if any   # noqa: E501

        :return: The quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity_destroyed

    @quantity_destroyed.setter
    def quantity_destroyed(self, quantity_destroyed):
        """Sets the quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem.

        How many of the item were destroyed if any   # noqa: E501

        :param quantity_destroyed: The quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :type: int
        """

        self._quantity_destroyed = quantity_destroyed

    @property
    def quantity_dropped(self):
        """Gets the quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501

        How many of the item were dropped if any   # noqa: E501

        :return: The quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity_dropped

    @quantity_dropped.setter
    def quantity_dropped(self, quantity_dropped):
        """Sets the quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem.

        How many of the item were dropped if any   # noqa: E501

        :param quantity_dropped: The quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :type: int
        """

        self._quantity_dropped = quantity_dropped

    @property
    def singleton(self):
        """Gets the singleton of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501

        singleton integer  # noqa: E501

        :return: The singleton of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :rtype: int
        """
        return self._singleton

    @singleton.setter
    def singleton(self, singleton):
        """Sets the singleton of this GetKillmailsKillmailIdKillmailHashItem.

        singleton integer  # noqa: E501

        :param singleton: The singleton of this GetKillmailsKillmailIdKillmailHashItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and singleton is None:
            raise ValueError("Invalid value for `singleton`, must not be `None`")  # noqa: E501

        self._singleton = singleton

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
        if issubclass(GetKillmailsKillmailIdKillmailHashItem, dict):
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
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashItem):
            return True

        return self.to_dict() != other.to_dict()
