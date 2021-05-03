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


class GetCorporationsCorporationIdBookmarks200Ok(object):
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
        'bookmark_id': 'int',
        'coordinates': 'GetCorporationsCorporationIdBookmarksCoordinates',
        'created': 'datetime',
        'creator_id': 'int',
        'folder_id': 'int',
        'item': 'GetCorporationsCorporationIdBookmarksItem',
        'label': 'str',
        'location_id': 'int',
        'notes': 'str'
    }

    attribute_map = {
        'bookmark_id': 'bookmark_id',
        'coordinates': 'coordinates',
        'created': 'created',
        'creator_id': 'creator_id',
        'folder_id': 'folder_id',
        'item': 'item',
        'label': 'label',
        'location_id': 'location_id',
        'notes': 'notes'
    }

    def __init__(self, bookmark_id=None, coordinates=None, created=None, creator_id=None, folder_id=None, item=None, label=None, location_id=None, notes=None):  # noqa: E501
        """GetCorporationsCorporationIdBookmarks200Ok - a model defined in Swagger"""  # noqa: E501

        self._bookmark_id = None
        self._coordinates = None
        self._created = None
        self._creator_id = None
        self._folder_id = None
        self._item = None
        self._label = None
        self._location_id = None
        self._notes = None
        self.discriminator = None

        self.bookmark_id = bookmark_id
        if coordinates is not None:
            self.coordinates = coordinates
        self.created = created
        self.creator_id = creator_id
        if folder_id is not None:
            self.folder_id = folder_id
        if item is not None:
            self.item = item
        self.label = label
        self.location_id = location_id
        self.notes = notes

    @property
    def bookmark_id(self):
        """Gets the bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        bookmark_id integer  # noqa: E501

        :return: The bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: int
        """
        return self._bookmark_id

    @bookmark_id.setter
    def bookmark_id(self, bookmark_id):
        """Sets the bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.

        bookmark_id integer  # noqa: E501

        :param bookmark_id: The bookmark_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: int
        """
        if bookmark_id is None:
            raise ValueError("Invalid value for `bookmark_id`, must not be `None`")  # noqa: E501

        self._bookmark_id = bookmark_id

    @property
    def coordinates(self):
        """Gets the coordinates of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501


        :return: The coordinates of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: GetCorporationsCorporationIdBookmarksCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this GetCorporationsCorporationIdBookmarks200Ok.


        :param coordinates: The coordinates of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: GetCorporationsCorporationIdBookmarksCoordinates
        """

        self._coordinates = coordinates

    @property
    def created(self):
        """Gets the created of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        created string  # noqa: E501

        :return: The created of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetCorporationsCorporationIdBookmarks200Ok.

        created string  # noqa: E501

        :param created: The created of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def creator_id(self):
        """Gets the creator_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        creator_id integer  # noqa: E501

        :return: The creator_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this GetCorporationsCorporationIdBookmarks200Ok.

        creator_id integer  # noqa: E501

        :param creator_id: The creator_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: int
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def folder_id(self):
        """Gets the folder_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        folder_id integer  # noqa: E501

        :return: The folder_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this GetCorporationsCorporationIdBookmarks200Ok.

        folder_id integer  # noqa: E501

        :param folder_id: The folder_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def item(self):
        """Gets the item of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501


        :return: The item of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: GetCorporationsCorporationIdBookmarksItem
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this GetCorporationsCorporationIdBookmarks200Ok.


        :param item: The item of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: GetCorporationsCorporationIdBookmarksItem
        """

        self._item = item

    @property
    def label(self):
        """Gets the label of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        label string  # noqa: E501

        :return: The label of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GetCorporationsCorporationIdBookmarks200Ok.

        label string  # noqa: E501

        :param label: The label of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def location_id(self):
        """Gets the location_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCorporationsCorporationIdBookmarks200Ok.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def notes(self):
        """Gets the notes of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501

        notes string  # noqa: E501

        :return: The notes of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GetCorporationsCorporationIdBookmarks200Ok.

        notes string  # noqa: E501

        :param notes: The notes of this GetCorporationsCorporationIdBookmarks200Ok.  # noqa: E501
        :type: str
        """
        if notes is None:
            raise ValueError("Invalid value for `notes`, must not be `None`")  # noqa: E501

        self._notes = notes

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
        if issubclass(GetCorporationsCorporationIdBookmarks200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdBookmarks200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
