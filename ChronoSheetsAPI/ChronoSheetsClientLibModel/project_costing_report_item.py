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


class ProjectCostingReportItem(object):
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
        'client_id': 'int',
        'organisation_id': 'int',
        'client_name': 'str',
        'estimated_cost': 'float',
        'actual_cost_filtered': 'float',
        'actual_cost': 'float'
    }

    attribute_map = {
        'project_id': 'ProjectId',
        'project_name': 'ProjectName',
        'client_id': 'ClientId',
        'organisation_id': 'OrganisationId',
        'client_name': 'ClientName',
        'estimated_cost': 'EstimatedCost',
        'actual_cost_filtered': 'ActualCostFiltered',
        'actual_cost': 'ActualCost'
    }

    def __init__(self, project_id=None, project_name=None, client_id=None, organisation_id=None, client_name=None, estimated_cost=None, actual_cost_filtered=None, actual_cost=None, local_vars_configuration=None):  # noqa: E501
        """ProjectCostingReportItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._project_name = None
        self._client_id = None
        self._organisation_id = None
        self._client_name = None
        self._estimated_cost = None
        self._actual_cost_filtered = None
        self._actual_cost = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if client_id is not None:
            self.client_id = client_id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if client_name is not None:
            self.client_name = client_name
        if estimated_cost is not None:
            self.estimated_cost = estimated_cost
        if actual_cost_filtered is not None:
            self.actual_cost_filtered = actual_cost_filtered
        if actual_cost is not None:
            self.actual_cost = actual_cost

    @property
    def project_id(self):
        """Gets the project_id of this ProjectCostingReportItem.  # noqa: E501


        :return: The project_id of this ProjectCostingReportItem.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectCostingReportItem.


        :param project_id: The project_id of this ProjectCostingReportItem.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ProjectCostingReportItem.  # noqa: E501


        :return: The project_name of this ProjectCostingReportItem.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectCostingReportItem.


        :param project_name: The project_name of this ProjectCostingReportItem.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def client_id(self):
        """Gets the client_id of this ProjectCostingReportItem.  # noqa: E501


        :return: The client_id of this ProjectCostingReportItem.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ProjectCostingReportItem.


        :param client_id: The client_id of this ProjectCostingReportItem.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this ProjectCostingReportItem.  # noqa: E501


        :return: The organisation_id of this ProjectCostingReportItem.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this ProjectCostingReportItem.


        :param organisation_id: The organisation_id of this ProjectCostingReportItem.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def client_name(self):
        """Gets the client_name of this ProjectCostingReportItem.  # noqa: E501


        :return: The client_name of this ProjectCostingReportItem.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this ProjectCostingReportItem.


        :param client_name: The client_name of this ProjectCostingReportItem.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def estimated_cost(self):
        """Gets the estimated_cost of this ProjectCostingReportItem.  # noqa: E501


        :return: The estimated_cost of this ProjectCostingReportItem.  # noqa: E501
        :rtype: float
        """
        return self._estimated_cost

    @estimated_cost.setter
    def estimated_cost(self, estimated_cost):
        """Sets the estimated_cost of this ProjectCostingReportItem.


        :param estimated_cost: The estimated_cost of this ProjectCostingReportItem.  # noqa: E501
        :type: float
        """

        self._estimated_cost = estimated_cost

    @property
    def actual_cost_filtered(self):
        """Gets the actual_cost_filtered of this ProjectCostingReportItem.  # noqa: E501


        :return: The actual_cost_filtered of this ProjectCostingReportItem.  # noqa: E501
        :rtype: float
        """
        return self._actual_cost_filtered

    @actual_cost_filtered.setter
    def actual_cost_filtered(self, actual_cost_filtered):
        """Sets the actual_cost_filtered of this ProjectCostingReportItem.


        :param actual_cost_filtered: The actual_cost_filtered of this ProjectCostingReportItem.  # noqa: E501
        :type: float
        """

        self._actual_cost_filtered = actual_cost_filtered

    @property
    def actual_cost(self):
        """Gets the actual_cost of this ProjectCostingReportItem.  # noqa: E501


        :return: The actual_cost of this ProjectCostingReportItem.  # noqa: E501
        :rtype: float
        """
        return self._actual_cost

    @actual_cost.setter
    def actual_cost(self, actual_cost):
        """Sets the actual_cost of this ProjectCostingReportItem.


        :param actual_cost: The actual_cost of this ProjectCostingReportItem.  # noqa: E501
        :type: float
        """

        self._actual_cost = actual_cost

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
        if not isinstance(other, ProjectCostingReportItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectCostingReportItem):
            return True

        return self.to_dict() != other.to_dict()