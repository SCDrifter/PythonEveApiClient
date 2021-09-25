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


class GetSovereigntyStructures200Ok(object):
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
        'solar_system_id': 'int',
        'structure_id': 'int',
        'structure_type_id': 'int',
        'vulnerability_occupancy_level': 'float',
        'vulnerable_end_time': 'datetime',
        'vulnerable_start_time': 'datetime'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'solar_system_id': 'solar_system_id',
        'structure_id': 'structure_id',
        'structure_type_id': 'structure_type_id',
        'vulnerability_occupancy_level': 'vulnerability_occupancy_level',
        'vulnerable_end_time': 'vulnerable_end_time',
        'vulnerable_start_time': 'vulnerable_start_time'
    }

    def __init__(self, alliance_id=None, solar_system_id=None, structure_id=None, structure_type_id=None, vulnerability_occupancy_level=None, vulnerable_end_time=None, vulnerable_start_time=None):  # noqa: E501
        """GetSovereigntyStructures200Ok - a model defined in Swagger"""  # noqa: E501

        self._alliance_id = None
        self._solar_system_id = None
        self._structure_id = None
        self._structure_type_id = None
        self._vulnerability_occupancy_level = None
        self._vulnerable_end_time = None
        self._vulnerable_start_time = None
        self.discriminator = None

        self.alliance_id = alliance_id
        self.solar_system_id = solar_system_id
        self.structure_id = structure_id
        self.structure_type_id = structure_type_id
        if vulnerability_occupancy_level is not None:
            self.vulnerability_occupancy_level = vulnerability_occupancy_level
        if vulnerable_end_time is not None:
            self.vulnerable_end_time = vulnerable_end_time
        if vulnerable_start_time is not None:
            self.vulnerable_start_time = vulnerable_start_time

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetSovereigntyStructures200Ok.  # noqa: E501

        The alliance that owns the structure.   # noqa: E501

        :return: The alliance_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetSovereigntyStructures200Ok.

        The alliance that owns the structure.   # noqa: E501

        :param alliance_id: The alliance_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: int
        """
        if alliance_id is None:
            raise ValueError("Invalid value for `alliance_id`, must not be `None`")  # noqa: E501

        self._alliance_id = alliance_id

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetSovereigntyStructures200Ok.  # noqa: E501

        Solar system in which the structure is located.   # noqa: E501

        :return: The solar_system_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetSovereigntyStructures200Ok.

        Solar system in which the structure is located.   # noqa: E501

        :param solar_system_id: The solar_system_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def structure_id(self):
        """Gets the structure_id of this GetSovereigntyStructures200Ok.  # noqa: E501

        Unique item ID for this structure.  # noqa: E501

        :return: The structure_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """Sets the structure_id of this GetSovereigntyStructures200Ok.

        Unique item ID for this structure.  # noqa: E501

        :param structure_id: The structure_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: int
        """
        if structure_id is None:
            raise ValueError("Invalid value for `structure_id`, must not be `None`")  # noqa: E501

        self._structure_id = structure_id

    @property
    def structure_type_id(self):
        """Gets the structure_type_id of this GetSovereigntyStructures200Ok.  # noqa: E501

        A reference to the type of structure this is.   # noqa: E501

        :return: The structure_type_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._structure_type_id

    @structure_type_id.setter
    def structure_type_id(self, structure_type_id):
        """Sets the structure_type_id of this GetSovereigntyStructures200Ok.

        A reference to the type of structure this is.   # noqa: E501

        :param structure_type_id: The structure_type_id of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: int
        """
        if structure_type_id is None:
            raise ValueError("Invalid value for `structure_type_id`, must not be `None`")  # noqa: E501

        self._structure_type_id = structure_type_id

    @property
    def vulnerability_occupancy_level(self):
        """Gets the vulnerability_occupancy_level of this GetSovereigntyStructures200Ok.  # noqa: E501

        The occupancy level for the next or current vulnerability window. This takes into account all development indexes and capital system bonuses. Also known as Activity Defense Multiplier from in the client. It increases the time that attackers must spend using their entosis links on the structure.   # noqa: E501

        :return: The vulnerability_occupancy_level of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: float
        """
        return self._vulnerability_occupancy_level

    @vulnerability_occupancy_level.setter
    def vulnerability_occupancy_level(self, vulnerability_occupancy_level):
        """Sets the vulnerability_occupancy_level of this GetSovereigntyStructures200Ok.

        The occupancy level for the next or current vulnerability window. This takes into account all development indexes and capital system bonuses. Also known as Activity Defense Multiplier from in the client. It increases the time that attackers must spend using their entosis links on the structure.   # noqa: E501

        :param vulnerability_occupancy_level: The vulnerability_occupancy_level of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: float
        """

        self._vulnerability_occupancy_level = vulnerability_occupancy_level

    @property
    def vulnerable_end_time(self):
        """Gets the vulnerable_end_time of this GetSovereigntyStructures200Ok.  # noqa: E501

        The time at which the next or current vulnerability window ends. At the end of a vulnerability window the next window is recalculated and locked in along with the vulnerabilityOccupancyLevel. If the structure is not in 100% entosis control of the defender, it will go in to 'overtime' and stay vulnerable for as long as that situation persists. Only once the defenders have 100% entosis control and has the vulnerableEndTime passed does the vulnerability interval expire and a new one is calculated.   # noqa: E501

        :return: The vulnerable_end_time of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._vulnerable_end_time

    @vulnerable_end_time.setter
    def vulnerable_end_time(self, vulnerable_end_time):
        """Sets the vulnerable_end_time of this GetSovereigntyStructures200Ok.

        The time at which the next or current vulnerability window ends. At the end of a vulnerability window the next window is recalculated and locked in along with the vulnerabilityOccupancyLevel. If the structure is not in 100% entosis control of the defender, it will go in to 'overtime' and stay vulnerable for as long as that situation persists. Only once the defenders have 100% entosis control and has the vulnerableEndTime passed does the vulnerability interval expire and a new one is calculated.   # noqa: E501

        :param vulnerable_end_time: The vulnerable_end_time of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._vulnerable_end_time = vulnerable_end_time

    @property
    def vulnerable_start_time(self):
        """Gets the vulnerable_start_time of this GetSovereigntyStructures200Ok.  # noqa: E501

        The next time at which the structure will become vulnerable. Or the start time of the current window if current time is between this and vulnerableEndTime.   # noqa: E501

        :return: The vulnerable_start_time of this GetSovereigntyStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._vulnerable_start_time

    @vulnerable_start_time.setter
    def vulnerable_start_time(self, vulnerable_start_time):
        """Sets the vulnerable_start_time of this GetSovereigntyStructures200Ok.

        The next time at which the structure will become vulnerable. Or the start time of the current window if current time is between this and vulnerableEndTime.   # noqa: E501

        :param vulnerable_start_time: The vulnerable_start_time of this GetSovereigntyStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._vulnerable_start_time = vulnerable_start_time

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
        if issubclass(GetSovereigntyStructures200Ok, dict):
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
        if not isinstance(other, GetSovereigntyStructures200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
