# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCorporationCorporationIdMiningObserversObserverId200Ok(object):
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
        'character_id': 'int',
        'last_updated': 'date',
        'quantity': 'int',
        'recorded_corporation_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'character_id': 'character_id',
        'last_updated': 'last_updated',
        'quantity': 'quantity',
        'recorded_corporation_id': 'recorded_corporation_id',
        'type_id': 'type_id'
    }

    def __init__(self, character_id=None, last_updated=None, quantity=None, recorded_corporation_id=None, type_id=None):  # noqa: E501
        """GetCorporationCorporationIdMiningObserversObserverId200Ok - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._last_updated = None
        self._quantity = None
        self._recorded_corporation_id = None
        self._type_id = None
        self.discriminator = None

        self.character_id = character_id
        self.last_updated = last_updated
        self.quantity = quantity
        self.recorded_corporation_id = recorded_corporation_id
        self.type_id = type_id

    @property
    def character_id(self):
        """Gets the character_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501

        The character that did the mining   # noqa: E501

        :return: The character_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.

        The character that did the mining   # noqa: E501

        :param character_id: The character_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def last_updated(self):
        """Gets the last_updated of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501

        last_updated string  # noqa: E501

        :return: The last_updated of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :rtype: date
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this GetCorporationCorporationIdMiningObserversObserverId200Ok.

        last_updated string  # noqa: E501

        :param last_updated: The last_updated of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :type: date
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def quantity(self):
        """Gets the quantity of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCorporationCorporationIdMiningObserversObserverId200Ok.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def recorded_corporation_id(self):
        """Gets the recorded_corporation_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501

        The corporation id of the character at the time data was recorded.   # noqa: E501

        :return: The recorded_corporation_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._recorded_corporation_id

    @recorded_corporation_id.setter
    def recorded_corporation_id(self, recorded_corporation_id):
        """Sets the recorded_corporation_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.

        The corporation id of the character at the time data was recorded.   # noqa: E501

        :param recorded_corporation_id: The recorded_corporation_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :type: int
        """
        if recorded_corporation_id is None:
            raise ValueError("Invalid value for `recorded_corporation_id`, must not be `None`")  # noqa: E501

        self._recorded_corporation_id = recorded_corporation_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCorporationCorporationIdMiningObserversObserverId200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

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
        if issubclass(GetCorporationCorporationIdMiningObserversObserverId200Ok, dict):
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
        if not isinstance(other, GetCorporationCorporationIdMiningObserversObserverId200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
