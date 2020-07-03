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


class ApiResponseForPaginatedListTrip(object):
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
        'total_set_count': 'int',
        'data': 'list[Trip]',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'total_set_count': 'TotalSetCount',
        'data': 'Data',
        'status': 'Status',
        'message': 'Message'
    }

    def __init__(self, total_set_count=None, data=None, status=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ApiResponseForPaginatedListTrip - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_set_count = None
        self._data = None
        self._status = None
        self._message = None
        self.discriminator = None

        if total_set_count is not None:
            self.total_set_count = total_set_count
        if data is not None:
            self.data = data
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def total_set_count(self):
        """Gets the total_set_count of this ApiResponseForPaginatedListTrip.  # noqa: E501

        The count of total records that are being paginated  # noqa: E501

        :return: The total_set_count of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :rtype: int
        """
        return self._total_set_count

    @total_set_count.setter
    def total_set_count(self, total_set_count):
        """Sets the total_set_count of this ApiResponseForPaginatedListTrip.

        The count of total records that are being paginated  # noqa: E501

        :param total_set_count: The total_set_count of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :type: int
        """

        self._total_set_count = total_set_count

    @property
    def data(self):
        """Gets the data of this ApiResponseForPaginatedListTrip.  # noqa: E501

        The main Data of the response  # noqa: E501

        :return: The data of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :rtype: list[Trip]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiResponseForPaginatedListTrip.

        The main Data of the response  # noqa: E501

        :param data: The data of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :type: list[Trip]
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this ApiResponseForPaginatedListTrip.  # noqa: E501

        The API response status. Indicates if the request was successful, failed or was unauthorised.  # noqa: E501

        :return: The status of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiResponseForPaginatedListTrip.

        The API response status. Indicates if the request was successful, failed or was unauthorised.  # noqa: E501

        :param status: The status of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :type: str
        """
        allowed_values = ["Succeeded", "FatalException", "GeneralError", "ValidationError", "UnAuthorized", "SessionExpired"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this ApiResponseForPaginatedListTrip.  # noqa: E501

        A message to accompany the response status.  If the Status is failed, this message will hint why it failed and what you need to do.  # noqa: E501

        :return: The message of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiResponseForPaginatedListTrip.

        A message to accompany the response status.  If the Status is failed, this message will hint why it failed and what you need to do.  # noqa: E501

        :param message: The message of this ApiResponseForPaginatedListTrip.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ApiResponseForPaginatedListTrip):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiResponseForPaginatedListTrip):
            return True

        return self.to_dict() != other.to_dict()
