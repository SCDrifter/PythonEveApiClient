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


class GetKillmailsKillmailIdKillmailHashVictim(object):
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
        'alliance_id': 'int',
        'character_id': 'int',
        'corporation_id': 'int',
        'damage_taken': 'int',
        'faction_id': 'int',
        'items': 'list[GetKillmailsKillmailIdKillmailHashItem]',
        'position': 'GetKillmailsKillmailIdKillmailHashPosition',
        'ship_type_id': 'int'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'character_id': 'character_id',
        'corporation_id': 'corporation_id',
        'damage_taken': 'damage_taken',
        'faction_id': 'faction_id',
        'items': 'items',
        'position': 'position',
        'ship_type_id': 'ship_type_id'
    }

    def __init__(self, alliance_id=None, character_id=None, corporation_id=None, damage_taken=None, faction_id=None, items=None, position=None, ship_type_id=None, _configuration=None):  # noqa: E501
        """GetKillmailsKillmailIdKillmailHashVictim - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alliance_id = None
        self._character_id = None
        self._corporation_id = None
        self._damage_taken = None
        self._faction_id = None
        self._items = None
        self._position = None
        self._ship_type_id = None
        self.discriminator = None

        if alliance_id is not None:
            self.alliance_id = alliance_id
        if character_id is not None:
            self.character_id = character_id
        if corporation_id is not None:
            self.corporation_id = corporation_id
        self.damage_taken = damage_taken
        if faction_id is not None:
            self.faction_id = faction_id
        if items is not None:
            self.items = items
        if position is not None:
            self.position = position
        self.ship_type_id = ship_type_id

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        alliance_id integer  # noqa: E501

        :return: The alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.

        alliance_id integer  # noqa: E501

        :param alliance_id: The alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def character_id(self):
        """Gets the character_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetKillmailsKillmailIdKillmailHashVictim.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: int
        """

        self._character_id = character_id

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def damage_taken(self):
        """Gets the damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        How much total damage was taken by the victim   # noqa: E501

        :return: The damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: int
        """
        return self._damage_taken

    @damage_taken.setter
    def damage_taken(self, damage_taken):
        """Sets the damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.

        How much total damage was taken by the victim   # noqa: E501

        :param damage_taken: The damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and damage_taken is None:
            raise ValueError("Invalid value for `damage_taken`, must not be `None`")  # noqa: E501

        self._damage_taken = damage_taken

    @property
    def faction_id(self):
        """Gets the faction_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        faction_id integer  # noqa: E501

        :return: The faction_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetKillmailsKillmailIdKillmailHashVictim.

        faction_id integer  # noqa: E501

        :param faction_id: The faction_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: int
        """

        self._faction_id = faction_id

    @property
    def items(self):
        """Gets the items of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        items array  # noqa: E501

        :return: The items of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: list[GetKillmailsKillmailIdKillmailHashItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GetKillmailsKillmailIdKillmailHashVictim.

        items array  # noqa: E501

        :param items: The items of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: list[GetKillmailsKillmailIdKillmailHashItem]
        """

        self._items = items

    @property
    def position(self):
        """Gets the position of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501


        :return: The position of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: GetKillmailsKillmailIdKillmailHashPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GetKillmailsKillmailIdKillmailHashVictim.


        :param position: The position of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: GetKillmailsKillmailIdKillmailHashPosition
        """

        self._position = position

    @property
    def ship_type_id(self):
        """Gets the ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501

        The ship that the victim was piloting and was destroyed   # noqa: E501

        :return: The ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """Sets the ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.

        The ship that the victim was piloting and was destroyed   # noqa: E501

        :param ship_type_id: The ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ship_type_id is None:
            raise ValueError("Invalid value for `ship_type_id`, must not be `None`")  # noqa: E501

        self._ship_type_id = ship_type_id

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
        if issubclass(GetKillmailsKillmailIdKillmailHashVictim, dict):
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
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashVictim):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashVictim):
            return True

        return self.to_dict() != other.to_dict()
