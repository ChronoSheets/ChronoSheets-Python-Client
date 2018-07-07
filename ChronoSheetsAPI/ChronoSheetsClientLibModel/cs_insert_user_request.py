# coding: utf-8

"""
    The ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CSInsertUserRequest(object):
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
        'email_address': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'is_subscribed_to_newsletter': 'bool',
        'roles': 'int',
        'alert_settings': 'int',
        'user_name': 'str',
        'hourly_pay_rate': 'float',
        'hourly_overtime_pay_rate': 'float',
        'current_date': 'datetime'
    }

    attribute_map = {
        'email_address': 'EmailAddress',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'is_subscribed_to_newsletter': 'IsSubscribedToNewsletter',
        'roles': 'Roles',
        'alert_settings': 'AlertSettings',
        'user_name': 'UserName',
        'hourly_pay_rate': 'HourlyPayRate',
        'hourly_overtime_pay_rate': 'HourlyOvertimePayRate',
        'current_date': 'CurrentDate'
    }

    def __init__(self, email_address=None, first_name=None, last_name=None, is_subscribed_to_newsletter=None, roles=None, alert_settings=None, user_name=None, hourly_pay_rate=None, hourly_overtime_pay_rate=None, current_date=None):  # noqa: E501
        """CSInsertUserRequest - a model defined in Swagger"""  # noqa: E501

        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._is_subscribed_to_newsletter = None
        self._roles = None
        self._alert_settings = None
        self._user_name = None
        self._hourly_pay_rate = None
        self._hourly_overtime_pay_rate = None
        self._current_date = None
        self.discriminator = None

        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if is_subscribed_to_newsletter is not None:
            self.is_subscribed_to_newsletter = is_subscribed_to_newsletter
        if roles is not None:
            self.roles = roles
        if alert_settings is not None:
            self.alert_settings = alert_settings
        if user_name is not None:
            self.user_name = user_name
        if hourly_pay_rate is not None:
            self.hourly_pay_rate = hourly_pay_rate
        if hourly_overtime_pay_rate is not None:
            self.hourly_overtime_pay_rate = hourly_overtime_pay_rate
        if current_date is not None:
            self.current_date = current_date

    @property
    def email_address(self):
        """Gets the email_address of this CSInsertUserRequest.  # noqa: E501

        The Email Address of the employee  # noqa: E501

        :return: The email_address of this CSInsertUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSInsertUserRequest.

        The Email Address of the employee  # noqa: E501

        :param email_address: The email_address of this CSInsertUserRequest.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this CSInsertUserRequest.  # noqa: E501

        The First Name of the employee  # noqa: E501

        :return: The first_name of this CSInsertUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CSInsertUserRequest.

        The First Name of the employee  # noqa: E501

        :param first_name: The first_name of this CSInsertUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CSInsertUserRequest.  # noqa: E501

        The Last Name of the employee  # noqa: E501

        :return: The last_name of this CSInsertUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CSInsertUserRequest.

        The Last Name of the employee  # noqa: E501

        :param last_name: The last_name of this CSInsertUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def is_subscribed_to_newsletter(self):
        """Gets the is_subscribed_to_newsletter of this CSInsertUserRequest.  # noqa: E501

        Whether or not the employee is subscribed to ChronoSheets newsletters  # noqa: E501

        :return: The is_subscribed_to_newsletter of this CSInsertUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_newsletter

    @is_subscribed_to_newsletter.setter
    def is_subscribed_to_newsletter(self, is_subscribed_to_newsletter):
        """Sets the is_subscribed_to_newsletter of this CSInsertUserRequest.

        Whether or not the employee is subscribed to ChronoSheets newsletters  # noqa: E501

        :param is_subscribed_to_newsletter: The is_subscribed_to_newsletter of this CSInsertUserRequest.  # noqa: E501
        :type: bool
        """

        self._is_subscribed_to_newsletter = is_subscribed_to_newsletter

    @property
    def roles(self):
        """Gets the roles of this CSInsertUserRequest.  # noqa: E501

        A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details  # noqa: E501

        :return: The roles of this CSInsertUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CSInsertUserRequest.

        A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details  # noqa: E501

        :param roles: The roles of this CSInsertUserRequest.  # noqa: E501
        :type: int
        """

        self._roles = roles

    @property
    def alert_settings(self):
        """Gets the alert_settings of this CSInsertUserRequest.  # noqa: E501

        A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details  # noqa: E501

        :return: The alert_settings of this CSInsertUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._alert_settings

    @alert_settings.setter
    def alert_settings(self, alert_settings):
        """Sets the alert_settings of this CSInsertUserRequest.

        A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details  # noqa: E501

        :param alert_settings: The alert_settings of this CSInsertUserRequest.  # noqa: E501
        :type: int
        """

        self._alert_settings = alert_settings

    @property
    def user_name(self):
        """Gets the user_name of this CSInsertUserRequest.  # noqa: E501

        The UserName of the employee.  This can be used when logging into ChronoSheets  # noqa: E501

        :return: The user_name of this CSInsertUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CSInsertUserRequest.

        The UserName of the employee.  This can be used when logging into ChronoSheets  # noqa: E501

        :param user_name: The user_name of this CSInsertUserRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def hourly_pay_rate(self):
        """Gets the hourly_pay_rate of this CSInsertUserRequest.  # noqa: E501

        Set the starting usual Hourly Pay Rate with this value.  This is the Pay Rate the employee receives for working during Rostered Hours  # noqa: E501

        :return: The hourly_pay_rate of this CSInsertUserRequest.  # noqa: E501
        :rtype: float
        """
        return self._hourly_pay_rate

    @hourly_pay_rate.setter
    def hourly_pay_rate(self, hourly_pay_rate):
        """Sets the hourly_pay_rate of this CSInsertUserRequest.

        Set the starting usual Hourly Pay Rate with this value.  This is the Pay Rate the employee receives for working during Rostered Hours  # noqa: E501

        :param hourly_pay_rate: The hourly_pay_rate of this CSInsertUserRequest.  # noqa: E501
        :type: float
        """

        self._hourly_pay_rate = hourly_pay_rate

    @property
    def hourly_overtime_pay_rate(self):
        """Gets the hourly_overtime_pay_rate of this CSInsertUserRequest.  # noqa: E501

        Set the starting usual Overtime Hourly Pay Rate with this value.  This is the Pay Rate the employee receives for working outside of Rostered Hours  # noqa: E501

        :return: The hourly_overtime_pay_rate of this CSInsertUserRequest.  # noqa: E501
        :rtype: float
        """
        return self._hourly_overtime_pay_rate

    @hourly_overtime_pay_rate.setter
    def hourly_overtime_pay_rate(self, hourly_overtime_pay_rate):
        """Sets the hourly_overtime_pay_rate of this CSInsertUserRequest.

        Set the starting usual Overtime Hourly Pay Rate with this value.  This is the Pay Rate the employee receives for working outside of Rostered Hours  # noqa: E501

        :param hourly_overtime_pay_rate: The hourly_overtime_pay_rate of this CSInsertUserRequest.  # noqa: E501
        :type: float
        """

        self._hourly_overtime_pay_rate = hourly_overtime_pay_rate

    @property
    def current_date(self):
        """Gets the current_date of this CSInsertUserRequest.  # noqa: E501

        The Current date time  # noqa: E501

        :return: The current_date of this CSInsertUserRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._current_date

    @current_date.setter
    def current_date(self, current_date):
        """Sets the current_date of this CSInsertUserRequest.

        The Current date time  # noqa: E501

        :param current_date: The current_date of this CSInsertUserRequest.  # noqa: E501
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
        if not isinstance(other, CSInsertUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
