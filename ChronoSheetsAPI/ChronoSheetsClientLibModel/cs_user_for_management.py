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

from ChronoSheetsAPI.ChronoSheetsClientLibModel.cs_cs_organisation import CSOrganisation  # noqa: F401,E501


class CSUserForManagement(object):
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
        'is_account_active': 'bool',
        'id': 'int',
        'organisation_id': 'int',
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str',
        'roles': 'int',
        'alert_settings': 'int',
        'setup_wizard_required': 'bool',
        'is_subscribed_to_newsletter': 'bool',
        'organisation': 'CSOrganisation'
    }

    attribute_map = {
        'is_account_active': 'IsAccountActive',
        'id': 'Id',
        'organisation_id': 'OrganisationId',
        'user_name': 'UserName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'email_address': 'EmailAddress',
        'roles': 'Roles',
        'alert_settings': 'AlertSettings',
        'setup_wizard_required': 'SetupWizardRequired',
        'is_subscribed_to_newsletter': 'IsSubscribedToNewsletter',
        'organisation': 'Organisation'
    }

    def __init__(self, is_account_active=None, id=None, organisation_id=None, user_name=None, first_name=None, last_name=None, email_address=None, roles=None, alert_settings=None, setup_wizard_required=None, is_subscribed_to_newsletter=None, organisation=None):  # noqa: E501
        """CSUserForManagement - a model defined in Swagger"""  # noqa: E501

        self._is_account_active = None
        self._id = None
        self._organisation_id = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._roles = None
        self._alert_settings = None
        self._setup_wizard_required = None
        self._is_subscribed_to_newsletter = None
        self._organisation = None
        self.discriminator = None

        if is_account_active is not None:
            self.is_account_active = is_account_active
        if id is not None:
            self.id = id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if user_name is not None:
            self.user_name = user_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if roles is not None:
            self.roles = roles
        if alert_settings is not None:
            self.alert_settings = alert_settings
        if setup_wizard_required is not None:
            self.setup_wizard_required = setup_wizard_required
        if is_subscribed_to_newsletter is not None:
            self.is_subscribed_to_newsletter = is_subscribed_to_newsletter
        if organisation is not None:
            self.organisation = organisation

    @property
    def is_account_active(self):
        """Gets the is_account_active of this CSUserForManagement.  # noqa: E501


        :return: The is_account_active of this CSUserForManagement.  # noqa: E501
        :rtype: bool
        """
        return self._is_account_active

    @is_account_active.setter
    def is_account_active(self, is_account_active):
        """Sets the is_account_active of this CSUserForManagement.


        :param is_account_active: The is_account_active of this CSUserForManagement.  # noqa: E501
        :type: bool
        """

        self._is_account_active = is_account_active

    @property
    def id(self):
        """Gets the id of this CSUserForManagement.  # noqa: E501


        :return: The id of this CSUserForManagement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CSUserForManagement.


        :param id: The id of this CSUserForManagement.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CSUserForManagement.  # noqa: E501


        :return: The organisation_id of this CSUserForManagement.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CSUserForManagement.


        :param organisation_id: The organisation_id of this CSUserForManagement.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def user_name(self):
        """Gets the user_name of this CSUserForManagement.  # noqa: E501


        :return: The user_name of this CSUserForManagement.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CSUserForManagement.


        :param user_name: The user_name of this CSUserForManagement.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this CSUserForManagement.  # noqa: E501


        :return: The first_name of this CSUserForManagement.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CSUserForManagement.


        :param first_name: The first_name of this CSUserForManagement.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CSUserForManagement.  # noqa: E501


        :return: The last_name of this CSUserForManagement.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CSUserForManagement.


        :param last_name: The last_name of this CSUserForManagement.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this CSUserForManagement.  # noqa: E501


        :return: The email_address of this CSUserForManagement.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSUserForManagement.


        :param email_address: The email_address of this CSUserForManagement.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def roles(self):
        """Gets the roles of this CSUserForManagement.  # noqa: E501


        :return: The roles of this CSUserForManagement.  # noqa: E501
        :rtype: int
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CSUserForManagement.


        :param roles: The roles of this CSUserForManagement.  # noqa: E501
        :type: int
        """

        self._roles = roles

    @property
    def alert_settings(self):
        """Gets the alert_settings of this CSUserForManagement.  # noqa: E501


        :return: The alert_settings of this CSUserForManagement.  # noqa: E501
        :rtype: int
        """
        return self._alert_settings

    @alert_settings.setter
    def alert_settings(self, alert_settings):
        """Sets the alert_settings of this CSUserForManagement.


        :param alert_settings: The alert_settings of this CSUserForManagement.  # noqa: E501
        :type: int
        """

        self._alert_settings = alert_settings

    @property
    def setup_wizard_required(self):
        """Gets the setup_wizard_required of this CSUserForManagement.  # noqa: E501


        :return: The setup_wizard_required of this CSUserForManagement.  # noqa: E501
        :rtype: bool
        """
        return self._setup_wizard_required

    @setup_wizard_required.setter
    def setup_wizard_required(self, setup_wizard_required):
        """Sets the setup_wizard_required of this CSUserForManagement.


        :param setup_wizard_required: The setup_wizard_required of this CSUserForManagement.  # noqa: E501
        :type: bool
        """

        self._setup_wizard_required = setup_wizard_required

    @property
    def is_subscribed_to_newsletter(self):
        """Gets the is_subscribed_to_newsletter of this CSUserForManagement.  # noqa: E501


        :return: The is_subscribed_to_newsletter of this CSUserForManagement.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_newsletter

    @is_subscribed_to_newsletter.setter
    def is_subscribed_to_newsletter(self, is_subscribed_to_newsletter):
        """Sets the is_subscribed_to_newsletter of this CSUserForManagement.


        :param is_subscribed_to_newsletter: The is_subscribed_to_newsletter of this CSUserForManagement.  # noqa: E501
        :type: bool
        """

        self._is_subscribed_to_newsletter = is_subscribed_to_newsletter

    @property
    def organisation(self):
        """Gets the organisation of this CSUserForManagement.  # noqa: E501


        :return: The organisation of this CSUserForManagement.  # noqa: E501
        :rtype: CSOrganisation
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this CSUserForManagement.


        :param organisation: The organisation of this CSUserForManagement.  # noqa: E501
        :type: CSOrganisation
        """

        self._organisation = organisation

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
        if not isinstance(other, CSUserForManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
