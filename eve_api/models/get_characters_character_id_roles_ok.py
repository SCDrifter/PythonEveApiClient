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


class GetCharactersCharacterIdRolesOk(object):
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
        'roles': 'list[str]',
        'roles_at_base': 'list[str]',
        'roles_at_hq': 'list[str]',
        'roles_at_other': 'list[str]'
    }

    attribute_map = {
        'roles': 'roles',
        'roles_at_base': 'roles_at_base',
        'roles_at_hq': 'roles_at_hq',
        'roles_at_other': 'roles_at_other'
    }

    def __init__(self, roles=None, roles_at_base=None, roles_at_hq=None, roles_at_other=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdRolesOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._roles = None
        self._roles_at_base = None
        self._roles_at_hq = None
        self._roles_at_other = None
        self.discriminator = None

        if roles is not None:
            self.roles = roles
        if roles_at_base is not None:
            self.roles_at_base = roles_at_base
        if roles_at_hq is not None:
            self.roles_at_hq = roles_at_hq
        if roles_at_other is not None:
            self.roles_at_other = roles_at_other

    @property
    def roles(self):
        """Gets the roles of this GetCharactersCharacterIdRolesOk.  # noqa: E501

        roles array  # noqa: E501

        :return: The roles of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this GetCharactersCharacterIdRolesOk.

        roles array  # noqa: E501

        :param roles: The roles of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(roles).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

    @property
    def roles_at_base(self):
        """Gets the roles_at_base of this GetCharactersCharacterIdRolesOk.  # noqa: E501

        roles_at_base array  # noqa: E501

        :return: The roles_at_base of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles_at_base

    @roles_at_base.setter
    def roles_at_base(self, roles_at_base):
        """Sets the roles_at_base of this GetCharactersCharacterIdRolesOk.

        roles_at_base array  # noqa: E501

        :param roles_at_base: The roles_at_base of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(roles_at_base).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles_at_base` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles_at_base) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles_at_base = roles_at_base

    @property
    def roles_at_hq(self):
        """Gets the roles_at_hq of this GetCharactersCharacterIdRolesOk.  # noqa: E501

        roles_at_hq array  # noqa: E501

        :return: The roles_at_hq of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles_at_hq

    @roles_at_hq.setter
    def roles_at_hq(self, roles_at_hq):
        """Sets the roles_at_hq of this GetCharactersCharacterIdRolesOk.

        roles_at_hq array  # noqa: E501

        :param roles_at_hq: The roles_at_hq of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(roles_at_hq).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles_at_hq` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles_at_hq) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles_at_hq = roles_at_hq

    @property
    def roles_at_other(self):
        """Gets the roles_at_other of this GetCharactersCharacterIdRolesOk.  # noqa: E501

        roles_at_other array  # noqa: E501

        :return: The roles_at_other of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles_at_other

    @roles_at_other.setter
    def roles_at_other(self, roles_at_other):
        """Sets the roles_at_other of this GetCharactersCharacterIdRolesOk.

        roles_at_other array  # noqa: E501

        :param roles_at_other: The roles_at_other of this GetCharactersCharacterIdRolesOk.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(roles_at_other).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles_at_other` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles_at_other) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles_at_other = roles_at_other

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
        if issubclass(GetCharactersCharacterIdRolesOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdRolesOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdRolesOk):
            return True

        return self.to_dict() != other.to_dict()
