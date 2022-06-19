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


class GetCorporationsCorporationIdBookmarksFolders200Ok(object):
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
        'creator_id': 'int',
        'folder_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'creator_id': 'creator_id',
        'folder_id': 'folder_id',
        'name': 'name'
    }

    def __init__(self, creator_id=None, folder_id=None, name=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdBookmarksFolders200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creator_id = None
        self._folder_id = None
        self._name = None
        self.discriminator = None

        if creator_id is not None:
            self.creator_id = creator_id
        self.folder_id = folder_id
        self.name = name

    @property
    def creator_id(self):
        """Gets the creator_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501

        creator_id integer  # noqa: E501

        :return: The creator_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.

        creator_id integer  # noqa: E501

        :param creator_id: The creator_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def folder_id(self):
        """Gets the folder_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501

        folder_id integer  # noqa: E501

        :return: The folder_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.

        folder_id integer  # noqa: E501

        :param folder_id: The folder_id of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and folder_id is None:
            raise ValueError("Invalid value for `folder_id`, must not be `None`")  # noqa: E501

        self._folder_id = folder_id

    @property
    def name(self):
        """Gets the name of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCorporationsCorporationIdBookmarksFolders200Ok.

        name string  # noqa: E501

        :param name: The name of this GetCorporationsCorporationIdBookmarksFolders200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(GetCorporationsCorporationIdBookmarksFolders200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdBookmarksFolders200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdBookmarksFolders200Ok):
            return True

        return self.to_dict() != other.to_dict()
