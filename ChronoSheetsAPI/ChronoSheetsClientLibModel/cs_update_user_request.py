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


class CSUpdateUserRequest(object):
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
        'email_address': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'is_subscribed_to_newsletter': 'bool',
        'is_account_active': 'bool',
        'roles': 'int',
        'alert_settings': 'int'
    }

    attribute_map = {
        'user_id': 'UserId',
        'email_address': 'EmailAddress',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'is_subscribed_to_newsletter': 'IsSubscribedToNewsletter',
        'is_account_active': 'IsAccountActive',
        'roles': 'Roles',
        'alert_settings': 'AlertSettings'
    }

    def __init__(self, user_id=None, email_address=None, first_name=None, last_name=None, is_subscribed_to_newsletter=None, is_account_active=None, roles=None, alert_settings=None):  # noqa: E501
        """CSUpdateUserRequest - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._is_subscribed_to_newsletter = None
        self._is_account_active = None
        self._roles = None
        self._alert_settings = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if is_subscribed_to_newsletter is not None:
            self.is_subscribed_to_newsletter = is_subscribed_to_newsletter
        if is_account_active is not None:
            self.is_account_active = is_account_active
        if roles is not None:
            self.roles = roles
        if alert_settings is not None:
            self.alert_settings = alert_settings

    @property
    def user_id(self):
        """Gets the user_id of this CSUpdateUserRequest.  # noqa: E501

        The Id of the User that is to be updated  # noqa: E501

        :return: The user_id of this CSUpdateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSUpdateUserRequest.

        The Id of the User that is to be updated  # noqa: E501

        :param user_id: The user_id of this CSUpdateUserRequest.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def email_address(self):
        """Gets the email_address of this CSUpdateUserRequest.  # noqa: E501

        The Email Address of the employee  # noqa: E501

        :return: The email_address of this CSUpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSUpdateUserRequest.

        The Email Address of the employee  # noqa: E501

        :param email_address: The email_address of this CSUpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this CSUpdateUserRequest.  # noqa: E501

        The First Name of the employee  # noqa: E501

        :return: The first_name of this CSUpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CSUpdateUserRequest.

        The First Name of the employee  # noqa: E501

        :param first_name: The first_name of this CSUpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CSUpdateUserRequest.  # noqa: E501

        The Last Name of the employee  # noqa: E501

        :return: The last_name of this CSUpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CSUpdateUserRequest.

        The Last Name of the employee  # noqa: E501

        :param last_name: The last_name of this CSUpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def is_subscribed_to_newsletter(self):
        """Gets the is_subscribed_to_newsletter of this CSUpdateUserRequest.  # noqa: E501

        Whether or not the employee is subscribed to ChronoSheets newsletters  # noqa: E501

        :return: The is_subscribed_to_newsletter of this CSUpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_newsletter

    @is_subscribed_to_newsletter.setter
    def is_subscribed_to_newsletter(self, is_subscribed_to_newsletter):
        """Sets the is_subscribed_to_newsletter of this CSUpdateUserRequest.

        Whether or not the employee is subscribed to ChronoSheets newsletters  # noqa: E501

        :param is_subscribed_to_newsletter: The is_subscribed_to_newsletter of this CSUpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._is_subscribed_to_newsletter = is_subscribed_to_newsletter

    @property
    def is_account_active(self):
        """Gets the is_account_active of this CSUpdateUserRequest.  # noqa: E501

        Whether or not the employee account is active  # noqa: E501

        :return: The is_account_active of this CSUpdateUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_account_active

    @is_account_active.setter
    def is_account_active(self, is_account_active):
        """Sets the is_account_active of this CSUpdateUserRequest.

        Whether or not the employee account is active  # noqa: E501

        :param is_account_active: The is_account_active of this CSUpdateUserRequest.  # noqa: E501
        :type: bool
        """

        self._is_account_active = is_account_active

    @property
    def roles(self):
        """Gets the roles of this CSUpdateUserRequest.  # noqa: E501

        A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details  # noqa: E501

        :return: The roles of this CSUpdateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CSUpdateUserRequest.

        A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details  # noqa: E501

        :param roles: The roles of this CSUpdateUserRequest.  # noqa: E501
        :type: int
        """

        self._roles = roles

    @property
    def alert_settings(self):
        """Gets the alert_settings of this CSUpdateUserRequest.  # noqa: E501

        A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details  # noqa: E501

        :return: The alert_settings of this CSUpdateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._alert_settings

    @alert_settings.setter
    def alert_settings(self, alert_settings):
        """Sets the alert_settings of this CSUpdateUserRequest.

        A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details  # noqa: E501

        :param alert_settings: The alert_settings of this CSUpdateUserRequest.  # noqa: E501
        :type: int
        """

        self._alert_settings = alert_settings

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
        if not isinstance(other, CSUpdateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
