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


class CSProjectTotalsReportItem(object):
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
        'project_id': 'int',
        'project_name': 'str',
        'span_seconds': 'int'
    }

    attribute_map = {
        'organisation_id': 'OrganisationId',
        'user_id': 'UserId',
        'project_id': 'ProjectId',
        'project_name': 'ProjectName',
        'span_seconds': 'SpanSeconds'
    }

    def __init__(self, organisation_id=None, user_id=None, project_id=None, project_name=None, span_seconds=None):  # noqa: E501
        """CSProjectTotalsReportItem - a model defined in Swagger"""  # noqa: E501

        self._organisation_id = None
        self._user_id = None
        self._project_id = None
        self._project_name = None
        self._span_seconds = None
        self.discriminator = None

        if organisation_id is not None:
            self.organisation_id = organisation_id
        if user_id is not None:
            self.user_id = user_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if span_seconds is not None:
            self.span_seconds = span_seconds

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CSProjectTotalsReportItem.  # noqa: E501


        :return: The organisation_id of this CSProjectTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CSProjectTotalsReportItem.


        :param organisation_id: The organisation_id of this CSProjectTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def user_id(self):
        """Gets the user_id of this CSProjectTotalsReportItem.  # noqa: E501


        :return: The user_id of this CSProjectTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSProjectTotalsReportItem.


        :param user_id: The user_id of this CSProjectTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def project_id(self):
        """Gets the project_id of this CSProjectTotalsReportItem.  # noqa: E501


        :return: The project_id of this CSProjectTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CSProjectTotalsReportItem.


        :param project_id: The project_id of this CSProjectTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this CSProjectTotalsReportItem.  # noqa: E501


        :return: The project_name of this CSProjectTotalsReportItem.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CSProjectTotalsReportItem.


        :param project_name: The project_name of this CSProjectTotalsReportItem.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def span_seconds(self):
        """Gets the span_seconds of this CSProjectTotalsReportItem.  # noqa: E501


        :return: The span_seconds of this CSProjectTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._span_seconds

    @span_seconds.setter
    def span_seconds(self, span_seconds):
        """Sets the span_seconds of this CSProjectTotalsReportItem.


        :param span_seconds: The span_seconds of this CSProjectTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._span_seconds = span_seconds

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
        if not isinstance(other, CSProjectTotalsReportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
