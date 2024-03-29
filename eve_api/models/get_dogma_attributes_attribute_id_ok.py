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


class GetDogmaAttributesAttributeIdOk(object):
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
        'attribute_id': 'int',
        'default_value': 'float',
        'description': 'str',
        'display_name': 'str',
        'high_is_good': 'bool',
        'icon_id': 'int',
        'name': 'str',
        'published': 'bool',
        'stackable': 'bool',
        'unit_id': 'int'
    }

    attribute_map = {
        'attribute_id': 'attribute_id',
        'default_value': 'default_value',
        'description': 'description',
        'display_name': 'display_name',
        'high_is_good': 'high_is_good',
        'icon_id': 'icon_id',
        'name': 'name',
        'published': 'published',
        'stackable': 'stackable',
        'unit_id': 'unit_id'
    }

    def __init__(self, attribute_id=None, default_value=None, description=None, display_name=None, high_is_good=None, icon_id=None, name=None, published=None, stackable=None, unit_id=None, _configuration=None):  # noqa: E501
        """GetDogmaAttributesAttributeIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_id = None
        self._default_value = None
        self._description = None
        self._display_name = None
        self._high_is_good = None
        self._icon_id = None
        self._name = None
        self._published = None
        self._stackable = None
        self._unit_id = None
        self.discriminator = None

        self.attribute_id = attribute_id
        if default_value is not None:
            self.default_value = default_value
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if high_is_good is not None:
            self.high_is_good = high_is_good
        if icon_id is not None:
            self.icon_id = icon_id
        if name is not None:
            self.name = name
        if published is not None:
            self.published = published
        if stackable is not None:
            self.stackable = stackable
        if unit_id is not None:
            self.unit_id = unit_id

    @property
    def attribute_id(self):
        """Gets the attribute_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        attribute_id integer  # noqa: E501

        :return: The attribute_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this GetDogmaAttributesAttributeIdOk.

        attribute_id integer  # noqa: E501

        :param attribute_id: The attribute_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and attribute_id is None:
            raise ValueError("Invalid value for `attribute_id`, must not be `None`")  # noqa: E501

        self._attribute_id = attribute_id

    @property
    def default_value(self):
        """Gets the default_value of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        default_value number  # noqa: E501

        :return: The default_value of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: float
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this GetDogmaAttributesAttributeIdOk.

        default_value number  # noqa: E501

        :param default_value: The default_value of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: float
        """

        self._default_value = default_value

    @property
    def description(self):
        """Gets the description of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetDogmaAttributesAttributeIdOk.

        description string  # noqa: E501

        :param description: The description of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        display_name string  # noqa: E501

        :return: The display_name of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetDogmaAttributesAttributeIdOk.

        display_name string  # noqa: E501

        :param display_name: The display_name of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def high_is_good(self):
        """Gets the high_is_good of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        high_is_good boolean  # noqa: E501

        :return: The high_is_good of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._high_is_good

    @high_is_good.setter
    def high_is_good(self, high_is_good):
        """Sets the high_is_good of this GetDogmaAttributesAttributeIdOk.

        high_is_good boolean  # noqa: E501

        :param high_is_good: The high_is_good of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: bool
        """

        self._high_is_good = high_is_good

    @property
    def icon_id(self):
        """Gets the icon_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        icon_id integer  # noqa: E501

        :return: The icon_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: int
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """Sets the icon_id of this GetDogmaAttributesAttributeIdOk.

        icon_id integer  # noqa: E501

        :param icon_id: The icon_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: int
        """

        self._icon_id = icon_id

    @property
    def name(self):
        """Gets the name of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDogmaAttributesAttributeIdOk.

        name string  # noqa: E501

        :param name: The name of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def published(self):
        """Gets the published of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        published boolean  # noqa: E501

        :return: The published of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this GetDogmaAttributesAttributeIdOk.

        published boolean  # noqa: E501

        :param published: The published of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: bool
        """

        self._published = published

    @property
    def stackable(self):
        """Gets the stackable of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        stackable boolean  # noqa: E501

        :return: The stackable of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._stackable

    @stackable.setter
    def stackable(self, stackable):
        """Sets the stackable of this GetDogmaAttributesAttributeIdOk.

        stackable boolean  # noqa: E501

        :param stackable: The stackable of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: bool
        """

        self._stackable = stackable

    @property
    def unit_id(self):
        """Gets the unit_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501

        unit_id integer  # noqa: E501

        :return: The unit_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this GetDogmaAttributesAttributeIdOk.

        unit_id integer  # noqa: E501

        :param unit_id: The unit_id of this GetDogmaAttributesAttributeIdOk.  # noqa: E501
        :type: int
        """

        self._unit_id = unit_id

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
        if issubclass(GetDogmaAttributesAttributeIdOk, dict):
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
        if not isinstance(other, GetDogmaAttributesAttributeIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDogmaAttributesAttributeIdOk):
            return True

        return self.to_dict() != other.to_dict()
