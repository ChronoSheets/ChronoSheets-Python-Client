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


class CSInsertUserHourlyRateRequest(object):
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
        'user_id': 'int',
        'hourly_rate': 'float',
        'hourly_overtime_rate': 'float',
        'current_date': 'datetime'
    }

    attribute_map = {
        'user_id': 'UserId',
        'hourly_rate': 'HourlyRate',
        'hourly_overtime_rate': 'HourlyOvertimeRate',
        'current_date': 'CurrentDate'
    }

    def __init__(self, user_id=None, hourly_rate=None, hourly_overtime_rate=None, current_date=None):  # noqa: E501
        """CSInsertUserHourlyRateRequest - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._hourly_rate = None
        self._hourly_overtime_rate = None
        self._current_date = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if hourly_rate is not None:
            self.hourly_rate = hourly_rate
        if hourly_overtime_rate is not None:
            self.hourly_overtime_rate = hourly_overtime_rate
        if current_date is not None:
            self.current_date = current_date

    @property
    def user_id(self):
        """Gets the user_id of this CSInsertUserHourlyRateRequest.  # noqa: E501

        The Id of the User that is getting the new set of Pay Rates  # noqa: E501

        :return: The user_id of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSInsertUserHourlyRateRequest.

        The Id of the User that is getting the new set of Pay Rates  # noqa: E501

        :param user_id: The user_id of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def hourly_rate(self):
        """Gets the hourly_rate of this CSInsertUserHourlyRateRequest.  # noqa: E501

        The Hourly Rate the employee should receive during their usual rostered hours  # noqa: E501

        :return: The hourly_rate of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        """Sets the hourly_rate of this CSInsertUserHourlyRateRequest.

        The Hourly Rate the employee should receive during their usual rostered hours  # noqa: E501

        :param hourly_rate: The hourly_rate of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def hourly_overtime_rate(self):
        """Gets the hourly_overtime_rate of this CSInsertUserHourlyRateRequest.  # noqa: E501

        The Hourly Rate the employee should receive during outside of their usual rostered hours  # noqa: E501

        :return: The hourly_overtime_rate of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :rtype: float
        """
        return self._hourly_overtime_rate

    @hourly_overtime_rate.setter
    def hourly_overtime_rate(self, hourly_overtime_rate):
        """Sets the hourly_overtime_rate of this CSInsertUserHourlyRateRequest.

        The Hourly Rate the employee should receive during outside of their usual rostered hours  # noqa: E501

        :param hourly_overtime_rate: The hourly_overtime_rate of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :type: float
        """

        self._hourly_overtime_rate = hourly_overtime_rate

    @property
    def current_date(self):
        """Gets the current_date of this CSInsertUserHourlyRateRequest.  # noqa: E501

        The current date time  # noqa: E501

        :return: The current_date of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._current_date

    @current_date.setter
    def current_date(self, current_date):
        """Sets the current_date of this CSInsertUserHourlyRateRequest.

        The current date time  # noqa: E501

        :param current_date: The current_date of this CSInsertUserHourlyRateRequest.  # noqa: E501
        :type: datetime
        """

        self._current_date = current_date

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
        if not isinstance(other, CSInsertUserHourlyRateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
