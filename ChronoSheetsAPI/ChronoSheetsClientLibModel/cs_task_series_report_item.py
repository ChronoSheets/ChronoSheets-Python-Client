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


class CSTaskSeriesReportItem(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'task_id': 'int',
        'task_name': 'str',
        'span_seconds': 'int'
    }

    attribute_map = {
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'task_id': 'TaskId',
        'task_name': 'TaskName',
        'span_seconds': 'SpanSeconds'
    }

    def __init__(self, start_date=None, end_date=None, task_id=None, task_name=None, span_seconds=None):  # noqa: E501
        """CSTaskSeriesReportItem - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._task_id = None
        self._task_name = None
        self._span_seconds = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if span_seconds is not None:
            self.span_seconds = span_seconds

    @property
    def start_date(self):
        """Gets the start_date of this CSTaskSeriesReportItem.  # noqa: E501


        :return: The start_date of this CSTaskSeriesReportItem.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CSTaskSeriesReportItem.


        :param start_date: The start_date of this CSTaskSeriesReportItem.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CSTaskSeriesReportItem.  # noqa: E501


        :return: The end_date of this CSTaskSeriesReportItem.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CSTaskSeriesReportItem.


        :param end_date: The end_date of this CSTaskSeriesReportItem.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def task_id(self):
        """Gets the task_id of this CSTaskSeriesReportItem.  # noqa: E501


        :return: The task_id of this CSTaskSeriesReportItem.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CSTaskSeriesReportItem.


        :param task_id: The task_id of this CSTaskSeriesReportItem.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this CSTaskSeriesReportItem.  # noqa: E501


        :return: The task_name of this CSTaskSeriesReportItem.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CSTaskSeriesReportItem.


        :param task_name: The task_name of this CSTaskSeriesReportItem.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def span_seconds(self):
        """Gets the span_seconds of this CSTaskSeriesReportItem.  # noqa: E501


        :return: The span_seconds of this CSTaskSeriesReportItem.  # noqa: E501
        :rtype: int
        """
        return self._span_seconds

    @span_seconds.setter
    def span_seconds(self, span_seconds):
        """Sets the span_seconds of this CSTaskSeriesReportItem.


        :param span_seconds: The span_seconds of this CSTaskSeriesReportItem.  # noqa: E501
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
        if not isinstance(other, CSTaskSeriesReportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
