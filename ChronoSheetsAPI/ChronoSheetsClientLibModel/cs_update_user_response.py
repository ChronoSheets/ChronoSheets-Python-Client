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


class CSUpdateUserResponse(object):
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
        'organisation_id': 'int',
        'user_id': 'int',
        'validation_errors': 'list[str]'
    }

    attribute_map = {
        'organisation_id': 'OrganisationId',
        'user_id': 'UserId',
        'validation_errors': 'ValidationErrors'
    }

    def __init__(self, organisation_id=None, user_id=None, validation_errors=None):  # noqa: E501
        """CSUpdateUserResponse - a model defined in Swagger"""  # noqa: E501

        self._organisation_id = None
        self._user_id = None
        self._validation_errors = None
        self.discriminator = None

        if organisation_id is not None:
            self.organisation_id = organisation_id
        if user_id is not None:
            self.user_id = user_id
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CSUpdateUserResponse.  # noqa: E501


        :return: The organisation_id of this CSUpdateUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CSUpdateUserResponse.


        :param organisation_id: The organisation_id of this CSUpdateUserResponse.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def user_id(self):
        """Gets the user_id of this CSUpdateUserResponse.  # noqa: E501


        :return: The user_id of this CSUpdateUserResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSUpdateUserResponse.


        :param user_id: The user_id of this CSUpdateUserResponse.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def validation_errors(self):
        """Gets the validation_errors of this CSUpdateUserResponse.  # noqa: E501


        :return: The validation_errors of this CSUpdateUserResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this CSUpdateUserResponse.


        :param validation_errors: The validation_errors of this CSUpdateUserResponse.  # noqa: E501
        :type: list[str]
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, CSUpdateUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
