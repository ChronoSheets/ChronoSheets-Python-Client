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


class CreateAutomationStepRequest(object):
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
        'geofencing_id': 'int',
        'nfc_id': 'int',
        'automation_action_type': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'client_time': 'datetime'
    }

    attribute_map = {
        'geofencing_id': 'GeofencingId',
        'nfc_id': 'NfcId',
        'automation_action_type': 'AutomationActionType',
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'client_time': 'ClientTime'
    }

    def __init__(self, geofencing_id=None, nfc_id=None, automation_action_type=None, latitude=None, longitude=None, client_time=None, local_vars_configuration=None):  # noqa: E501
        """CreateAutomationStepRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geofencing_id = None
        self._nfc_id = None
        self._automation_action_type = None
        self._latitude = None
        self._longitude = None
        self._client_time = None
        self.discriminator = None

        if geofencing_id is not None:
            self.geofencing_id = geofencing_id
        if nfc_id is not None:
            self.nfc_id = nfc_id
        if automation_action_type is not None:
            self.automation_action_type = automation_action_type
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if client_time is not None:
            self.client_time = client_time

    @property
    def geofencing_id(self):
        """Gets the geofencing_id of this CreateAutomationStepRequest.  # noqa: E501


        :return: The geofencing_id of this CreateAutomationStepRequest.  # noqa: E501
        :rtype: int
        """
        return self._geofencing_id

    @geofencing_id.setter
    def geofencing_id(self, geofencing_id):
        """Sets the geofencing_id of this CreateAutomationStepRequest.


        :param geofencing_id: The geofencing_id of this CreateAutomationStepRequest.  # noqa: E501
        :type: int
        """

        self._geofencing_id = geofencing_id

    @property
    def nfc_id(self):
        """Gets the nfc_id of this CreateAutomationStepRequest.  # noqa: E501


        :return: The nfc_id of this CreateAutomationStepRequest.  # noqa: E501
        :rtype: int
        """
        return self._nfc_id

    @nfc_id.setter
    def nfc_id(self, nfc_id):
        """Sets the nfc_id of this CreateAutomationStepRequest.


        :param nfc_id: The nfc_id of this CreateAutomationStepRequest.  # noqa: E501
        :type: int
        """

        self._nfc_id = nfc_id

    @property
    def automation_action_type(self):
        """Gets the automation_action_type of this CreateAutomationStepRequest.  # noqa: E501


        :return: The automation_action_type of this CreateAutomationStepRequest.  # noqa: E501
        :rtype: str
        """
        return self._automation_action_type

    @automation_action_type.setter
    def automation_action_type(self, automation_action_type):
        """Sets the automation_action_type of this CreateAutomationStepRequest.


        :param automation_action_type: The automation_action_type of this CreateAutomationStepRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["EnterGeofence", "ExitGeofence", "TapOnNfc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and automation_action_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `automation_action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(automation_action_type, allowed_values)
            )

        self._automation_action_type = automation_action_type

    @property
    def latitude(self):
        """Gets the latitude of this CreateAutomationStepRequest.  # noqa: E501


        :return: The latitude of this CreateAutomationStepRequest.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this CreateAutomationStepRequest.


        :param latitude: The latitude of this CreateAutomationStepRequest.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this CreateAutomationStepRequest.  # noqa: E501


        :return: The longitude of this CreateAutomationStepRequest.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this CreateAutomationStepRequest.


        :param longitude: The longitude of this CreateAutomationStepRequest.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def client_time(self):
        """Gets the client_time of this CreateAutomationStepRequest.  # noqa: E501


        :return: The client_time of this CreateAutomationStepRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._client_time

    @client_time.setter
    def client_time(self, client_time):
        """Sets the client_time of this CreateAutomationStepRequest.


        :param client_time: The client_time of this CreateAutomationStepRequest.  # noqa: E501
        :type: datetime
        """

        self._client_time = client_time

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
        if not isinstance(other, CreateAutomationStepRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAutomationStepRequest):
            return True

        return self.to_dict() != other.to_dict()
