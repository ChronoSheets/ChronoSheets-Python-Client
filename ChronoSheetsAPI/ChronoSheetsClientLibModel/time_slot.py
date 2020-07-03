# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ChronoSheetsAPI.configuration import Configuration


class TimeSlot(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'day_type': 'str',
        'usual_hour_id': 'int',
        'start_hour': 'int',
        'start_minute': 'int',
        'end_hour': 'int',
        'end_minute': 'int',
        'is_valid': 'bool'
    }

    attribute_map = {
        'day_type': 'DayType',
        'usual_hour_id': 'UsualHourId',
        'start_hour': 'StartHour',
        'start_minute': 'StartMinute',
        'end_hour': 'EndHour',
        'end_minute': 'EndMinute',
        'is_valid': 'IsValid'
    }

    def __init__(self, day_type=None, usual_hour_id=None, start_hour=None, start_minute=None, end_hour=None, end_minute=None, is_valid=None, local_vars_configuration=None):  # noqa: E501
        """TimeSlot - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._day_type = None
        self._usual_hour_id = None
        self._start_hour = None
        self._start_minute = None
        self._end_hour = None
        self._end_minute = None
        self._is_valid = None
        self.discriminator = None

        if day_type is not None:
            self.day_type = day_type
        if usual_hour_id is not None:
            self.usual_hour_id = usual_hour_id
        if start_hour is not None:
            self.start_hour = start_hour
        if start_minute is not None:
            self.start_minute = start_minute
        if end_hour is not None:
            self.end_hour = end_hour
        if end_minute is not None:
            self.end_minute = end_minute
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def day_type(self):
        """Gets the day_type of this TimeSlot.  # noqa: E501


        :return: The day_type of this TimeSlot.  # noqa: E501
        :rtype: str
        """
        return self._day_type

    @day_type.setter
    def day_type(self, day_type):
        """Sets the day_type of this TimeSlot.


        :param day_type: The day_type of this TimeSlot.  # noqa: E501
        :type: str
        """
        allowed_values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and day_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `day_type` ({0}), must be one of {1}"  # noqa: E501
                .format(day_type, allowed_values)
            )

        self._day_type = day_type

    @property
    def usual_hour_id(self):
        """Gets the usual_hour_id of this TimeSlot.  # noqa: E501


        :return: The usual_hour_id of this TimeSlot.  # noqa: E501
        :rtype: int
        """
        return self._usual_hour_id

    @usual_hour_id.setter
    def usual_hour_id(self, usual_hour_id):
        """Sets the usual_hour_id of this TimeSlot.


        :param usual_hour_id: The usual_hour_id of this TimeSlot.  # noqa: E501
        :type: int
        """

        self._usual_hour_id = usual_hour_id

    @property
    def start_hour(self):
        """Gets the start_hour of this TimeSlot.  # noqa: E501


        :return: The start_hour of this TimeSlot.  # noqa: E501
        :rtype: int
        """
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        """Sets the start_hour of this TimeSlot.


        :param start_hour: The start_hour of this TimeSlot.  # noqa: E501
        :type: int
        """

        self._start_hour = start_hour

    @property
    def start_minute(self):
        """Gets the start_minute of this TimeSlot.  # noqa: E501


        :return: The start_minute of this TimeSlot.  # noqa: E501
        :rtype: int
        """
        return self._start_minute

    @start_minute.setter
    def start_minute(self, start_minute):
        """Sets the start_minute of this TimeSlot.


        :param start_minute: The start_minute of this TimeSlot.  # noqa: E501
        :type: int
        """

        self._start_minute = start_minute

    @property
    def end_hour(self):
        """Gets the end_hour of this TimeSlot.  # noqa: E501


        :return: The end_hour of this TimeSlot.  # noqa: E501
        :rtype: int
        """
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        """Sets the end_hour of this TimeSlot.


        :param end_hour: The end_hour of this TimeSlot.  # noqa: E501
        :type: int
        """

        self._end_hour = end_hour

    @property
    def end_minute(self):
        """Gets the end_minute of this TimeSlot.  # noqa: E501


        :return: The end_minute of this TimeSlot.  # noqa: E501
        :rtype: int
        """
        return self._end_minute

    @end_minute.setter
    def end_minute(self, end_minute):
        """Sets the end_minute of this TimeSlot.


        :param end_minute: The end_minute of this TimeSlot.  # noqa: E501
        :type: int
        """

        self._end_minute = end_minute

    @property
    def is_valid(self):
        """Gets the is_valid of this TimeSlot.  # noqa: E501


        :return: The is_valid of this TimeSlot.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this TimeSlot.


        :param is_valid: The is_valid of this TimeSlot.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeSlot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeSlot):
            return True

        return self.to_dict() != other.to_dict()