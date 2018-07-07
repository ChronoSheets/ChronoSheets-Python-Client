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


class CSInsertProjectRequest(object):
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
        'client_id': 'int',
        'project_name': 'str',
        'cost_estimation': 'float',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'project_name': 'ProjectName',
        'cost_estimation': 'CostEstimation',
        'start_date': 'StartDate',
        'end_date': 'EndDate'
    }

    def __init__(self, client_id=None, project_name=None, cost_estimation=None, start_date=None, end_date=None):  # noqa: E501
        """CSInsertProjectRequest - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._project_name = None
        self._cost_estimation = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if project_name is not None:
            self.project_name = project_name
        if cost_estimation is not None:
            self.cost_estimation = cost_estimation
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def client_id(self):
        """Gets the client_id of this CSInsertProjectRequest.  # noqa: E501

        The Id of the Client that is associated with the new project  # noqa: E501

        :return: The client_id of this CSInsertProjectRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this CSInsertProjectRequest.

        The Id of the Client that is associated with the new project  # noqa: E501

        :param client_id: The client_id of this CSInsertProjectRequest.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def project_name(self):
        """Gets the project_name of this CSInsertProjectRequest.  # noqa: E501

        The name of the new Project  # noqa: E501

        :return: The project_name of this CSInsertProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CSInsertProjectRequest.

        The name of the new Project  # noqa: E501

        :param project_name: The project_name of this CSInsertProjectRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def cost_estimation(self):
        """Gets the cost_estimation of this CSInsertProjectRequest.  # noqa: E501

        The estimated cost of work to complete the project.  This value is used in the Organisation Reports view 'Project Costs'  # noqa: E501

        :return: The cost_estimation of this CSInsertProjectRequest.  # noqa: E501
        :rtype: float
        """
        return self._cost_estimation

    @cost_estimation.setter
    def cost_estimation(self, cost_estimation):
        """Sets the cost_estimation of this CSInsertProjectRequest.

        The estimated cost of work to complete the project.  This value is used in the Organisation Reports view 'Project Costs'  # noqa: E501

        :param cost_estimation: The cost_estimation of this CSInsertProjectRequest.  # noqa: E501
        :type: float
        """

        self._cost_estimation = cost_estimation

    @property
    def start_date(self):
        """Gets the start_date of this CSInsertProjectRequest.  # noqa: E501

        The start date of the project.  When the project is due to start  # noqa: E501

        :return: The start_date of this CSInsertProjectRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CSInsertProjectRequest.

        The start date of the project.  When the project is due to start  # noqa: E501

        :param start_date: The start_date of this CSInsertProjectRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CSInsertProjectRequest.  # noqa: E501

        The end date of the project.  When the project is due to end  # noqa: E501

        :return: The end_date of this CSInsertProjectRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CSInsertProjectRequest.

        The end date of the project.  When the project is due to end  # noqa: E501

        :param end_date: The end_date of this CSInsertProjectRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, CSInsertProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
