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


class GetUniverseSystemKills200Ok(object):
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
        'npc_kills': 'int',
        'pod_kills': 'int',
        'ship_kills': 'int',
        'system_id': 'int'
    }

    attribute_map = {
        'npc_kills': 'npc_kills',
        'pod_kills': 'pod_kills',
        'ship_kills': 'ship_kills',
        'system_id': 'system_id'
    }

    def __init__(self, npc_kills=None, pod_kills=None, ship_kills=None, system_id=None):  # noqa: E501
        """GetUniverseSystemKills200Ok - a model defined in Swagger"""  # noqa: E501

        self._npc_kills = None
        self._pod_kills = None
        self._ship_kills = None
        self._system_id = None
        self.discriminator = None

        self.npc_kills = npc_kills
        self.pod_kills = pod_kills
        self.ship_kills = ship_kills
        self.system_id = system_id

    @property
    def npc_kills(self):
        """Gets the npc_kills of this GetUniverseSystemKills200Ok.  # noqa: E501

        Number of NPC ships killed in this system  # noqa: E501

        :return: The npc_kills of this GetUniverseSystemKills200Ok.  # noqa: E501
        :rtype: int
        """
        return self._npc_kills

    @npc_kills.setter
    def npc_kills(self, npc_kills):
        """Sets the npc_kills of this GetUniverseSystemKills200Ok.

        Number of NPC ships killed in this system  # noqa: E501

        :param npc_kills: The npc_kills of this GetUniverseSystemKills200Ok.  # noqa: E501
        :type: int
        """
        if npc_kills is None:
            raise ValueError("Invalid value for `npc_kills`, must not be `None`")  # noqa: E501

        self._npc_kills = npc_kills

    @property
    def pod_kills(self):
        """Gets the pod_kills of this GetUniverseSystemKills200Ok.  # noqa: E501

        Number of pods killed in this system  # noqa: E501

        :return: The pod_kills of this GetUniverseSystemKills200Ok.  # noqa: E501
        :rtype: int
        """
        return self._pod_kills

    @pod_kills.setter
    def pod_kills(self, pod_kills):
        """Sets the pod_kills of this GetUniverseSystemKills200Ok.

        Number of pods killed in this system  # noqa: E501

        :param pod_kills: The pod_kills of this GetUniverseSystemKills200Ok.  # noqa: E501
        :type: int
        """
        if pod_kills is None:
            raise ValueError("Invalid value for `pod_kills`, must not be `None`")  # noqa: E501

        self._pod_kills = pod_kills

    @property
    def ship_kills(self):
        """Gets the ship_kills of this GetUniverseSystemKills200Ok.  # noqa: E501

        Number of player ships killed in this system  # noqa: E501

        :return: The ship_kills of this GetUniverseSystemKills200Ok.  # noqa: E501
        :rtype: int
        """
        return self._ship_kills

    @ship_kills.setter
    def ship_kills(self, ship_kills):
        """Sets the ship_kills of this GetUniverseSystemKills200Ok.

        Number of player ships killed in this system  # noqa: E501

        :param ship_kills: The ship_kills of this GetUniverseSystemKills200Ok.  # noqa: E501
        :type: int
        """
        if ship_kills is None:
            raise ValueError("Invalid value for `ship_kills`, must not be `None`")  # noqa: E501

        self._ship_kills = ship_kills

    @property
    def system_id(self):
        """Gets the system_id of this GetUniverseSystemKills200Ok.  # noqa: E501

        system_id integer  # noqa: E501

        :return: The system_id of this GetUniverseSystemKills200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetUniverseSystemKills200Ok.

        system_id integer  # noqa: E501

        :param system_id: The system_id of this GetUniverseSystemKills200Ok.  # noqa: E501
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

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
        if issubclass(GetUniverseSystemKills200Ok, dict):
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
        if not isinstance(other, GetUniverseSystemKills200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
