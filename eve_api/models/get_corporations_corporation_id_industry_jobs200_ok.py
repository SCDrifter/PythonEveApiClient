# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.3.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCorporationsCorporationIdIndustryJobs200Ok(object):
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
        'activity_id': 'int',
        'blueprint_id': 'int',
        'blueprint_location_id': 'int',
        'blueprint_type_id': 'int',
        'completed_character_id': 'int',
        'completed_date': 'datetime',
        'cost': 'float',
        'duration': 'int',
        'end_date': 'datetime',
        'facility_id': 'int',
        'installer_id': 'int',
        'job_id': 'int',
        'licensed_runs': 'int',
        'location_id': 'int',
        'output_location_id': 'int',
        'pause_date': 'datetime',
        'probability': 'float',
        'product_type_id': 'int',
        'runs': 'int',
        'start_date': 'datetime',
        'status': 'str',
        'successful_runs': 'int'
    }

    attribute_map = {
        'activity_id': 'activity_id',
        'blueprint_id': 'blueprint_id',
        'blueprint_location_id': 'blueprint_location_id',
        'blueprint_type_id': 'blueprint_type_id',
        'completed_character_id': 'completed_character_id',
        'completed_date': 'completed_date',
        'cost': 'cost',
        'duration': 'duration',
        'end_date': 'end_date',
        'facility_id': 'facility_id',
        'installer_id': 'installer_id',
        'job_id': 'job_id',
        'licensed_runs': 'licensed_runs',
        'location_id': 'location_id',
        'output_location_id': 'output_location_id',
        'pause_date': 'pause_date',
        'probability': 'probability',
        'product_type_id': 'product_type_id',
        'runs': 'runs',
        'start_date': 'start_date',
        'status': 'status',
        'successful_runs': 'successful_runs'
    }

    def __init__(self, activity_id=None, blueprint_id=None, blueprint_location_id=None, blueprint_type_id=None, completed_character_id=None, completed_date=None, cost=None, duration=None, end_date=None, facility_id=None, installer_id=None, job_id=None, licensed_runs=None, location_id=None, output_location_id=None, pause_date=None, probability=None, product_type_id=None, runs=None, start_date=None, status=None, successful_runs=None):  # noqa: E501
        """GetCorporationsCorporationIdIndustryJobs200Ok - a model defined in Swagger"""  # noqa: E501

        self._activity_id = None
        self._blueprint_id = None
        self._blueprint_location_id = None
        self._blueprint_type_id = None
        self._completed_character_id = None
        self._completed_date = None
        self._cost = None
        self._duration = None
        self._end_date = None
        self._facility_id = None
        self._installer_id = None
        self._job_id = None
        self._licensed_runs = None
        self._location_id = None
        self._output_location_id = None
        self._pause_date = None
        self._probability = None
        self._product_type_id = None
        self._runs = None
        self._start_date = None
        self._status = None
        self._successful_runs = None
        self.discriminator = None

        self.activity_id = activity_id
        self.blueprint_id = blueprint_id
        self.blueprint_location_id = blueprint_location_id
        self.blueprint_type_id = blueprint_type_id
        if completed_character_id is not None:
            self.completed_character_id = completed_character_id
        if completed_date is not None:
            self.completed_date = completed_date
        if cost is not None:
            self.cost = cost
        self.duration = duration
        self.end_date = end_date
        self.facility_id = facility_id
        self.installer_id = installer_id
        self.job_id = job_id
        if licensed_runs is not None:
            self.licensed_runs = licensed_runs
        self.location_id = location_id
        self.output_location_id = output_location_id
        if pause_date is not None:
            self.pause_date = pause_date
        if probability is not None:
            self.probability = probability
        if product_type_id is not None:
            self.product_type_id = product_type_id
        self.runs = runs
        self.start_date = start_date
        self.status = status
        if successful_runs is not None:
            self.successful_runs = successful_runs

    @property
    def activity_id(self):
        """Gets the activity_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Job activity ID  # noqa: E501

        :return: The activity_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Job activity ID  # noqa: E501

        :param activity_id: The activity_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")  # noqa: E501

        self._activity_id = activity_id

    @property
    def blueprint_id(self):
        """Gets the blueprint_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        blueprint_id integer  # noqa: E501

        :return: The blueprint_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._blueprint_id

    @blueprint_id.setter
    def blueprint_id(self, blueprint_id):
        """Sets the blueprint_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        blueprint_id integer  # noqa: E501

        :param blueprint_id: The blueprint_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if blueprint_id is None:
            raise ValueError("Invalid value for `blueprint_id`, must not be `None`")  # noqa: E501

        self._blueprint_id = blueprint_id

    @property
    def blueprint_location_id(self):
        """Gets the blueprint_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility  # noqa: E501

        :return: The blueprint_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._blueprint_location_id

    @blueprint_location_id.setter
    def blueprint_location_id(self, blueprint_location_id):
        """Sets the blueprint_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Location ID of the location from which the blueprint was installed. Normally a station ID, but can also be an asset (e.g. container) or corporation facility  # noqa: E501

        :param blueprint_location_id: The blueprint_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if blueprint_location_id is None:
            raise ValueError("Invalid value for `blueprint_location_id`, must not be `None`")  # noqa: E501

        self._blueprint_location_id = blueprint_location_id

    @property
    def blueprint_type_id(self):
        """Gets the blueprint_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        blueprint_type_id integer  # noqa: E501

        :return: The blueprint_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._blueprint_type_id

    @blueprint_type_id.setter
    def blueprint_type_id(self, blueprint_type_id):
        """Sets the blueprint_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        blueprint_type_id integer  # noqa: E501

        :param blueprint_type_id: The blueprint_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if blueprint_type_id is None:
            raise ValueError("Invalid value for `blueprint_type_id`, must not be `None`")  # noqa: E501

        self._blueprint_type_id = blueprint_type_id

    @property
    def completed_character_id(self):
        """Gets the completed_character_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        ID of the character which completed this job  # noqa: E501

        :return: The completed_character_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._completed_character_id

    @completed_character_id.setter
    def completed_character_id(self, completed_character_id):
        """Sets the completed_character_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        ID of the character which completed this job  # noqa: E501

        :param completed_character_id: The completed_character_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """

        self._completed_character_id = completed_character_id

    @property
    def completed_date(self):
        """Gets the completed_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Date and time when this job was completed  # noqa: E501

        :return: The completed_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Date and time when this job was completed  # noqa: E501

        :param completed_date: The completed_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: datetime
        """

        self._completed_date = completed_date

    @property
    def cost(self):
        """Gets the cost of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        The sume of job installation fee and industry facility tax  # noqa: E501

        :return: The cost of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this GetCorporationsCorporationIdIndustryJobs200Ok.

        The sume of job installation fee and industry facility tax  # noqa: E501

        :param cost: The cost of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def duration(self):
        """Gets the duration of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Job duration in seconds  # noqa: E501

        :return: The duration of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Job duration in seconds  # noqa: E501

        :param duration: The duration of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def end_date(self):
        """Gets the end_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Date and time when this job finished  # noqa: E501

        :return: The end_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Date and time when this job finished  # noqa: E501

        :param end_date: The end_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def facility_id(self):
        """Gets the facility_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        ID of the facility where this job is running  # noqa: E501

        :return: The facility_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        ID of the facility where this job is running  # noqa: E501

        :param facility_id: The facility_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")  # noqa: E501

        self._facility_id = facility_id

    @property
    def installer_id(self):
        """Gets the installer_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        ID of the character which installed this job  # noqa: E501

        :return: The installer_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._installer_id

    @installer_id.setter
    def installer_id(self, installer_id):
        """Sets the installer_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        ID of the character which installed this job  # noqa: E501

        :param installer_id: The installer_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if installer_id is None:
            raise ValueError("Invalid value for `installer_id`, must not be `None`")  # noqa: E501

        self._installer_id = installer_id

    @property
    def job_id(self):
        """Gets the job_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Unique job ID  # noqa: E501

        :return: The job_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Unique job ID  # noqa: E501

        :param job_id: The job_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def licensed_runs(self):
        """Gets the licensed_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Number of runs blueprint is licensed for  # noqa: E501

        :return: The licensed_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._licensed_runs

    @licensed_runs.setter
    def licensed_runs(self, licensed_runs):
        """Sets the licensed_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Number of runs blueprint is licensed for  # noqa: E501

        :param licensed_runs: The licensed_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """

        self._licensed_runs = licensed_runs

    @property
    def location_id(self):
        """Gets the location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        ID of the location for the industry facility  # noqa: E501

        :return: The location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        ID of the location for the industry facility  # noqa: E501

        :param location_id: The location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def output_location_id(self):
        """Gets the output_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility  # noqa: E501

        :return: The output_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._output_location_id

    @output_location_id.setter
    def output_location_id(self, output_location_id):
        """Sets the output_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Location ID of the location to which the output of the job will be delivered. Normally a station ID, but can also be a corporation facility  # noqa: E501

        :param output_location_id: The output_location_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if output_location_id is None:
            raise ValueError("Invalid value for `output_location_id`, must not be `None`")  # noqa: E501

        self._output_location_id = output_location_id

    @property
    def pause_date(self):
        """Gets the pause_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Date and time when this job was paused (i.e. time when the facility where this job was installed went offline)  # noqa: E501

        :return: The pause_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._pause_date

    @pause_date.setter
    def pause_date(self, pause_date):
        """Sets the pause_date of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Date and time when this job was paused (i.e. time when the facility where this job was installed went offline)  # noqa: E501

        :param pause_date: The pause_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: datetime
        """

        self._pause_date = pause_date

    @property
    def probability(self):
        """Gets the probability of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Chance of success for invention  # noqa: E501

        :return: The probability of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Chance of success for invention  # noqa: E501

        :param probability: The probability of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: float
        """

        self._probability = probability

    @property
    def product_type_id(self):
        """Gets the product_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Type ID of product (manufactured, copied or invented)  # noqa: E501

        :return: The product_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Type ID of product (manufactured, copied or invented)  # noqa: E501

        :param product_type_id: The product_type_id of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """

        self._product_type_id = product_type_id

    @property
    def runs(self):
        """Gets the runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Number of runs for a manufacturing job, or number of copies to make for a blueprint copy  # noqa: E501

        :return: The runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Number of runs for a manufacturing job, or number of copies to make for a blueprint copy  # noqa: E501

        :param runs: The runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """
        if runs is None:
            raise ValueError("Invalid value for `runs`, must not be `None`")  # noqa: E501

        self._runs = runs

    @property
    def start_date(self):
        """Gets the start_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Date and time when this job started  # noqa: E501

        :return: The start_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Date and time when this job started  # noqa: E501

        :param start_date: The start_date of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        status string  # noqa: E501

        :return: The status of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetCorporationsCorporationIdIndustryJobs200Ok.

        status string  # noqa: E501

        :param status: The status of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["active", "cancelled", "delivered", "paused", "ready", "reverted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def successful_runs(self):
        """Gets the successful_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501

        Number of successful runs for this job. Equal to runs unless this is an invention job  # noqa: E501

        :return: The successful_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :rtype: int
        """
        return self._successful_runs

    @successful_runs.setter
    def successful_runs(self, successful_runs):
        """Sets the successful_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.

        Number of successful runs for this job. Equal to runs unless this is an invention job  # noqa: E501

        :param successful_runs: The successful_runs of this GetCorporationsCorporationIdIndustryJobs200Ok.  # noqa: E501
        :type: int
        """

        self._successful_runs = successful_runs

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
        if issubclass(GetCorporationsCorporationIdIndustryJobs200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdIndustryJobs200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
