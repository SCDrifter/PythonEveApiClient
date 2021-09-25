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


class GetCorporationsCorporationIdRoles200Ok(object):
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
        'grantable_roles': 'list[str]',
        'grantable_roles_at_base': 'list[str]',
        'grantable_roles_at_hq': 'list[str]',
        'grantable_roles_at_other': 'list[str]',
        'roles': 'list[str]',
        'roles_at_base': 'list[str]',
        'roles_at_hq': 'list[str]',
        'roles_at_other': 'list[str]'
    }

    attribute_map = {
        'character_id': 'character_id',
        'grantable_roles': 'grantable_roles',
        'grantable_roles_at_base': 'grantable_roles_at_base',
        'grantable_roles_at_hq': 'grantable_roles_at_hq',
        'grantable_roles_at_other': 'grantable_roles_at_other',
        'roles': 'roles',
        'roles_at_base': 'roles_at_base',
        'roles_at_hq': 'roles_at_hq',
        'roles_at_other': 'roles_at_other'
    }

    def __init__(self, character_id=None, grantable_roles=None, grantable_roles_at_base=None, grantable_roles_at_hq=None, grantable_roles_at_other=None, roles=None, roles_at_base=None, roles_at_hq=None, roles_at_other=None):  # noqa: E501
        """GetCorporationsCorporationIdRoles200Ok - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._grantable_roles = None
        self._grantable_roles_at_base = None
        self._grantable_roles_at_hq = None
        self._grantable_roles_at_other = None
        self._roles = None
        self._roles_at_base = None
        self._roles_at_hq = None
        self._roles_at_other = None
        self.discriminator = None

        self.character_id = character_id
        if grantable_roles is not None:
            self.grantable_roles = grantable_roles
        if grantable_roles_at_base is not None:
            self.grantable_roles_at_base = grantable_roles_at_base
        if grantable_roles_at_hq is not None:
            self.grantable_roles_at_hq = grantable_roles_at_hq
        if grantable_roles_at_other is not None:
            self.grantable_roles_at_other = grantable_roles_at_other
        if roles is not None:
            self.roles = roles
        if roles_at_base is not None:
            self.roles_at_base = roles_at_base
        if roles_at_hq is not None:
            self.roles_at_hq = roles_at_hq
        if roles_at_other is not None:
            self.roles_at_other = roles_at_other

    @property
    def character_id(self):
        """Gets the character_id of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetCorporationsCorporationIdRoles200Ok.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def grantable_roles(self):
        """Gets the grantable_roles of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        grantable_roles array  # noqa: E501

        :return: The grantable_roles of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._grantable_roles

    @grantable_roles.setter
    def grantable_roles(self, grantable_roles):
        """Sets the grantable_roles of this GetCorporationsCorporationIdRoles200Ok.

        grantable_roles array  # noqa: E501

        :param grantable_roles: The grantable_roles of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(grantable_roles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `grantable_roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(grantable_roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._grantable_roles = grantable_roles

    @property
    def grantable_roles_at_base(self):
        """Gets the grantable_roles_at_base of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        grantable_roles_at_base array  # noqa: E501

        :return: The grantable_roles_at_base of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._grantable_roles_at_base

    @grantable_roles_at_base.setter
    def grantable_roles_at_base(self, grantable_roles_at_base):
        """Sets the grantable_roles_at_base of this GetCorporationsCorporationIdRoles200Ok.

        grantable_roles_at_base array  # noqa: E501

        :param grantable_roles_at_base: The grantable_roles_at_base of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(grantable_roles_at_base).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `grantable_roles_at_base` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(grantable_roles_at_base) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._grantable_roles_at_base = grantable_roles_at_base

    @property
    def grantable_roles_at_hq(self):
        """Gets the grantable_roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        grantable_roles_at_hq array  # noqa: E501

        :return: The grantable_roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._grantable_roles_at_hq

    @grantable_roles_at_hq.setter
    def grantable_roles_at_hq(self, grantable_roles_at_hq):
        """Sets the grantable_roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.

        grantable_roles_at_hq array  # noqa: E501

        :param grantable_roles_at_hq: The grantable_roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(grantable_roles_at_hq).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `grantable_roles_at_hq` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(grantable_roles_at_hq) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._grantable_roles_at_hq = grantable_roles_at_hq

    @property
    def grantable_roles_at_other(self):
        """Gets the grantable_roles_at_other of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        grantable_roles_at_other array  # noqa: E501

        :return: The grantable_roles_at_other of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._grantable_roles_at_other

    @grantable_roles_at_other.setter
    def grantable_roles_at_other(self, grantable_roles_at_other):
        """Sets the grantable_roles_at_other of this GetCorporationsCorporationIdRoles200Ok.

        grantable_roles_at_other array  # noqa: E501

        :param grantable_roles_at_other: The grantable_roles_at_other of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(grantable_roles_at_other).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `grantable_roles_at_other` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(grantable_roles_at_other) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._grantable_roles_at_other = grantable_roles_at_other

    @property
    def roles(self):
        """Gets the roles of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        roles array  # noqa: E501

        :return: The roles of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this GetCorporationsCorporationIdRoles200Ok.

        roles array  # noqa: E501

        :param roles: The roles of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(roles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

    @property
    def roles_at_base(self):
        """Gets the roles_at_base of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        roles_at_base array  # noqa: E501

        :return: The roles_at_base of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles_at_base

    @roles_at_base.setter
    def roles_at_base(self, roles_at_base):
        """Sets the roles_at_base of this GetCorporationsCorporationIdRoles200Ok.

        roles_at_base array  # noqa: E501

        :param roles_at_base: The roles_at_base of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(roles_at_base).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles_at_base` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles_at_base) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles_at_base = roles_at_base

    @property
    def roles_at_hq(self):
        """Gets the roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        roles_at_hq array  # noqa: E501

        :return: The roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles_at_hq

    @roles_at_hq.setter
    def roles_at_hq(self, roles_at_hq):
        """Sets the roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.

        roles_at_hq array  # noqa: E501

        :param roles_at_hq: The roles_at_hq of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(roles_at_hq).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles_at_hq` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles_at_hq) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles_at_hq = roles_at_hq

    @property
    def roles_at_other(self):
        """Gets the roles_at_other of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501

        roles_at_other array  # noqa: E501

        :return: The roles_at_other of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles_at_other

    @roles_at_other.setter
    def roles_at_other(self, roles_at_other):
        """Sets the roles_at_other of this GetCorporationsCorporationIdRoles200Ok.

        roles_at_other array  # noqa: E501

        :param roles_at_other: The roles_at_other of this GetCorporationsCorporationIdRoles200Ok.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Account_Take_1", "Account_Take_2", "Account_Take_3", "Account_Take_4", "Account_Take_5", "Account_Take_6", "Account_Take_7", "Accountant", "Auditor", "Communications_Officer", "Config_Equipment", "Config_Starbase_Equipment", "Container_Take_1", "Container_Take_2", "Container_Take_3", "Container_Take_4", "Container_Take_5", "Container_Take_6", "Container_Take_7", "Contract_Manager", "Diplomat", "Director", "Factory_Manager", "Fitting_Manager", "Hangar_Query_1", "Hangar_Query_2", "Hangar_Query_3", "Hangar_Query_4", "Hangar_Query_5", "Hangar_Query_6", "Hangar_Query_7", "Hangar_Take_1", "Hangar_Take_2", "Hangar_Take_3", "Hangar_Take_4", "Hangar_Take_5", "Hangar_Take_6", "Hangar_Take_7", "Junior_Accountant", "Personnel_Manager", "Rent_Factory_Facility", "Rent_Office", "Rent_Research_Facility", "Security_Officer", "Starbase_Defense_Operator", "Starbase_Fuel_Technician", "Station_Manager", "Trader"]  # noqa: E501
        if not set(roles_at_other).issubset(set(allowed_values)):
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
        if issubclass(GetCorporationsCorporationIdRoles200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdRoles200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
