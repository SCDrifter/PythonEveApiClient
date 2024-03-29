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


class GetCorporationsCorporationIdContainersLogs200Ok(object):
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
        'action': 'str',
        'character_id': 'int',
        'container_id': 'int',
        'container_type_id': 'int',
        'location_flag': 'str',
        'location_id': 'int',
        'logged_at': 'datetime',
        'new_config_bitmask': 'int',
        'old_config_bitmask': 'int',
        'password_type': 'str',
        'quantity': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'action': 'action',
        'character_id': 'character_id',
        'container_id': 'container_id',
        'container_type_id': 'container_type_id',
        'location_flag': 'location_flag',
        'location_id': 'location_id',
        'logged_at': 'logged_at',
        'new_config_bitmask': 'new_config_bitmask',
        'old_config_bitmask': 'old_config_bitmask',
        'password_type': 'password_type',
        'quantity': 'quantity',
        'type_id': 'type_id'
    }

    def __init__(self, action=None, character_id=None, container_id=None, container_type_id=None, location_flag=None, location_id=None, logged_at=None, new_config_bitmask=None, old_config_bitmask=None, password_type=None, quantity=None, type_id=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdContainersLogs200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._character_id = None
        self._container_id = None
        self._container_type_id = None
        self._location_flag = None
        self._location_id = None
        self._logged_at = None
        self._new_config_bitmask = None
        self._old_config_bitmask = None
        self._password_type = None
        self._quantity = None
        self._type_id = None
        self.discriminator = None

        self.action = action
        self.character_id = character_id
        self.container_id = container_id
        self.container_type_id = container_type_id
        self.location_flag = location_flag
        self.location_id = location_id
        self.logged_at = logged_at
        if new_config_bitmask is not None:
            self.new_config_bitmask = new_config_bitmask
        if old_config_bitmask is not None:
            self.old_config_bitmask = old_config_bitmask
        if password_type is not None:
            self.password_type = password_type
        if quantity is not None:
            self.quantity = quantity
        if type_id is not None:
            self.type_id = type_id

    @property
    def action(self):
        """Gets the action of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        action string  # noqa: E501

        :return: The action of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GetCorporationsCorporationIdContainersLogs200Ok.

        action string  # noqa: E501

        :param action: The action of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["add", "assemble", "configure", "enter_password", "lock", "move", "repackage", "set_name", "set_password", "unlock"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def character_id(self):
        """Gets the character_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        ID of the character who performed the action.  # noqa: E501

        :return: The character_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetCorporationsCorporationIdContainersLogs200Ok.

        ID of the character who performed the action.  # noqa: E501

        :param character_id: The character_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def container_id(self):
        """Gets the container_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        ID of the container  # noqa: E501

        :return: The container_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this GetCorporationsCorporationIdContainersLogs200Ok.

        ID of the container  # noqa: E501

        :param container_id: The container_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and container_id is None:
            raise ValueError("Invalid value for `container_id`, must not be `None`")  # noqa: E501

        self._container_id = container_id

    @property
    def container_type_id(self):
        """Gets the container_type_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        Type ID of the container  # noqa: E501

        :return: The container_type_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._container_type_id

    @container_type_id.setter
    def container_type_id(self, container_type_id):
        """Sets the container_type_id of this GetCorporationsCorporationIdContainersLogs200Ok.

        Type ID of the container  # noqa: E501

        :param container_type_id: The container_type_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and container_type_id is None:
            raise ValueError("Invalid value for `container_type_id`, must not be `None`")  # noqa: E501

        self._container_type_id = container_type_id

    @property
    def location_flag(self):
        """Gets the location_flag of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        location_flag string  # noqa: E501

        :return: The location_flag of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: str
        """
        return self._location_flag

    @location_flag.setter
    def location_flag(self, location_flag):
        """Sets the location_flag of this GetCorporationsCorporationIdContainersLogs200Ok.

        location_flag string  # noqa: E501

        :param location_flag: The location_flag of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and location_flag is None:
            raise ValueError("Invalid value for `location_flag`, must not be `None`")  # noqa: E501
        allowed_values = ["AssetSafety", "AutoFit", "Bonus", "Booster", "BoosterBay", "Capsule", "Cargo", "CorpDeliveries", "CorpSAG1", "CorpSAG2", "CorpSAG3", "CorpSAG4", "CorpSAG5", "CorpSAG6", "CorpSAG7", "CrateLoot", "Deliveries", "DroneBay", "DustBattle", "DustDatabank", "FighterBay", "FighterTube0", "FighterTube1", "FighterTube2", "FighterTube3", "FighterTube4", "FleetHangar", "FrigateEscapeBay", "Hangar", "HangarAll", "HiSlot0", "HiSlot1", "HiSlot2", "HiSlot3", "HiSlot4", "HiSlot5", "HiSlot6", "HiSlot7", "HiddenModifiers", "Implant", "Impounded", "JunkyardReprocessed", "JunkyardTrashed", "LoSlot0", "LoSlot1", "LoSlot2", "LoSlot3", "LoSlot4", "LoSlot5", "LoSlot6", "LoSlot7", "Locked", "MedSlot0", "MedSlot1", "MedSlot2", "MedSlot3", "MedSlot4", "MedSlot5", "MedSlot6", "MedSlot7", "OfficeFolder", "Pilot", "PlanetSurface", "QuafeBay", "QuantumCoreRoom", "Reward", "RigSlot0", "RigSlot1", "RigSlot2", "RigSlot3", "RigSlot4", "RigSlot5", "RigSlot6", "RigSlot7", "SecondaryStorage", "ServiceSlot0", "ServiceSlot1", "ServiceSlot2", "ServiceSlot3", "ServiceSlot4", "ServiceSlot5", "ServiceSlot6", "ServiceSlot7", "ShipHangar", "ShipOffline", "Skill", "SkillInTraining", "SpecializedAmmoHold", "SpecializedCommandCenterHold", "SpecializedFuelBay", "SpecializedGasHold", "SpecializedIndustrialShipHold", "SpecializedLargeShipHold", "SpecializedMaterialBay", "SpecializedMediumShipHold", "SpecializedMineralHold", "SpecializedOreHold", "SpecializedPlanetaryCommoditiesHold", "SpecializedSalvageHold", "SpecializedShipHold", "SpecializedSmallShipHold", "StructureActive", "StructureFuel", "StructureInactive", "StructureOffline", "SubSystemBay", "SubSystemSlot0", "SubSystemSlot1", "SubSystemSlot2", "SubSystemSlot3", "SubSystemSlot4", "SubSystemSlot5", "SubSystemSlot6", "SubSystemSlot7", "Unlocked", "Wallet", "Wardrobe"]  # noqa: E501
        if (self._configuration.client_side_validation and
                location_flag not in allowed_values):
            raise ValueError(
                "Invalid value for `location_flag` ({0}), must be one of {1}"  # noqa: E501
                .format(location_flag, allowed_values)
            )

        self._location_flag = location_flag

    @property
    def location_id(self):
        """Gets the location_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCorporationsCorporationIdContainersLogs200Ok.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def logged_at(self):
        """Gets the logged_at of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        Timestamp when this log was created  # noqa: E501

        :return: The logged_at of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._logged_at

    @logged_at.setter
    def logged_at(self, logged_at):
        """Sets the logged_at of this GetCorporationsCorporationIdContainersLogs200Ok.

        Timestamp when this log was created  # noqa: E501

        :param logged_at: The logged_at of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and logged_at is None:
            raise ValueError("Invalid value for `logged_at`, must not be `None`")  # noqa: E501

        self._logged_at = logged_at

    @property
    def new_config_bitmask(self):
        """Gets the new_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        new_config_bitmask integer  # noqa: E501

        :return: The new_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._new_config_bitmask

    @new_config_bitmask.setter
    def new_config_bitmask(self, new_config_bitmask):
        """Sets the new_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.

        new_config_bitmask integer  # noqa: E501

        :param new_config_bitmask: The new_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """

        self._new_config_bitmask = new_config_bitmask

    @property
    def old_config_bitmask(self):
        """Gets the old_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        old_config_bitmask integer  # noqa: E501

        :return: The old_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._old_config_bitmask

    @old_config_bitmask.setter
    def old_config_bitmask(self, old_config_bitmask):
        """Sets the old_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.

        old_config_bitmask integer  # noqa: E501

        :param old_config_bitmask: The old_config_bitmask of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """

        self._old_config_bitmask = old_config_bitmask

    @property
    def password_type(self):
        """Gets the password_type of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        Type of password set if action is of type SetPassword or EnterPassword  # noqa: E501

        :return: The password_type of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: str
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this GetCorporationsCorporationIdContainersLogs200Ok.

        Type of password set if action is of type SetPassword or EnterPassword  # noqa: E501

        :param password_type: The password_type of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["config", "general"]  # noqa: E501
        if (self._configuration.client_side_validation and
                password_type not in allowed_values):
            raise ValueError(
                "Invalid value for `password_type` ({0}), must be one of {1}"  # noqa: E501
                .format(password_type, allowed_values)
            )

        self._password_type = password_type

    @property
    def quantity(self):
        """Gets the quantity of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        Quantity of the item being acted upon  # noqa: E501

        :return: The quantity of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCorporationsCorporationIdContainersLogs200Ok.

        Quantity of the item being acted upon  # noqa: E501

        :param quantity: The quantity of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501

        Type ID of the item being acted upon  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdContainersLogs200Ok.

        Type ID of the item being acted upon  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdContainersLogs200Ok.  # noqa: E501
        :type: int
        """

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
        if issubclass(GetCorporationsCorporationIdContainersLogs200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdContainersLogs200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdContainersLogs200Ok):
            return True

        return self.to_dict() != other.to_dict()
