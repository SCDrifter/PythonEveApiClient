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


class GetCharactersCharacterIdOk(object):
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
        'alliance_id': 'int',
        'birthday': 'datetime',
        'bloodline_id': 'int',
        'corporation_id': 'int',
        'description': 'str',
        'faction_id': 'int',
        'gender': 'str',
        'name': 'str',
        'race_id': 'int',
        'security_status': 'float',
        'title': 'str'
    }

    attribute_map = {
        'alliance_id': 'alliance_id',
        'birthday': 'birthday',
        'bloodline_id': 'bloodline_id',
        'corporation_id': 'corporation_id',
        'description': 'description',
        'faction_id': 'faction_id',
        'gender': 'gender',
        'name': 'name',
        'race_id': 'race_id',
        'security_status': 'security_status',
        'title': 'title'
    }

    def __init__(self, alliance_id=None, birthday=None, bloodline_id=None, corporation_id=None, description=None, faction_id=None, gender=None, name=None, race_id=None, security_status=None, title=None):  # noqa: E501
        """GetCharactersCharacterIdOk - a model defined in Swagger"""  # noqa: E501

        self._alliance_id = None
        self._birthday = None
        self._bloodline_id = None
        self._corporation_id = None
        self._description = None
        self._faction_id = None
        self._gender = None
        self._name = None
        self._race_id = None
        self._security_status = None
        self._title = None
        self.discriminator = None

        if alliance_id is not None:
            self.alliance_id = alliance_id
        self.birthday = birthday
        self.bloodline_id = bloodline_id
        self.corporation_id = corporation_id
        if description is not None:
            self.description = description
        if faction_id is not None:
            self.faction_id = faction_id
        self.gender = gender
        self.name = name
        self.race_id = race_id
        if security_status is not None:
            self.security_status = security_status
        if title is not None:
            self.title = title

    @property
    def alliance_id(self):
        """Gets the alliance_id of this GetCharactersCharacterIdOk.  # noqa: E501

        The character's alliance ID  # noqa: E501

        :return: The alliance_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """Sets the alliance_id of this GetCharactersCharacterIdOk.

        The character's alliance ID  # noqa: E501

        :param alliance_id: The alliance_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def birthday(self):
        """Gets the birthday of this GetCharactersCharacterIdOk.  # noqa: E501

        Creation date of the character  # noqa: E501

        :return: The birthday of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this GetCharactersCharacterIdOk.

        Creation date of the character  # noqa: E501

        :param birthday: The birthday of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: datetime
        """
        if birthday is None:
            raise ValueError("Invalid value for `birthday`, must not be `None`")  # noqa: E501

        self._birthday = birthday

    @property
    def bloodline_id(self):
        """Gets the bloodline_id of this GetCharactersCharacterIdOk.  # noqa: E501

        bloodline_id integer  # noqa: E501

        :return: The bloodline_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: int
        """
        return self._bloodline_id

    @bloodline_id.setter
    def bloodline_id(self, bloodline_id):
        """Sets the bloodline_id of this GetCharactersCharacterIdOk.

        bloodline_id integer  # noqa: E501

        :param bloodline_id: The bloodline_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: int
        """
        if bloodline_id is None:
            raise ValueError("Invalid value for `bloodline_id`, must not be `None`")  # noqa: E501

        self._bloodline_id = bloodline_id

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetCharactersCharacterIdOk.  # noqa: E501

        The character's corporation ID  # noqa: E501

        :return: The corporation_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetCharactersCharacterIdOk.

        The character's corporation ID  # noqa: E501

        :param corporation_id: The corporation_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")  # noqa: E501

        self._corporation_id = corporation_id

    @property
    def description(self):
        """Gets the description of this GetCharactersCharacterIdOk.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetCharactersCharacterIdOk.

        description string  # noqa: E501

        :param description: The description of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def faction_id(self):
        """Gets the faction_id of this GetCharactersCharacterIdOk.  # noqa: E501

        ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare  # noqa: E501

        :return: The faction_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetCharactersCharacterIdOk.

        ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare  # noqa: E501

        :param faction_id: The faction_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: int
        """

        self._faction_id = faction_id

    @property
    def gender(self):
        """Gets the gender of this GetCharactersCharacterIdOk.  # noqa: E501

        gender string  # noqa: E501

        :return: The gender of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this GetCharactersCharacterIdOk.

        gender string  # noqa: E501

        :param gender: The gender of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: str
        """
        if gender is None:
            raise ValueError("Invalid value for `gender`, must not be `None`")  # noqa: E501
        allowed_values = ["female", "male"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def name(self):
        """Gets the name of this GetCharactersCharacterIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCharactersCharacterIdOk.

        name string  # noqa: E501

        :param name: The name of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def race_id(self):
        """Gets the race_id of this GetCharactersCharacterIdOk.  # noqa: E501

        race_id integer  # noqa: E501

        :return: The race_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: int
        """
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        """Sets the race_id of this GetCharactersCharacterIdOk.

        race_id integer  # noqa: E501

        :param race_id: The race_id of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: int
        """
        if race_id is None:
            raise ValueError("Invalid value for `race_id`, must not be `None`")  # noqa: E501

        self._race_id = race_id

    @property
    def security_status(self):
        """Gets the security_status of this GetCharactersCharacterIdOk.  # noqa: E501

        security_status number  # noqa: E501

        :return: The security_status of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: float
        """
        return self._security_status

    @security_status.setter
    def security_status(self, security_status):
        """Sets the security_status of this GetCharactersCharacterIdOk.

        security_status number  # noqa: E501

        :param security_status: The security_status of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: float
        """
        if security_status is not None and security_status > 10:  # noqa: E501
            raise ValueError("Invalid value for `security_status`, must be a value less than or equal to `10`")  # noqa: E501
        if security_status is not None and security_status < -10:  # noqa: E501
            raise ValueError("Invalid value for `security_status`, must be a value greater than or equal to `-10`")  # noqa: E501

        self._security_status = security_status

    @property
    def title(self):
        """Gets the title of this GetCharactersCharacterIdOk.  # noqa: E501

        The individual title of the character  # noqa: E501

        :return: The title of this GetCharactersCharacterIdOk.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetCharactersCharacterIdOk.

        The individual title of the character  # noqa: E501

        :param title: The title of this GetCharactersCharacterIdOk.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(GetCharactersCharacterIdOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
