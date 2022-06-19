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


class GetUniverseBloodlines200Ok(object):
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
        'bloodline_id': 'int',
        'charisma': 'int',
        'corporation_id': 'int',
        'description': 'str',
        'intelligence': 'int',
        'memory': 'int',
        'name': 'str',
        'perception': 'int',
        'race_id': 'int',
        'ship_type_id': 'int',
        'willpower': 'int'
    }

    attribute_map = {
        'bloodline_id': 'bloodline_id',
        'charisma': 'charisma',
        'corporation_id': 'corporation_id',
        'description': 'description',
        'intelligence': 'intelligence',
        'memory': 'memory',
        'name': 'name',
        'perception': 'perception',
        'race_id': 'race_id',
        'ship_type_id': 'ship_type_id',
        'willpower': 'willpower'
    }

    def __init__(self, bloodline_id=None, charisma=None, corporation_id=None, description=None, intelligence=None, memory=None, name=None, perception=None, race_id=None, ship_type_id=None, willpower=None, _configuration=None):  # noqa: E501
        """GetUniverseBloodlines200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bloodline_id = None
        self._charisma = None
        self._corporation_id = None
        self._description = None
        self._intelligence = None
        self._memory = None
        self._name = None
        self._perception = None
        self._race_id = None
        self._ship_type_id = None
        self._willpower = None
        self.discriminator = None

        self.bloodline_id = bloodline_id
        self.charisma = charisma
        self.corporation_id = corporation_id
        self.description = description
        self.intelligence = intelligence
        self.memory = memory
        self.name = name
        self.perception = perception
        self.race_id = race_id
        self.ship_type_id = ship_type_id
        self.willpower = willpower

    @property
    def bloodline_id(self):
        """Gets the bloodline_id of this GetUniverseBloodlines200Ok.  # noqa: E501

        bloodline_id integer  # noqa: E501

        :return: The bloodline_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._bloodline_id

    @bloodline_id.setter
    def bloodline_id(self, bloodline_id):
        """Sets the bloodline_id of this GetUniverseBloodlines200Ok.

        bloodline_id integer  # noqa: E501

        :param bloodline_id: The bloodline_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and bloodline_id is None:
            raise ValueError("Invalid value for `bloodline_id`, must not be `None`")  # noqa: E501

        self._bloodline_id = bloodline_id

    @property
    def charisma(self):
        """Gets the charisma of this GetUniverseBloodlines200Ok.  # noqa: E501

        charisma integer  # noqa: E501

        :return: The charisma of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._charisma

    @charisma.setter
    def charisma(self, charisma):
        """Sets the charisma of this GetUniverseBloodlines200Ok.

        charisma integer  # noqa: E501

        :param charisma: The charisma of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and charisma is None:
            raise ValueError("Invalid value for `charisma`, must not be `None`")  # noqa: E501

        self._charisma = charisma

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetUniverseBloodlines200Ok.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetUniverseBloodlines200Ok.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")  # noqa: E501

        self._corporation_id = corporation_id

    @property
    def description(self):
        """Gets the description of this GetUniverseBloodlines200Ok.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetUniverseBloodlines200Ok.

        description string  # noqa: E501

        :param description: The description of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def intelligence(self):
        """Gets the intelligence of this GetUniverseBloodlines200Ok.  # noqa: E501

        intelligence integer  # noqa: E501

        :return: The intelligence of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        """Sets the intelligence of this GetUniverseBloodlines200Ok.

        intelligence integer  # noqa: E501

        :param intelligence: The intelligence of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and intelligence is None:
            raise ValueError("Invalid value for `intelligence`, must not be `None`")  # noqa: E501

        self._intelligence = intelligence

    @property
    def memory(self):
        """Gets the memory of this GetUniverseBloodlines200Ok.  # noqa: E501

        memory integer  # noqa: E501

        :return: The memory of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this GetUniverseBloodlines200Ok.

        memory integer  # noqa: E501

        :param memory: The memory of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def name(self):
        """Gets the name of this GetUniverseBloodlines200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseBloodlines200Ok.

        name string  # noqa: E501

        :param name: The name of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def perception(self):
        """Gets the perception of this GetUniverseBloodlines200Ok.  # noqa: E501

        perception integer  # noqa: E501

        :return: The perception of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._perception

    @perception.setter
    def perception(self, perception):
        """Sets the perception of this GetUniverseBloodlines200Ok.

        perception integer  # noqa: E501

        :param perception: The perception of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and perception is None:
            raise ValueError("Invalid value for `perception`, must not be `None`")  # noqa: E501

        self._perception = perception

    @property
    def race_id(self):
        """Gets the race_id of this GetUniverseBloodlines200Ok.  # noqa: E501

        race_id integer  # noqa: E501

        :return: The race_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        """Sets the race_id of this GetUniverseBloodlines200Ok.

        race_id integer  # noqa: E501

        :param race_id: The race_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and race_id is None:
            raise ValueError("Invalid value for `race_id`, must not be `None`")  # noqa: E501

        self._race_id = race_id

    @property
    def ship_type_id(self):
        """Gets the ship_type_id of this GetUniverseBloodlines200Ok.  # noqa: E501

        ship_type_id integer  # noqa: E501

        :return: The ship_type_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """Sets the ship_type_id of this GetUniverseBloodlines200Ok.

        ship_type_id integer  # noqa: E501

        :param ship_type_id: The ship_type_id of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ship_type_id is None:
            raise ValueError("Invalid value for `ship_type_id`, must not be `None`")  # noqa: E501

        self._ship_type_id = ship_type_id

    @property
    def willpower(self):
        """Gets the willpower of this GetUniverseBloodlines200Ok.  # noqa: E501

        willpower integer  # noqa: E501

        :return: The willpower of this GetUniverseBloodlines200Ok.  # noqa: E501
        :rtype: int
        """
        return self._willpower

    @willpower.setter
    def willpower(self, willpower):
        """Sets the willpower of this GetUniverseBloodlines200Ok.

        willpower integer  # noqa: E501

        :param willpower: The willpower of this GetUniverseBloodlines200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and willpower is None:
            raise ValueError("Invalid value for `willpower`, must not be `None`")  # noqa: E501

        self._willpower = willpower

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
        if issubclass(GetUniverseBloodlines200Ok, dict):
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
        if not isinstance(other, GetUniverseBloodlines200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseBloodlines200Ok):
            return True

        return self.to_dict() != other.to_dict()
