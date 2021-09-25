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


class GetCharactersCharacterIdPlanetsPlanetIdRoute(object):
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
        'content_type_id': 'int',
        'destination_pin_id': 'int',
        'quantity': 'float',
        'route_id': 'int',
        'source_pin_id': 'int',
        'waypoints': 'list[int]'
    }

    attribute_map = {
        'content_type_id': 'content_type_id',
        'destination_pin_id': 'destination_pin_id',
        'quantity': 'quantity',
        'route_id': 'route_id',
        'source_pin_id': 'source_pin_id',
        'waypoints': 'waypoints'
    }

    def __init__(self, content_type_id=None, destination_pin_id=None, quantity=None, route_id=None, source_pin_id=None, waypoints=None):  # noqa: E501
        """GetCharactersCharacterIdPlanetsPlanetIdRoute - a model defined in Swagger"""  # noqa: E501

        self._content_type_id = None
        self._destination_pin_id = None
        self._quantity = None
        self._route_id = None
        self._source_pin_id = None
        self._waypoints = None
        self.discriminator = None

        self.content_type_id = content_type_id
        self.destination_pin_id = destination_pin_id
        self.quantity = quantity
        self.route_id = route_id
        self.source_pin_id = source_pin_id
        if waypoints is not None:
            self.waypoints = waypoints

    @property
    def content_type_id(self):
        """Gets the content_type_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501

        content_type_id integer  # noqa: E501

        :return: The content_type_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :rtype: int
        """
        return self._content_type_id

    @content_type_id.setter
    def content_type_id(self, content_type_id):
        """Sets the content_type_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.

        content_type_id integer  # noqa: E501

        :param content_type_id: The content_type_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :type: int
        """
        if content_type_id is None:
            raise ValueError("Invalid value for `content_type_id`, must not be `None`")  # noqa: E501

        self._content_type_id = content_type_id

    @property
    def destination_pin_id(self):
        """Gets the destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501

        destination_pin_id integer  # noqa: E501

        :return: The destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :rtype: int
        """
        return self._destination_pin_id

    @destination_pin_id.setter
    def destination_pin_id(self, destination_pin_id):
        """Sets the destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.

        destination_pin_id integer  # noqa: E501

        :param destination_pin_id: The destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :type: int
        """
        if destination_pin_id is None:
            raise ValueError("Invalid value for `destination_pin_id`, must not be `None`")  # noqa: E501

        self._destination_pin_id = destination_pin_id

    @property
    def quantity(self):
        """Gets the quantity of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501

        quantity number  # noqa: E501

        :return: The quantity of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCharactersCharacterIdPlanetsPlanetIdRoute.

        quantity number  # noqa: E501

        :param quantity: The quantity of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def route_id(self):
        """Gets the route_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501

        route_id integer  # noqa: E501

        :return: The route_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :rtype: int
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.

        route_id integer  # noqa: E501

        :param route_id: The route_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :type: int
        """
        if route_id is None:
            raise ValueError("Invalid value for `route_id`, must not be `None`")  # noqa: E501

        self._route_id = route_id

    @property
    def source_pin_id(self):
        """Gets the source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501

        source_pin_id integer  # noqa: E501

        :return: The source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :rtype: int
        """
        return self._source_pin_id

    @source_pin_id.setter
    def source_pin_id(self, source_pin_id):
        """Sets the source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.

        source_pin_id integer  # noqa: E501

        :param source_pin_id: The source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :type: int
        """
        if source_pin_id is None:
            raise ValueError("Invalid value for `source_pin_id`, must not be `None`")  # noqa: E501

        self._source_pin_id = source_pin_id

    @property
    def waypoints(self):
        """Gets the waypoints of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501

        list of pin ID waypoints  # noqa: E501

        :return: The waypoints of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :rtype: list[int]
        """
        return self._waypoints

    @waypoints.setter
    def waypoints(self, waypoints):
        """Sets the waypoints of this GetCharactersCharacterIdPlanetsPlanetIdRoute.

        list of pin ID waypoints  # noqa: E501

        :param waypoints: The waypoints of this GetCharactersCharacterIdPlanetsPlanetIdRoute.  # noqa: E501
        :type: list[int]
        """

        self._waypoints = waypoints

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
        if issubclass(GetCharactersCharacterIdPlanetsPlanetIdRoute, dict):
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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
