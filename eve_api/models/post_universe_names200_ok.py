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


class PostUniverseNames200Ok(object):
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
        'category': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'category': 'category',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, category=None, id=None, name=None):  # noqa: E501
        """PostUniverseNames200Ok - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.category = category
        self.id = id
        self.name = name

    @property
    def category(self):
        """Gets the category of this PostUniverseNames200Ok.  # noqa: E501

        category string  # noqa: E501

        :return: The category of this PostUniverseNames200Ok.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PostUniverseNames200Ok.

        category string  # noqa: E501

        :param category: The category of this PostUniverseNames200Ok.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance", "character", "constellation", "corporation", "inventory_type", "region", "solar_system", "station", "faction"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def id(self):
        """Gets the id of this PostUniverseNames200Ok.  # noqa: E501

        id integer  # noqa: E501

        :return: The id of this PostUniverseNames200Ok.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostUniverseNames200Ok.

        id integer  # noqa: E501

        :param id: The id of this PostUniverseNames200Ok.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this PostUniverseNames200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this PostUniverseNames200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostUniverseNames200Ok.

        name string  # noqa: E501

        :param name: The name of this PostUniverseNames200Ok.  # noqa: E501
        :type: str
        """
        if name is None:
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
        if issubclass(PostUniverseNames200Ok, dict):
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
        if not isinstance(other, PostUniverseNames200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
