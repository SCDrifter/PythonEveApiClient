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


class GetUniverseGraphicsGraphicIdOk(object):
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
        'collision_file': 'str',
        'graphic_file': 'str',
        'graphic_id': 'int',
        'icon_folder': 'str',
        'sof_dna': 'str',
        'sof_fation_name': 'str',
        'sof_hull_name': 'str',
        'sof_race_name': 'str'
    }

    attribute_map = {
        'collision_file': 'collision_file',
        'graphic_file': 'graphic_file',
        'graphic_id': 'graphic_id',
        'icon_folder': 'icon_folder',
        'sof_dna': 'sof_dna',
        'sof_fation_name': 'sof_fation_name',
        'sof_hull_name': 'sof_hull_name',
        'sof_race_name': 'sof_race_name'
    }

    def __init__(self, collision_file=None, graphic_file=None, graphic_id=None, icon_folder=None, sof_dna=None, sof_fation_name=None, sof_hull_name=None, sof_race_name=None, _configuration=None):  # noqa: E501
        """GetUniverseGraphicsGraphicIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collision_file = None
        self._graphic_file = None
        self._graphic_id = None
        self._icon_folder = None
        self._sof_dna = None
        self._sof_fation_name = None
        self._sof_hull_name = None
        self._sof_race_name = None
        self.discriminator = None

        if collision_file is not None:
            self.collision_file = collision_file
        if graphic_file is not None:
            self.graphic_file = graphic_file
        self.graphic_id = graphic_id
        if icon_folder is not None:
            self.icon_folder = icon_folder
        if sof_dna is not None:
            self.sof_dna = sof_dna
        if sof_fation_name is not None:
            self.sof_fation_name = sof_fation_name
        if sof_hull_name is not None:
            self.sof_hull_name = sof_hull_name
        if sof_race_name is not None:
            self.sof_race_name = sof_race_name

    @property
    def collision_file(self):
        """Gets the collision_file of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        collision_file string  # noqa: E501

        :return: The collision_file of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._collision_file

    @collision_file.setter
    def collision_file(self, collision_file):
        """Sets the collision_file of this GetUniverseGraphicsGraphicIdOk.

        collision_file string  # noqa: E501

        :param collision_file: The collision_file of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._collision_file = collision_file

    @property
    def graphic_file(self):
        """Gets the graphic_file of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        graphic_file string  # noqa: E501

        :return: The graphic_file of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._graphic_file

    @graphic_file.setter
    def graphic_file(self, graphic_file):
        """Sets the graphic_file of this GetUniverseGraphicsGraphicIdOk.

        graphic_file string  # noqa: E501

        :param graphic_file: The graphic_file of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._graphic_file = graphic_file

    @property
    def graphic_id(self):
        """Gets the graphic_id of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        graphic_id integer  # noqa: E501

        :return: The graphic_id of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: int
        """
        return self._graphic_id

    @graphic_id.setter
    def graphic_id(self, graphic_id):
        """Sets the graphic_id of this GetUniverseGraphicsGraphicIdOk.

        graphic_id integer  # noqa: E501

        :param graphic_id: The graphic_id of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and graphic_id is None:
            raise ValueError("Invalid value for `graphic_id`, must not be `None`")  # noqa: E501

        self._graphic_id = graphic_id

    @property
    def icon_folder(self):
        """Gets the icon_folder of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        icon_folder string  # noqa: E501

        :return: The icon_folder of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._icon_folder

    @icon_folder.setter
    def icon_folder(self, icon_folder):
        """Sets the icon_folder of this GetUniverseGraphicsGraphicIdOk.

        icon_folder string  # noqa: E501

        :param icon_folder: The icon_folder of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._icon_folder = icon_folder

    @property
    def sof_dna(self):
        """Gets the sof_dna of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        sof_dna string  # noqa: E501

        :return: The sof_dna of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._sof_dna

    @sof_dna.setter
    def sof_dna(self, sof_dna):
        """Sets the sof_dna of this GetUniverseGraphicsGraphicIdOk.

        sof_dna string  # noqa: E501

        :param sof_dna: The sof_dna of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._sof_dna = sof_dna

    @property
    def sof_fation_name(self):
        """Gets the sof_fation_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        sof_fation_name string  # noqa: E501

        :return: The sof_fation_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._sof_fation_name

    @sof_fation_name.setter
    def sof_fation_name(self, sof_fation_name):
        """Sets the sof_fation_name of this GetUniverseGraphicsGraphicIdOk.

        sof_fation_name string  # noqa: E501

        :param sof_fation_name: The sof_fation_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._sof_fation_name = sof_fation_name

    @property
    def sof_hull_name(self):
        """Gets the sof_hull_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        sof_hull_name string  # noqa: E501

        :return: The sof_hull_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._sof_hull_name

    @sof_hull_name.setter
    def sof_hull_name(self, sof_hull_name):
        """Sets the sof_hull_name of this GetUniverseGraphicsGraphicIdOk.

        sof_hull_name string  # noqa: E501

        :param sof_hull_name: The sof_hull_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._sof_hull_name = sof_hull_name

    @property
    def sof_race_name(self):
        """Gets the sof_race_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501

        sof_race_name string  # noqa: E501

        :return: The sof_race_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :rtype: str
        """
        return self._sof_race_name

    @sof_race_name.setter
    def sof_race_name(self, sof_race_name):
        """Sets the sof_race_name of this GetUniverseGraphicsGraphicIdOk.

        sof_race_name string  # noqa: E501

        :param sof_race_name: The sof_race_name of this GetUniverseGraphicsGraphicIdOk.  # noqa: E501
        :type: str
        """

        self._sof_race_name = sof_race_name

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
        if issubclass(GetUniverseGraphicsGraphicIdOk, dict):
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
        if not isinstance(other, GetUniverseGraphicsGraphicIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseGraphicsGraphicIdOk):
            return True

        return self.to_dict() != other.to_dict()
