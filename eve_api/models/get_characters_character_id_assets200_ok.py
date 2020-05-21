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


class GetCharactersCharacterIdAssets200Ok(object):
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
        'is_blueprint_copy': 'bool',
        'is_singleton': 'bool',
        'item_id': 'int',
        'location_flag': 'str',
        'location_id': 'int',
        'location_type': 'str',
        'quantity': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'is_blueprint_copy': 'is_blueprint_copy',
        'is_singleton': 'is_singleton',
        'item_id': 'item_id',
        'location_flag': 'location_flag',
        'location_id': 'location_id',
        'location_type': 'location_type',
        'quantity': 'quantity',
        'type_id': 'type_id'
    }

    def __init__(self, is_blueprint_copy=None, is_singleton=None, item_id=None, location_flag=None, location_id=None, location_type=None, quantity=None, type_id=None):  # noqa: E501
        """GetCharactersCharacterIdAssets200Ok - a model defined in Swagger"""  # noqa: E501

        self._is_blueprint_copy = None
        self._is_singleton = None
        self._item_id = None
        self._location_flag = None
        self._location_id = None
        self._location_type = None
        self._quantity = None
        self._type_id = None
        self.discriminator = None

        if is_blueprint_copy is not None:
            self.is_blueprint_copy = is_blueprint_copy
        self.is_singleton = is_singleton
        self.item_id = item_id
        self.location_flag = location_flag
        self.location_id = location_id
        self.location_type = location_type
        self.quantity = quantity
        self.type_id = type_id

    @property
    def is_blueprint_copy(self):
        """Gets the is_blueprint_copy of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        is_blueprint_copy boolean  # noqa: E501

        :return: The is_blueprint_copy of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_blueprint_copy

    @is_blueprint_copy.setter
    def is_blueprint_copy(self, is_blueprint_copy):
        """Sets the is_blueprint_copy of this GetCharactersCharacterIdAssets200Ok.

        is_blueprint_copy boolean  # noqa: E501

        :param is_blueprint_copy: The is_blueprint_copy of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: bool
        """

        self._is_blueprint_copy = is_blueprint_copy

    @property
    def is_singleton(self):
        """Gets the is_singleton of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        is_singleton boolean  # noqa: E501

        :return: The is_singleton of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_singleton

    @is_singleton.setter
    def is_singleton(self, is_singleton):
        """Sets the is_singleton of this GetCharactersCharacterIdAssets200Ok.

        is_singleton boolean  # noqa: E501

        :param is_singleton: The is_singleton of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: bool
        """
        if is_singleton is None:
            raise ValueError("Invalid value for `is_singleton`, must not be `None`")  # noqa: E501

        self._is_singleton = is_singleton

    @property
    def item_id(self):
        """Gets the item_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        item_id integer  # noqa: E501

        :return: The item_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this GetCharactersCharacterIdAssets200Ok.

        item_id integer  # noqa: E501

        :param item_id: The item_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if item_id is None:
            raise ValueError("Invalid value for `item_id`, must not be `None`")  # noqa: E501

        self._item_id = item_id

    @property
    def location_flag(self):
        """Gets the location_flag of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        location_flag string  # noqa: E501

        :return: The location_flag of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: str
        """
        return self._location_flag

    @location_flag.setter
    def location_flag(self, location_flag):
        """Sets the location_flag of this GetCharactersCharacterIdAssets200Ok.

        location_flag string  # noqa: E501

        :param location_flag: The location_flag of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: str
        """
        if location_flag is None:
            raise ValueError("Invalid value for `location_flag`, must not be `None`")  # noqa: E501
        allowed_values = ["AssetSafety", "AutoFit", "BoosterBay", "Cargo", "CorpseBay", "Deliveries", "DroneBay", "FighterBay", "FighterTube0", "FighterTube1", "FighterTube2", "FighterTube3", "FighterTube4", "FleetHangar", "FrigateEscapeBay", "Hangar", "HangarAll", "HiSlot0", "HiSlot1", "HiSlot2", "HiSlot3", "HiSlot4", "HiSlot5", "HiSlot6", "HiSlot7", "HiddenModifiers", "Implant", "LoSlot0", "LoSlot1", "LoSlot2", "LoSlot3", "LoSlot4", "LoSlot5", "LoSlot6", "LoSlot7", "Locked", "MedSlot0", "MedSlot1", "MedSlot2", "MedSlot3", "MedSlot4", "MedSlot5", "MedSlot6", "MedSlot7", "QuafeBay", "RigSlot0", "RigSlot1", "RigSlot2", "RigSlot3", "RigSlot4", "RigSlot5", "RigSlot6", "RigSlot7", "ShipHangar", "Skill", "SpecializedAmmoHold", "SpecializedCommandCenterHold", "SpecializedFuelBay", "SpecializedGasHold", "SpecializedIndustrialShipHold", "SpecializedLargeShipHold", "SpecializedMaterialBay", "SpecializedMediumShipHold", "SpecializedMineralHold", "SpecializedOreHold", "SpecializedPlanetaryCommoditiesHold", "SpecializedSalvageHold", "SpecializedShipHold", "SpecializedSmallShipHold", "SubSystemBay", "SubSystemSlot0", "SubSystemSlot1", "SubSystemSlot2", "SubSystemSlot3", "SubSystemSlot4", "SubSystemSlot5", "SubSystemSlot6", "SubSystemSlot7", "Unlocked", "Wardrobe"]  # noqa: E501
        if location_flag not in allowed_values:
            raise ValueError(
                "Invalid value for `location_flag` ({0}), must be one of {1}"  # noqa: E501
                .format(location_flag, allowed_values)
            )

        self._location_flag = location_flag

    @property
    def location_id(self):
        """Gets the location_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCharactersCharacterIdAssets200Ok.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def location_type(self):
        """Gets the location_type of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        location_type string  # noqa: E501

        :return: The location_type of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this GetCharactersCharacterIdAssets200Ok.

        location_type string  # noqa: E501

        :param location_type: The location_type of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: str
        """
        if location_type is None:
            raise ValueError("Invalid value for `location_type`, must not be `None`")  # noqa: E501
        allowed_values = ["station", "solar_system", "item", "other"]  # noqa: E501
        if location_type not in allowed_values:
            raise ValueError(
                "Invalid value for `location_type` ({0}), must be one of {1}"  # noqa: E501
                .format(location_type, allowed_values)
            )

        self._location_type = location_type

    @property
    def quantity(self):
        """Gets the quantity of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCharactersCharacterIdAssets200Ok.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def type_id(self):
        """Gets the type_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCharactersCharacterIdAssets200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCharactersCharacterIdAssets200Ok.  # noqa: E501
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
        if issubclass(GetCharactersCharacterIdAssets200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdAssets200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
