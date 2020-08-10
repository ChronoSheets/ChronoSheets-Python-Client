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


class BasicGeofence(object):
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
        'geo_fencing_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'geo_fencing_id': 'GeoFencingId',
        'name': 'Name'
    }

    def __init__(self, geo_fencing_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """BasicGeofence - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geo_fencing_id = None
        self._name = None
        self.discriminator = None

        if geo_fencing_id is not None:
            self.geo_fencing_id = geo_fencing_id
        if name is not None:
            self.name = name

    @property
    def geo_fencing_id(self):
        """Gets the geo_fencing_id of this BasicGeofence.  # noqa: E501


        :return: The geo_fencing_id of this BasicGeofence.  # noqa: E501
        :rtype: int
        """
        return self._geo_fencing_id

    @geo_fencing_id.setter
    def geo_fencing_id(self, geo_fencing_id):
        """Sets the geo_fencing_id of this BasicGeofence.


        :param geo_fencing_id: The geo_fencing_id of this BasicGeofence.  # noqa: E501
        :type: int
        """

        self._geo_fencing_id = geo_fencing_id

    @property
    def name(self):
        """Gets the name of this BasicGeofence.  # noqa: E501


        :return: The name of this BasicGeofence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicGeofence.


        :param name: The name of this BasicGeofence.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, BasicGeofence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicGeofence):
            return True

        return self.to_dict() != other.to_dict()