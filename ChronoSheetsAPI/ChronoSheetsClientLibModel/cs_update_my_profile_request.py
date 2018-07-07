# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CSUpdateMyProfileRequest(object):
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
        'old_password': 'str',
        'new_password': 'str',
        'confirm_new_password': 'str',
        'is_subscribed_to_newsletter': 'bool',
        'wants_to_change_password': 'bool'
    }

    attribute_map = {
        'email_address': 'EmailAddress',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'old_password': 'OldPassword',
        'new_password': 'NewPassword',
        'confirm_new_password': 'ConfirmNewPassword',
        'is_subscribed_to_newsletter': 'IsSubscribedToNewsletter',
        'wants_to_change_password': 'WantsToChangePassword'
    }

    def __init__(self, email_address=None, first_name=None, last_name=None, old_password=None, new_password=None, confirm_new_password=None, is_subscribed_to_newsletter=None, wants_to_change_password=None):  # noqa: E501
        """CSUpdateMyProfileRequest - a model defined in Swagger"""  # noqa: E501

        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._old_password = None
        self._new_password = None
        self._confirm_new_password = None
        self._is_subscribed_to_newsletter = None
        self._wants_to_change_password = None
        self.discriminator = None

        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if old_password is not None:
            self.old_password = old_password
        if new_password is not None:
            self.new_password = new_password
        if confirm_new_password is not None:
            self.confirm_new_password = confirm_new_password
        if is_subscribed_to_newsletter is not None:
            self.is_subscribed_to_newsletter = is_subscribed_to_newsletter
        if wants_to_change_password is not None:
            self.wants_to_change_password = wants_to_change_password

    @property
    def email_address(self):
        """Gets the email_address of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The email_address of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSUpdateMyProfileRequest.


        :param email_address: The email_address of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The first_name of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CSUpdateMyProfileRequest.


        :param first_name: The first_name of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The last_name of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CSUpdateMyProfileRequest.


        :param last_name: The last_name of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def old_password(self):
        """Gets the old_password of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The old_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this CSUpdateMyProfileRequest.


        :param old_password: The old_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: str
        """

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The new_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this CSUpdateMyProfileRequest.


        :param new_password: The new_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

    @property
    def confirm_new_password(self):
        """Gets the confirm_new_password of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The confirm_new_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._confirm_new_password

    @confirm_new_password.setter
    def confirm_new_password(self, confirm_new_password):
        """Sets the confirm_new_password of this CSUpdateMyProfileRequest.


        :param confirm_new_password: The confirm_new_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: str
        """

        self._confirm_new_password = confirm_new_password

    @property
    def is_subscribed_to_newsletter(self):
        """Gets the is_subscribed_to_newsletter of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The is_subscribed_to_newsletter of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_newsletter

    @is_subscribed_to_newsletter.setter
    def is_subscribed_to_newsletter(self, is_subscribed_to_newsletter):
        """Sets the is_subscribed_to_newsletter of this CSUpdateMyProfileRequest.


        :param is_subscribed_to_newsletter: The is_subscribed_to_newsletter of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: bool
        """

        self._is_subscribed_to_newsletter = is_subscribed_to_newsletter

    @property
    def wants_to_change_password(self):
        """Gets the wants_to_change_password of this CSUpdateMyProfileRequest.  # noqa: E501


        :return: The wants_to_change_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._wants_to_change_password

    @wants_to_change_password.setter
    def wants_to_change_password(self, wants_to_change_password):
        """Sets the wants_to_change_password of this CSUpdateMyProfileRequest.


        :param wants_to_change_password: The wants_to_change_password of this CSUpdateMyProfileRequest.  # noqa: E501
        :type: bool
        """

        self._wants_to_change_password = wants_to_change_password

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
        if not isinstance(other, CSUpdateMyProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
