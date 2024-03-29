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


class GetCorporationsCorporationIdStructures200Ok(object):
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
        'corporation_id': 'int',
        'fuel_expires': 'datetime',
        'name': 'str',
        'next_reinforce_apply': 'datetime',
        'next_reinforce_hour': 'int',
        'profile_id': 'int',
        'reinforce_hour': 'int',
        'services': 'list[GetCorporationsCorporationIdStructuresService]',
        'state': 'str',
        'state_timer_end': 'datetime',
        'state_timer_start': 'datetime',
        'structure_id': 'int',
        'system_id': 'int',
        'type_id': 'int',
        'unanchors_at': 'datetime'
    }

    attribute_map = {
        'corporation_id': 'corporation_id',
        'fuel_expires': 'fuel_expires',
        'name': 'name',
        'next_reinforce_apply': 'next_reinforce_apply',
        'next_reinforce_hour': 'next_reinforce_hour',
        'profile_id': 'profile_id',
        'reinforce_hour': 'reinforce_hour',
        'services': 'services',
        'state': 'state',
        'state_timer_end': 'state_timer_end',
        'state_timer_start': 'state_timer_start',
        'structure_id': 'structure_id',
        'system_id': 'system_id',
        'type_id': 'type_id',
        'unanchors_at': 'unanchors_at'
    }

    def __init__(self, corporation_id=None, fuel_expires=None, name=None, next_reinforce_apply=None, next_reinforce_hour=None, profile_id=None, reinforce_hour=None, services=None, state=None, state_timer_end=None, state_timer_start=None, structure_id=None, system_id=None, type_id=None, unanchors_at=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdStructures200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._corporation_id = None
        self._fuel_expires = None
        self._name = None
        self._next_reinforce_apply = None
        self._next_reinforce_hour = None
        self._profile_id = None
        self._reinforce_hour = None
        self._services = None
        self._state = None
        self._state_timer_end = None
        self._state_timer_start = None
        self._structure_id = None
        self._system_id = None
        self._type_id = None
        self._unanchors_at = None
        self.discriminator = None

        self.corporation_id = corporation_id
        if fuel_expires is not None:
            self.fuel_expires = fuel_expires
        if name is not None:
            self.name = name
        if next_reinforce_apply is not None:
            self.next_reinforce_apply = next_reinforce_apply
        if next_reinforce_hour is not None:
            self.next_reinforce_hour = next_reinforce_hour
        self.profile_id = profile_id
        if reinforce_hour is not None:
            self.reinforce_hour = reinforce_hour
        if services is not None:
            self.services = services
        self.state = state
        if state_timer_end is not None:
            self.state_timer_end = state_timer_end
        if state_timer_start is not None:
            self.state_timer_start = state_timer_start
        self.structure_id = structure_id
        self.system_id = system_id
        self.type_id = type_id
        if unanchors_at is not None:
            self.unanchors_at = unanchors_at

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        ID of the corporation that owns the structure  # noqa: E501

        :return: The corporation_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetCorporationsCorporationIdStructures200Ok.

        ID of the corporation that owns the structure  # noqa: E501

        :param corporation_id: The corporation_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")  # noqa: E501

        self._corporation_id = corporation_id

    @property
    def fuel_expires(self):
        """Gets the fuel_expires of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        Date on which the structure will run out of fuel  # noqa: E501

        :return: The fuel_expires of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._fuel_expires

    @fuel_expires.setter
    def fuel_expires(self, fuel_expires):
        """Sets the fuel_expires of this GetCorporationsCorporationIdStructures200Ok.

        Date on which the structure will run out of fuel  # noqa: E501

        :param fuel_expires: The fuel_expires of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._fuel_expires = fuel_expires

    @property
    def name(self):
        """Gets the name of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The structure name  # noqa: E501

        :return: The name of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCorporationsCorporationIdStructures200Ok.

        The structure name  # noqa: E501

        :param name: The name of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next_reinforce_apply(self):
        """Gets the next_reinforce_apply of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The date and time when the structure's newly requested reinforcement times (e.g. next_reinforce_hour and next_reinforce_day) will take effect  # noqa: E501

        :return: The next_reinforce_apply of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._next_reinforce_apply

    @next_reinforce_apply.setter
    def next_reinforce_apply(self, next_reinforce_apply):
        """Sets the next_reinforce_apply of this GetCorporationsCorporationIdStructures200Ok.

        The date and time when the structure's newly requested reinforcement times (e.g. next_reinforce_hour and next_reinforce_day) will take effect  # noqa: E501

        :param next_reinforce_apply: The next_reinforce_apply of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._next_reinforce_apply = next_reinforce_apply

    @property
    def next_reinforce_hour(self):
        """Gets the next_reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The requested change to reinforce_hour that will take effect at the time shown by next_reinforce_apply  # noqa: E501

        :return: The next_reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._next_reinforce_hour

    @next_reinforce_hour.setter
    def next_reinforce_hour(self, next_reinforce_hour):
        """Sets the next_reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.

        The requested change to reinforce_hour that will take effect at the time shown by next_reinforce_apply  # noqa: E501

        :param next_reinforce_hour: The next_reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                next_reinforce_hour is not None and next_reinforce_hour > 23):  # noqa: E501
            raise ValueError("Invalid value for `next_reinforce_hour`, must be a value less than or equal to `23`")  # noqa: E501
        if (self._configuration.client_side_validation and
                next_reinforce_hour is not None and next_reinforce_hour < 0):  # noqa: E501
            raise ValueError("Invalid value for `next_reinforce_hour`, must be a value greater than or equal to `0`")  # noqa: E501

        self._next_reinforce_hour = next_reinforce_hour

    @property
    def profile_id(self):
        """Gets the profile_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The id of the ACL profile for this citadel  # noqa: E501

        :return: The profile_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this GetCorporationsCorporationIdStructures200Ok.

        The id of the ACL profile for this citadel  # noqa: E501

        :param profile_id: The profile_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def reinforce_hour(self):
        """Gets the reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The hour of day that determines the four hour window when the structure will randomly exit its reinforcement periods and become vulnerable to attack against its armor and/or hull. The structure will become vulnerable at a random time that is +/- 2 hours centered on the value of this property  # noqa: E501

        :return: The reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._reinforce_hour

    @reinforce_hour.setter
    def reinforce_hour(self, reinforce_hour):
        """Sets the reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.

        The hour of day that determines the four hour window when the structure will randomly exit its reinforcement periods and become vulnerable to attack against its armor and/or hull. The structure will become vulnerable at a random time that is +/- 2 hours centered on the value of this property  # noqa: E501

        :param reinforce_hour: The reinforce_hour of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                reinforce_hour is not None and reinforce_hour > 23):  # noqa: E501
            raise ValueError("Invalid value for `reinforce_hour`, must be a value less than or equal to `23`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reinforce_hour is not None and reinforce_hour < 0):  # noqa: E501
            raise ValueError("Invalid value for `reinforce_hour`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reinforce_hour = reinforce_hour

    @property
    def services(self):
        """Gets the services of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        Contains a list of service upgrades, and their state  # noqa: E501

        :return: The services of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: list[GetCorporationsCorporationIdStructuresService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this GetCorporationsCorporationIdStructures200Ok.

        Contains a list of service upgrades, and their state  # noqa: E501

        :param services: The services of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: list[GetCorporationsCorporationIdStructuresService]
        """

        self._services = services

    @property
    def state(self):
        """Gets the state of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        state string  # noqa: E501

        :return: The state of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetCorporationsCorporationIdStructures200Ok.

        state string  # noqa: E501

        :param state: The state of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["anchor_vulnerable", "anchoring", "armor_reinforce", "armor_vulnerable", "deploy_vulnerable", "fitting_invulnerable", "hull_reinforce", "hull_vulnerable", "online_deprecated", "onlining_vulnerable", "shield_vulnerable", "unanchored", "unknown"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_timer_end(self):
        """Gets the state_timer_end of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        Date at which the structure will move to it's next state  # noqa: E501

        :return: The state_timer_end of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._state_timer_end

    @state_timer_end.setter
    def state_timer_end(self, state_timer_end):
        """Sets the state_timer_end of this GetCorporationsCorporationIdStructures200Ok.

        Date at which the structure will move to it's next state  # noqa: E501

        :param state_timer_end: The state_timer_end of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._state_timer_end = state_timer_end

    @property
    def state_timer_start(self):
        """Gets the state_timer_start of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        Date at which the structure entered it's current state  # noqa: E501

        :return: The state_timer_start of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._state_timer_start

    @state_timer_start.setter
    def state_timer_start(self, state_timer_start):
        """Sets the state_timer_start of this GetCorporationsCorporationIdStructures200Ok.

        Date at which the structure entered it's current state  # noqa: E501

        :param state_timer_start: The state_timer_start of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._state_timer_start = state_timer_start

    @property
    def structure_id(self):
        """Gets the structure_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The Item ID of the structure  # noqa: E501

        :return: The structure_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """Sets the structure_id of this GetCorporationsCorporationIdStructures200Ok.

        The Item ID of the structure  # noqa: E501

        :param structure_id: The structure_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and structure_id is None:
            raise ValueError("Invalid value for `structure_id`, must not be `None`")  # noqa: E501

        self._structure_id = structure_id

    @property
    def system_id(self):
        """Gets the system_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The solar system the structure is in  # noqa: E501

        :return: The system_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetCorporationsCorporationIdStructures200Ok.

        The solar system the structure is in  # noqa: E501

        :param system_id: The system_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        The type id of the structure  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdStructures200Ok.

        The type id of the structure  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def unanchors_at(self):
        """Gets the unanchors_at of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501

        Date at which the structure will unanchor  # noqa: E501

        :return: The unanchors_at of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._unanchors_at

    @unanchors_at.setter
    def unanchors_at(self, unanchors_at):
        """Sets the unanchors_at of this GetCorporationsCorporationIdStructures200Ok.

        Date at which the structure will unanchor  # noqa: E501

        :param unanchors_at: The unanchors_at of this GetCorporationsCorporationIdStructures200Ok.  # noqa: E501
        :type: datetime
        """

        self._unanchors_at = unanchors_at

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
        if issubclass(GetCorporationsCorporationIdStructures200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdStructures200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdStructures200Ok):
            return True

        return self.to_dict() != other.to_dict()
