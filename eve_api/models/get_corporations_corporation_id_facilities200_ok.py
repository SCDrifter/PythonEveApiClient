# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCorporationsCorporationIdFacilities200Ok(object):
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
        'facility_id': 'int',
        'system_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'facility_id': 'facility_id',
        'system_id': 'system_id',
        'type_id': 'type_id'
    }

    def __init__(self, facility_id=None, system_id=None, type_id=None):  # noqa: E501
        """GetCorporationsCorporationIdFacilities200Ok - a model defined in Swagger"""  # noqa: E501

        self._facility_id = None
        self._system_id = None
        self._type_id = None
        self.discriminator = None

        self.facility_id = facility_id
        self.system_id = system_id
        self.type_id = type_id

    @property
    def facility_id(self):
        """Gets the facility_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501

        facility_id integer  # noqa: E501

        :return: The facility_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501
        :rtype: int
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this GetCorporationsCorporationIdFacilities200Ok.

        facility_id integer  # noqa: E501

        :param facility_id: The facility_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501
        :type: int
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")  # noqa: E501

        self._facility_id = facility_id

    @property
    def system_id(self):
        """Gets the system_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501

        system_id integer  # noqa: E501

        :return: The system_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetCorporationsCorporationIdFacilities200Ok.

        system_id integer  # noqa: E501

        :param system_id: The system_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdFacilities200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdFacilities200Ok.  # noqa: E501
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
        if issubclass(GetCorporationsCorporationIdFacilities200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdFacilities200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
