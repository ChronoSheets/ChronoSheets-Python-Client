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


class UpdateProjectRequest(object):
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
        'project_id': 'int',
        'project_name': 'str',
        'cost_estimation': 'float',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'project_id': 'ProjectId',
        'project_name': 'ProjectName',
        'cost_estimation': 'CostEstimation',
        'start_date': 'StartDate',
        'end_date': 'EndDate'
    }

    def __init__(self, project_id=None, project_name=None, cost_estimation=None, start_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """UpdateProjectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._project_name = None
        self._cost_estimation = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if cost_estimation is not None:
            self.cost_estimation = cost_estimation
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def project_id(self):
        """Gets the project_id of this UpdateProjectRequest.  # noqa: E501

        The Id of the Project that is to be updated  # noqa: E501

        :return: The project_id of this UpdateProjectRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateProjectRequest.

        The Id of the Project that is to be updated  # noqa: E501

        :param project_id: The project_id of this UpdateProjectRequest.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this UpdateProjectRequest.  # noqa: E501

        The new name of the Project  # noqa: E501

        :return: The project_name of this UpdateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateProjectRequest.

        The new name of the Project  # noqa: E501

        :param project_name: The project_name of this UpdateProjectRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def cost_estimation(self):
        """Gets the cost_estimation of this UpdateProjectRequest.  # noqa: E501

        The updated estimated cost of the Project  # noqa: E501

        :return: The cost_estimation of this UpdateProjectRequest.  # noqa: E501
        :rtype: float
        """
        return self._cost_estimation

    @cost_estimation.setter
    def cost_estimation(self, cost_estimation):
        """Sets the cost_estimation of this UpdateProjectRequest.

        The updated estimated cost of the Project  # noqa: E501

        :param cost_estimation: The cost_estimation of this UpdateProjectRequest.  # noqa: E501
        :type: float
        """

        self._cost_estimation = cost_estimation

    @property
    def start_date(self):
        """Gets the start_date of this UpdateProjectRequest.  # noqa: E501

        The updated project start date  # noqa: E501

        :return: The start_date of this UpdateProjectRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this UpdateProjectRequest.

        The updated project start date  # noqa: E501

        :param start_date: The start_date of this UpdateProjectRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this UpdateProjectRequest.  # noqa: E501

        The update project end date  # noqa: E501

        :return: The end_date of this UpdateProjectRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this UpdateProjectRequest.

        The update project end date  # noqa: E501

        :param end_date: The end_date of this UpdateProjectRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, UpdateProjectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateProjectRequest):
            return True

        return self.to_dict() != other.to_dict()