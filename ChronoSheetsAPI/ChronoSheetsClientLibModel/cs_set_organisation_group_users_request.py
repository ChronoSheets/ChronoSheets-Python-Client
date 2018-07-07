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


class CSSetOrganisationGroupUsersRequest(object):
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
        'organisation_group_id': 'int',
        'csv_user_ids': 'str'
    }

    attribute_map = {
        'organisation_group_id': 'OrganisationGroupId',
        'csv_user_ids': 'CsvUserIds'
    }

    def __init__(self, organisation_group_id=None, csv_user_ids=None):  # noqa: E501
        """CSSetOrganisationGroupUsersRequest - a model defined in Swagger"""  # noqa: E501

        self._organisation_group_id = None
        self._csv_user_ids = None
        self.discriminator = None

        if organisation_group_id is not None:
            self.organisation_group_id = organisation_group_id
        if csv_user_ids is not None:
            self.csv_user_ids = csv_user_ids

    @property
    def organisation_group_id(self):
        """Gets the organisation_group_id of this CSSetOrganisationGroupUsersRequest.  # noqa: E501


        :return: The organisation_group_id of this CSSetOrganisationGroupUsersRequest.  # noqa: E501
        :rtype: int
        """
        return self._organisation_group_id

    @organisation_group_id.setter
    def organisation_group_id(self, organisation_group_id):
        """Sets the organisation_group_id of this CSSetOrganisationGroupUsersRequest.


        :param organisation_group_id: The organisation_group_id of this CSSetOrganisationGroupUsersRequest.  # noqa: E501
        :type: int
        """

        self._organisation_group_id = organisation_group_id

    @property
    def csv_user_ids(self):
        """Gets the csv_user_ids of this CSSetOrganisationGroupUsersRequest.  # noqa: E501


        :return: The csv_user_ids of this CSSetOrganisationGroupUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._csv_user_ids

    @csv_user_ids.setter
    def csv_user_ids(self, csv_user_ids):
        """Sets the csv_user_ids of this CSSetOrganisationGroupUsersRequest.


        :param csv_user_ids: The csv_user_ids of this CSSetOrganisationGroupUsersRequest.  # noqa: E501
        :type: str
        """

        self._csv_user_ids = csv_user_ids

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
        if not isinstance(other, CSSetOrganisationGroupUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
