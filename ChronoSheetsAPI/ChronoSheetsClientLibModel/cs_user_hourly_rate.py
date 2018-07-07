# coding: utf-8

"""
    The ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  </p>  <p>      First Steps:       <ol>          <li>Make sure you've <a href='/HomeV2/App/sign-up'>signed up to ChronoSheets</a> to get yourself a user account</li>          <li>Confirm your account by following the link sent to your email address.  This will activate your account</li>          <li>Use your username and password to obtain an Auth Token by using the DoLogin method inside the UserProfile section below.  Use the Auth Token as an argument to the other methods</li>          <li>Try different methods in the API Playground to learn about the API</li>          <li>If you're stuck, try the full getting started guide on the <a href='/Home/ApiDocs'>API Toolkit</a> page.</li>      </ol>  </p>  <p>      Further Steps:       <ul>          <li>Create a mobile app (iOS, Android or Windows) using one of the ChronoSheets Mobile SDKs</li>          <li>Create a custom integration with your app using one of the ChronoSheets API Client Libraries.</li>      </ul>      Read more about the API Toolkit on the <a href='/Home/ApiDocs'>API Toolkit</a> page.  </p></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CSUserHourlyRate(object):
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
        'rate_id': 'int',
        'user_id': 'int',
        'organisation_id': 'int',
        'is_current': 'bool',
        'hourly_rate': 'float',
        'hourly_overtime_rate': 'float',
        'start_date_time': 'datetime',
        'end_date_time': 'datetime'
    }

    attribute_map = {
        'rate_id': 'RateId',
        'user_id': 'UserId',
        'organisation_id': 'OrganisationId',
        'is_current': 'IsCurrent',
        'hourly_rate': 'HourlyRate',
        'hourly_overtime_rate': 'HourlyOvertimeRate',
        'start_date_time': 'StartDateTime',
        'end_date_time': 'EndDateTime'
    }

    def __init__(self, rate_id=None, user_id=None, organisation_id=None, is_current=None, hourly_rate=None, hourly_overtime_rate=None, start_date_time=None, end_date_time=None):  # noqa: E501
        """CSUserHourlyRate - a model defined in Swagger"""  # noqa: E501

        self._rate_id = None
        self._user_id = None
        self._organisation_id = None
        self._is_current = None
        self._hourly_rate = None
        self._hourly_overtime_rate = None
        self._start_date_time = None
        self._end_date_time = None
        self.discriminator = None

        if rate_id is not None:
            self.rate_id = rate_id
        if user_id is not None:
            self.user_id = user_id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if is_current is not None:
            self.is_current = is_current
        if hourly_rate is not None:
            self.hourly_rate = hourly_rate
        if hourly_overtime_rate is not None:
            self.hourly_overtime_rate = hourly_overtime_rate
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time

    @property
    def rate_id(self):
        """Gets the rate_id of this CSUserHourlyRate.  # noqa: E501


        :return: The rate_id of this CSUserHourlyRate.  # noqa: E501
        :rtype: int
        """
        return self._rate_id

    @rate_id.setter
    def rate_id(self, rate_id):
        """Sets the rate_id of this CSUserHourlyRate.


        :param rate_id: The rate_id of this CSUserHourlyRate.  # noqa: E501
        :type: int
        """

        self._rate_id = rate_id

    @property
    def user_id(self):
        """Gets the user_id of this CSUserHourlyRate.  # noqa: E501


        :return: The user_id of this CSUserHourlyRate.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSUserHourlyRate.


        :param user_id: The user_id of this CSUserHourlyRate.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CSUserHourlyRate.  # noqa: E501


        :return: The organisation_id of this CSUserHourlyRate.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CSUserHourlyRate.


        :param organisation_id: The organisation_id of this CSUserHourlyRate.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def is_current(self):
        """Gets the is_current of this CSUserHourlyRate.  # noqa: E501


        :return: The is_current of this CSUserHourlyRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_current

    @is_current.setter
    def is_current(self, is_current):
        """Sets the is_current of this CSUserHourlyRate.


        :param is_current: The is_current of this CSUserHourlyRate.  # noqa: E501
        :type: bool
        """

        self._is_current = is_current

    @property
    def hourly_rate(self):
        """Gets the hourly_rate of this CSUserHourlyRate.  # noqa: E501


        :return: The hourly_rate of this CSUserHourlyRate.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        """Sets the hourly_rate of this CSUserHourlyRate.


        :param hourly_rate: The hourly_rate of this CSUserHourlyRate.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def hourly_overtime_rate(self):
        """Gets the hourly_overtime_rate of this CSUserHourlyRate.  # noqa: E501


        :return: The hourly_overtime_rate of this CSUserHourlyRate.  # noqa: E501
        :rtype: float
        """
        return self._hourly_overtime_rate

    @hourly_overtime_rate.setter
    def hourly_overtime_rate(self, hourly_overtime_rate):
        """Sets the hourly_overtime_rate of this CSUserHourlyRate.


        :param hourly_overtime_rate: The hourly_overtime_rate of this CSUserHourlyRate.  # noqa: E501
        :type: float
        """

        self._hourly_overtime_rate = hourly_overtime_rate

    @property
    def start_date_time(self):
        """Gets the start_date_time of this CSUserHourlyRate.  # noqa: E501


        :return: The start_date_time of this CSUserHourlyRate.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this CSUserHourlyRate.


        :param start_date_time: The start_date_time of this CSUserHourlyRate.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this CSUserHourlyRate.  # noqa: E501


        :return: The end_date_time of this CSUserHourlyRate.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this CSUserHourlyRate.


        :param end_date_time: The end_date_time of this CSUserHourlyRate.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CSUserHourlyRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
