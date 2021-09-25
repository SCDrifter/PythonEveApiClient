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


class GetCharactersCharacterIdSkillsOk(object):
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
        'skills': 'list[GetCharactersCharacterIdSkillsSkill]',
        'total_sp': 'int',
        'unallocated_sp': 'int'
    }

    attribute_map = {
        'skills': 'skills',
        'total_sp': 'total_sp',
        'unallocated_sp': 'unallocated_sp'
    }

    def __init__(self, skills=None, total_sp=None, unallocated_sp=None):  # noqa: E501
        """GetCharactersCharacterIdSkillsOk - a model defined in Swagger"""  # noqa: E501

        self._skills = None
        self._total_sp = None
        self._unallocated_sp = None
        self.discriminator = None

        self.skills = skills
        self.total_sp = total_sp
        if unallocated_sp is not None:
            self.unallocated_sp = unallocated_sp

    @property
    def skills(self):
        """Gets the skills of this GetCharactersCharacterIdSkillsOk.  # noqa: E501

        skills array  # noqa: E501

        :return: The skills of this GetCharactersCharacterIdSkillsOk.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdSkillsSkill]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this GetCharactersCharacterIdSkillsOk.

        skills array  # noqa: E501

        :param skills: The skills of this GetCharactersCharacterIdSkillsOk.  # noqa: E501
        :type: list[GetCharactersCharacterIdSkillsSkill]
        """
        if skills is None:
            raise ValueError("Invalid value for `skills`, must not be `None`")  # noqa: E501

        self._skills = skills

    @property
    def total_sp(self):
        """Gets the total_sp of this GetCharactersCharacterIdSkillsOk.  # noqa: E501

        total_sp integer  # noqa: E501

        :return: The total_sp of this GetCharactersCharacterIdSkillsOk.  # noqa: E501
        :rtype: int
        """
        return self._total_sp

    @total_sp.setter
    def total_sp(self, total_sp):
        """Sets the total_sp of this GetCharactersCharacterIdSkillsOk.

        total_sp integer  # noqa: E501

        :param total_sp: The total_sp of this GetCharactersCharacterIdSkillsOk.  # noqa: E501
        :type: int
        """
        if total_sp is None:
            raise ValueError("Invalid value for `total_sp`, must not be `None`")  # noqa: E501

        self._total_sp = total_sp

    @property
    def unallocated_sp(self):
        """Gets the unallocated_sp of this GetCharactersCharacterIdSkillsOk.  # noqa: E501

        Skill points available to be assigned  # noqa: E501

        :return: The unallocated_sp of this GetCharactersCharacterIdSkillsOk.  # noqa: E501
        :rtype: int
        """
        return self._unallocated_sp

    @unallocated_sp.setter
    def unallocated_sp(self, unallocated_sp):
        """Sets the unallocated_sp of this GetCharactersCharacterIdSkillsOk.

        Skill points available to be assigned  # noqa: E501

        :param unallocated_sp: The unallocated_sp of this GetCharactersCharacterIdSkillsOk.  # noqa: E501
        :type: int
        """

        self._unallocated_sp = unallocated_sp

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
        if issubclass(GetCharactersCharacterIdSkillsOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdSkillsOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
