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


class GetCharactersCharacterIdMedals200Ok(object):
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
        'corporation_id': 'int',
        '_date': 'datetime',
        'description': 'str',
        'graphics': 'list[GetCharactersCharacterIdMedalsGraphic]',
        'issuer_id': 'int',
        'medal_id': 'int',
        'reason': 'str',
        'status': 'str',
        'title': 'str'
    }

    attribute_map = {
        'corporation_id': 'corporation_id',
        '_date': 'date',
        'description': 'description',
        'graphics': 'graphics',
        'issuer_id': 'issuer_id',
        'medal_id': 'medal_id',
        'reason': 'reason',
        'status': 'status',
        'title': 'title'
    }

    def __init__(self, corporation_id=None, _date=None, description=None, graphics=None, issuer_id=None, medal_id=None, reason=None, status=None, title=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdMedals200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._corporation_id = None
        self.__date = None
        self._description = None
        self._graphics = None
        self._issuer_id = None
        self._medal_id = None
        self._reason = None
        self._status = None
        self._title = None
        self.discriminator = None

        self.corporation_id = corporation_id
        self._date = _date
        self.description = description
        self.graphics = graphics
        self.issuer_id = issuer_id
        self.medal_id = medal_id
        self.reason = reason
        self.status = status
        self.title = title

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetCharactersCharacterIdMedals200Ok.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")  # noqa: E501

        self._corporation_id = corporation_id

    @property
    def _date(self):
        """Gets the _date of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        date string  # noqa: E501

        :return: The _date of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetCharactersCharacterIdMedals200Ok.

        date string  # noqa: E501

        :param _date: The _date of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetCharactersCharacterIdMedals200Ok.

        description string  # noqa: E501

        :param description: The description of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def graphics(self):
        """Gets the graphics of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        graphics array  # noqa: E501

        :return: The graphics of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdMedalsGraphic]
        """
        return self._graphics

    @graphics.setter
    def graphics(self, graphics):
        """Sets the graphics of this GetCharactersCharacterIdMedals200Ok.

        graphics array  # noqa: E501

        :param graphics: The graphics of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: list[GetCharactersCharacterIdMedalsGraphic]
        """
        if self._configuration.client_side_validation and graphics is None:
            raise ValueError("Invalid value for `graphics`, must not be `None`")  # noqa: E501

        self._graphics = graphics

    @property
    def issuer_id(self):
        """Gets the issuer_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        issuer_id integer  # noqa: E501

        :return: The issuer_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: int
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this GetCharactersCharacterIdMedals200Ok.

        issuer_id integer  # noqa: E501

        :param issuer_id: The issuer_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and issuer_id is None:
            raise ValueError("Invalid value for `issuer_id`, must not be `None`")  # noqa: E501

        self._issuer_id = issuer_id

    @property
    def medal_id(self):
        """Gets the medal_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        medal_id integer  # noqa: E501

        :return: The medal_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: int
        """
        return self._medal_id

    @medal_id.setter
    def medal_id(self, medal_id):
        """Sets the medal_id of this GetCharactersCharacterIdMedals200Ok.

        medal_id integer  # noqa: E501

        :param medal_id: The medal_id of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and medal_id is None:
            raise ValueError("Invalid value for `medal_id`, must not be `None`")  # noqa: E501

        self._medal_id = medal_id

    @property
    def reason(self):
        """Gets the reason of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        reason string  # noqa: E501

        :return: The reason of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this GetCharactersCharacterIdMedals200Ok.

        reason string  # noqa: E501

        :param reason: The reason of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        status string  # noqa: E501

        :return: The status of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetCharactersCharacterIdMedals200Ok.

        status string  # noqa: E501

        :param status: The status of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["public", "private"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501

        title string  # noqa: E501

        :return: The title of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetCharactersCharacterIdMedals200Ok.

        title string  # noqa: E501

        :param title: The title of this GetCharactersCharacterIdMedals200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

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
        if issubclass(GetCharactersCharacterIdMedals200Ok, dict):
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
        if not isinstance(other, GetCharactersCharacterIdMedals200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdMedals200Ok):
            return True

        return self.to_dict() != other.to_dict()
