# coding: utf-8

"""
    The ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ChronoSheetsAPI.ChronoSheetsClientLibModel.cs_cs_raw_report_item import CSRawReportItem  # noqa: F401,E501


class CSApiResponseForPaginatedListRawReportItem(object):
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
        'total_set_count': 'int',
        'data': 'list[CSRawReportItem]',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'total_set_count': 'TotalSetCount',
        'data': 'Data',
        'status': 'Status',
        'message': 'Message'
    }

    def __init__(self, total_set_count=None, data=None, status=None, message=None):  # noqa: E501
        """CSApiResponseForPaginatedListRawReportItem - a model defined in Swagger"""  # noqa: E501

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
        """Gets the total_set_count of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501


        :return: The total_set_count of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :rtype: int
        """
        return self._total_set_count

    @total_set_count.setter
    def total_set_count(self, total_set_count):
        """Sets the total_set_count of this CSApiResponseForPaginatedListRawReportItem.


        :param total_set_count: The total_set_count of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :type: int
        """

        self._total_set_count = total_set_count

    @property
    def data(self):
        """Gets the data of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501


        :return: The data of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :rtype: list[CSRawReportItem]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CSApiResponseForPaginatedListRawReportItem.


        :param data: The data of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :type: list[CSRawReportItem]
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501


        :return: The status of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CSApiResponseForPaginatedListRawReportItem.


        :param status: The status of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Succeeded", "FatalException", "GeneralError", "ValidationError", "UnAuthorized", "SessionExpired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501


        :return: The message of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CSApiResponseForPaginatedListRawReportItem.


        :param message: The message of this CSApiResponseForPaginatedListRawReportItem.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, CSApiResponseForPaginatedListRawReportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
