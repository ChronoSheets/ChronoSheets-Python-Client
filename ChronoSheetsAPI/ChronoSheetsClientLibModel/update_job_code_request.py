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


class UpdateJobCodeRequest(object):
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
        'project_id': 'int',
        'client_id': 'int',
        'linked_task_ids': 'list[int]',
        'linked_org_group_ids': 'list[int]',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'code': 'Code',
        'project_id': 'ProjectId',
        'client_id': 'ClientId',
        'linked_task_ids': 'LinkedTaskIds',
        'linked_org_group_ids': 'LinkedOrgGroupIds',
        'is_deleted': 'IsDeleted'
    }

    def __init__(self, id=None, code=None, project_id=None, client_id=None, linked_task_ids=None, linked_org_group_ids=None, is_deleted=None, local_vars_configuration=None):  # noqa: E501
        """UpdateJobCodeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._code = None
        self._project_id = None
        self._client_id = None
        self._linked_task_ids = None
        self._linked_org_group_ids = None
        self._is_deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if project_id is not None:
            self.project_id = project_id
        if client_id is not None:
            self.client_id = client_id
        if linked_task_ids is not None:
            self.linked_task_ids = linked_task_ids
        if linked_org_group_ids is not None:
            self.linked_org_group_ids = linked_org_group_ids
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def id(self):
        """Gets the id of this UpdateJobCodeRequest.  # noqa: E501

        The Id of the JobCode to be updated  # noqa: E501

        :return: The id of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateJobCodeRequest.

        The Id of the JobCode to be updated  # noqa: E501

        :param id: The id of this UpdateJobCodeRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this UpdateJobCodeRequest.  # noqa: E501

        The new JobCode to be set  # noqa: E501

        :return: The code of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UpdateJobCodeRequest.

        The new JobCode to be set  # noqa: E501

        :param code: The code of this UpdateJobCodeRequest.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def project_id(self):
        """Gets the project_id of this UpdateJobCodeRequest.  # noqa: E501

        The Id of the Project to be associated to  # noqa: E501

        :return: The project_id of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateJobCodeRequest.

        The Id of the Project to be associated to  # noqa: E501

        :param project_id: The project_id of this UpdateJobCodeRequest.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def client_id(self):
        """Gets the client_id of this UpdateJobCodeRequest.  # noqa: E501

        The Id of the Client to be associated to  # noqa: E501

        :return: The client_id of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UpdateJobCodeRequest.

        The Id of the Client to be associated to  # noqa: E501

        :param client_id: The client_id of this UpdateJobCodeRequest.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def linked_task_ids(self):
        """Gets the linked_task_ids of this UpdateJobCodeRequest.  # noqa: E501

        A collection of Task Ids to be available when choosing this JobCode  # noqa: E501

        :return: The linked_task_ids of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_task_ids

    @linked_task_ids.setter
    def linked_task_ids(self, linked_task_ids):
        """Sets the linked_task_ids of this UpdateJobCodeRequest.

        A collection of Task Ids to be available when choosing this JobCode  # noqa: E501

        :param linked_task_ids: The linked_task_ids of this UpdateJobCodeRequest.  # noqa: E501
        :type: list[int]
        """

        self._linked_task_ids = linked_task_ids

    @property
    def linked_org_group_ids(self):
        """Gets the linked_org_group_ids of this UpdateJobCodeRequest.  # noqa: E501

        Restrict the access to this JobCode by specifying which Organisation Groups can have access.  Only employees in these Organisation Groups will be able to access this JobCode  # noqa: E501

        :return: The linked_org_group_ids of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_org_group_ids

    @linked_org_group_ids.setter
    def linked_org_group_ids(self, linked_org_group_ids):
        """Sets the linked_org_group_ids of this UpdateJobCodeRequest.

        Restrict the access to this JobCode by specifying which Organisation Groups can have access.  Only employees in these Organisation Groups will be able to access this JobCode  # noqa: E501

        :param linked_org_group_ids: The linked_org_group_ids of this UpdateJobCodeRequest.  # noqa: E501
        :type: list[int]
        """

        self._linked_org_group_ids = linked_org_group_ids

    @property
    def is_deleted(self):
        """Gets the is_deleted of this UpdateJobCodeRequest.  # noqa: E501

        Whether or not this JobCode is to be marked as deleted  # noqa: E501

        :return: The is_deleted of this UpdateJobCodeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this UpdateJobCodeRequest.

        Whether or not this JobCode is to be marked as deleted  # noqa: E501

        :param is_deleted: The is_deleted of this UpdateJobCodeRequest.  # noqa: E501
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
        if not isinstance(other, UpdateJobCodeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateJobCodeRequest):
            return True

        return self.to_dict() != other.to_dict()
