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


class JobCode(object):
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
        'id': 'int',
        'code': 'str',
        'client': 'str',
        'client_id': 'int',
        'project': 'str',
        'project_id': 'int',
        'organisation_id': 'int',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'code': 'Code',
        'client': 'Client',
        'client_id': 'ClientId',
        'project': 'Project',
        'project_id': 'ProjectId',
        'organisation_id': 'OrganisationId',
        'is_deleted': 'IsDeleted'
    }

    def __init__(self, id=None, code=None, client=None, client_id=None, project=None, project_id=None, organisation_id=None, is_deleted=None, local_vars_configuration=None):  # noqa: E501
        """JobCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._code = None
        self._client = None
        self._client_id = None
        self._project = None
        self._project_id = None
        self._organisation_id = None
        self._is_deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if client is not None:
            self.client = client
        if client_id is not None:
            self.client_id = client_id
        if project is not None:
            self.project = project
        if project_id is not None:
            self.project_id = project_id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def id(self):
        """Gets the id of this JobCode.  # noqa: E501

        The ID of the job code (not the code itself)  # noqa: E501

        :return: The id of this JobCode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobCode.

        The ID of the job code (not the code itself)  # noqa: E501

        :param id: The id of this JobCode.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this JobCode.  # noqa: E501

        The job code itself  # noqa: E501

        :return: The code of this JobCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this JobCode.

        The job code itself  # noqa: E501

        :param code: The code of this JobCode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def client(self):
        """Gets the client of this JobCode.  # noqa: E501

        The name of the client  # noqa: E501

        :return: The client of this JobCode.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this JobCode.

        The name of the client  # noqa: E501

        :param client: The client of this JobCode.  # noqa: E501
        :type: str
        """

        self._client = client

    @property
    def client_id(self):
        """Gets the client_id of this JobCode.  # noqa: E501

        The ID of the client  # noqa: E501

        :return: The client_id of this JobCode.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this JobCode.

        The ID of the client  # noqa: E501

        :param client_id: The client_id of this JobCode.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def project(self):
        """Gets the project of this JobCode.  # noqa: E501

        The name of the project  # noqa: E501

        :return: The project of this JobCode.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this JobCode.

        The name of the project  # noqa: E501

        :param project: The project of this JobCode.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def project_id(self):
        """Gets the project_id of this JobCode.  # noqa: E501

        The ID of the project  # noqa: E501

        :return: The project_id of this JobCode.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this JobCode.

        The ID of the project  # noqa: E501

        :param project_id: The project_id of this JobCode.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this JobCode.  # noqa: E501

        Your organisation ID  # noqa: E501

        :return: The organisation_id of this JobCode.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this JobCode.

        Your organisation ID  # noqa: E501

        :param organisation_id: The organisation_id of this JobCode.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this JobCode.  # noqa: E501

        A flag indicating whether or not the job code has been marked as deleted  # noqa: E501

        :return: The is_deleted of this JobCode.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this JobCode.

        A flag indicating whether or not the job code has been marked as deleted  # noqa: E501

        :param is_deleted: The is_deleted of this JobCode.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

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
        if not isinstance(other, JobCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobCode):
            return True

        return self.to_dict() != other.to_dict()