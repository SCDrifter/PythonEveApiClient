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


class GetFleetsFleetIdMembers200Ok(object):
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
        'join_time': 'datetime',
        'role': 'str',
        'role_name': 'str',
        'ship_type_id': 'int',
        'solar_system_id': 'int',
        'squad_id': 'int',
        'station_id': 'int',
        'takes_fleet_warp': 'bool',
        'wing_id': 'int'
    }

    attribute_map = {
        'character_id': 'character_id',
        'join_time': 'join_time',
        'role': 'role',
        'role_name': 'role_name',
        'ship_type_id': 'ship_type_id',
        'solar_system_id': 'solar_system_id',
        'squad_id': 'squad_id',
        'station_id': 'station_id',
        'takes_fleet_warp': 'takes_fleet_warp',
        'wing_id': 'wing_id'
    }

    def __init__(self, character_id=None, join_time=None, role=None, role_name=None, ship_type_id=None, solar_system_id=None, squad_id=None, station_id=None, takes_fleet_warp=None, wing_id=None):  # noqa: E501
        """GetFleetsFleetIdMembers200Ok - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._join_time = None
        self._role = None
        self._role_name = None
        self._ship_type_id = None
        self._solar_system_id = None
        self._squad_id = None
        self._station_id = None
        self._takes_fleet_warp = None
        self._wing_id = None
        self.discriminator = None

        self.character_id = character_id
        self.join_time = join_time
        self.role = role
        self.role_name = role_name
        self.ship_type_id = ship_type_id
        self.solar_system_id = solar_system_id
        self.squad_id = squad_id
        if station_id is not None:
            self.station_id = station_id
        self.takes_fleet_warp = takes_fleet_warp
        self.wing_id = wing_id

    @property
    def character_id(self):
        """Gets the character_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetFleetsFleetIdMembers200Ok.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def join_time(self):
        """Gets the join_time of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        join_time string  # noqa: E501

        :return: The join_time of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        """Sets the join_time of this GetFleetsFleetIdMembers200Ok.

        join_time string  # noqa: E501

        :param join_time: The join_time of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: datetime
        """
        if join_time is None:
            raise ValueError("Invalid value for `join_time`, must not be `None`")  # noqa: E501

        self._join_time = join_time

    @property
    def role(self):
        """Gets the role of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        Member’s role in fleet  # noqa: E501

        :return: The role of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this GetFleetsFleetIdMembers200Ok.

        Member’s role in fleet  # noqa: E501

        :param role: The role of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["fleet_commander", "wing_commander", "squad_commander", "squad_member"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def role_name(self):
        """Gets the role_name of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        Localized role names  # noqa: E501

        :return: The role_name of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this GetFleetsFleetIdMembers200Ok.

        Localized role names  # noqa: E501

        :param role_name: The role_name of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: str
        """
        if role_name is None:
            raise ValueError("Invalid value for `role_name`, must not be `None`")  # noqa: E501

        self._role_name = role_name

    @property
    def ship_type_id(self):
        """Gets the ship_type_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        ship_type_id integer  # noqa: E501

        :return: The ship_type_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """Sets the ship_type_id of this GetFleetsFleetIdMembers200Ok.

        ship_type_id integer  # noqa: E501

        :param ship_type_id: The ship_type_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: int
        """
        if ship_type_id is None:
            raise ValueError("Invalid value for `ship_type_id`, must not be `None`")  # noqa: E501

        self._ship_type_id = ship_type_id

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        Solar system the member is located in  # noqa: E501

        :return: The solar_system_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetFleetsFleetIdMembers200Ok.

        Solar system the member is located in  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def squad_id(self):
        """Gets the squad_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        ID of the squad the member is in. If not applicable, will be set to -1  # noqa: E501

        :return: The squad_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._squad_id

    @squad_id.setter
    def squad_id(self, squad_id):
        """Sets the squad_id of this GetFleetsFleetIdMembers200Ok.

        ID of the squad the member is in. If not applicable, will be set to -1  # noqa: E501

        :param squad_id: The squad_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: int
        """
        if squad_id is None:
            raise ValueError("Invalid value for `squad_id`, must not be `None`")  # noqa: E501

        self._squad_id = squad_id

    @property
    def station_id(self):
        """Gets the station_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        Station in which the member is docked in, if applicable  # noqa: E501

        :return: The station_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id):
        """Sets the station_id of this GetFleetsFleetIdMembers200Ok.

        Station in which the member is docked in, if applicable  # noqa: E501

        :param station_id: The station_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: int
        """

        self._station_id = station_id

    @property
    def takes_fleet_warp(self):
        """Gets the takes_fleet_warp of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        Whether the member take fleet warps  # noqa: E501

        :return: The takes_fleet_warp of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._takes_fleet_warp

    @takes_fleet_warp.setter
    def takes_fleet_warp(self, takes_fleet_warp):
        """Sets the takes_fleet_warp of this GetFleetsFleetIdMembers200Ok.

        Whether the member take fleet warps  # noqa: E501

        :param takes_fleet_warp: The takes_fleet_warp of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: bool
        """
        if takes_fleet_warp is None:
            raise ValueError("Invalid value for `takes_fleet_warp`, must not be `None`")  # noqa: E501

        self._takes_fleet_warp = takes_fleet_warp

    @property
    def wing_id(self):
        """Gets the wing_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501

        ID of the wing the member is in. If not applicable, will be set to -1  # noqa: E501

        :return: The wing_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._wing_id

    @wing_id.setter
    def wing_id(self, wing_id):
        """Sets the wing_id of this GetFleetsFleetIdMembers200Ok.

        ID of the wing the member is in. If not applicable, will be set to -1  # noqa: E501

        :param wing_id: The wing_id of this GetFleetsFleetIdMembers200Ok.  # noqa: E501
        :type: int
        """
        if wing_id is None:
            raise ValueError("Invalid value for `wing_id`, must not be `None`")  # noqa: E501

        self._wing_id = wing_id

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
        if issubclass(GetFleetsFleetIdMembers200Ok, dict):
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
        if not isinstance(other, GetFleetsFleetIdMembers200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
