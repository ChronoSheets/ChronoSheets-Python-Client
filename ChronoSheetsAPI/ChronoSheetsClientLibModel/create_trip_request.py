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


class CreateTripRequest(object):
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
        'timesheet_id': 'int',
        'vehicle_id': 'int',
        'path_coords_string_csv': 'str',
        'distance_meters': 'float',
        'mobile_platform': 'str'
    }

    attribute_map = {
        'timesheet_id': 'TimesheetId',
        'vehicle_id': 'VehicleId',
        'path_coords_string_csv': 'PathCoordsStringCsv',
        'distance_meters': 'DistanceMeters',
        'mobile_platform': 'MobilePlatform'
    }

    def __init__(self, timesheet_id=None, vehicle_id=None, path_coords_string_csv=None, distance_meters=None, mobile_platform=None, local_vars_configuration=None):  # noqa: E501
        """CreateTripRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timesheet_id = None
        self._vehicle_id = None
        self._path_coords_string_csv = None
        self._distance_meters = None
        self._mobile_platform = None
        self.discriminator = None

        if timesheet_id is not None:
            self.timesheet_id = timesheet_id
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id
        if path_coords_string_csv is not None:
            self.path_coords_string_csv = path_coords_string_csv
        if distance_meters is not None:
            self.distance_meters = distance_meters
        if mobile_platform is not None:
            self.mobile_platform = mobile_platform

    @property
    def timesheet_id(self):
        """Gets the timesheet_id of this CreateTripRequest.  # noqa: E501

        The associated Timesheet record Id.  The Trip will be linked to the Timesheet with this TimesheetId  # noqa: E501

        :return: The timesheet_id of this CreateTripRequest.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_id

    @timesheet_id.setter
    def timesheet_id(self, timesheet_id):
        """Sets the timesheet_id of this CreateTripRequest.

        The associated Timesheet record Id.  The Trip will be linked to the Timesheet with this TimesheetId  # noqa: E501

        :param timesheet_id: The timesheet_id of this CreateTripRequest.  # noqa: E501
        :type: int
        """

        self._timesheet_id = timesheet_id

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this CreateTripRequest.  # noqa: E501

        The associated Vehicle Id.  The Trip will show that this Vehicle was used  # noqa: E501

        :return: The vehicle_id of this CreateTripRequest.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this CreateTripRequest.

        The associated Vehicle Id.  The Trip will show that this Vehicle was used  # noqa: E501

        :param vehicle_id: The vehicle_id of this CreateTripRequest.  # noqa: E501
        :type: int
        """

        self._vehicle_id = vehicle_id

    @property
    def path_coords_string_csv(self):
        """Gets the path_coords_string_csv of this CreateTripRequest.  # noqa: E501

        A CSV of GPS path co-ordinates.  Format example: -37.8433562,144.7226188;[Lat1],[Long1];........[LatN],[LongN]  # noqa: E501

        :return: The path_coords_string_csv of this CreateTripRequest.  # noqa: E501
        :rtype: str
        """
        return self._path_coords_string_csv

    @path_coords_string_csv.setter
    def path_coords_string_csv(self, path_coords_string_csv):
        """Sets the path_coords_string_csv of this CreateTripRequest.

        A CSV of GPS path co-ordinates.  Format example: -37.8433562,144.7226188;[Lat1],[Long1];........[LatN],[LongN]  # noqa: E501

        :param path_coords_string_csv: The path_coords_string_csv of this CreateTripRequest.  # noqa: E501
        :type: str
        """

        self._path_coords_string_csv = path_coords_string_csv

    @property
    def distance_meters(self):
        """Gets the distance_meters of this CreateTripRequest.  # noqa: E501

        The total distance of the Trip  # noqa: E501

        :return: The distance_meters of this CreateTripRequest.  # noqa: E501
        :rtype: float
        """
        return self._distance_meters

    @distance_meters.setter
    def distance_meters(self, distance_meters):
        """Sets the distance_meters of this CreateTripRequest.

        The total distance of the Trip  # noqa: E501

        :param distance_meters: The distance_meters of this CreateTripRequest.  # noqa: E501
        :type: float
        """

        self._distance_meters = distance_meters

    @property
    def mobile_platform(self):
        """Gets the mobile_platform of this CreateTripRequest.  # noqa: E501

        The Mobile platform that the Trip was recorded on  # noqa: E501

        :return: The mobile_platform of this CreateTripRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_platform

    @mobile_platform.setter
    def mobile_platform(self, mobile_platform):
        """Sets the mobile_platform of this CreateTripRequest.

        The Mobile platform that the Trip was recorded on  # noqa: E501

        :param mobile_platform: The mobile_platform of this CreateTripRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "iOS", "Android"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mobile_platform not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mobile_platform` ({0}), must be one of {1}"  # noqa: E501
                .format(mobile_platform, allowed_values)
            )

        self._mobile_platform = mobile_platform

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
        if not isinstance(other, CreateTripRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTripRequest):
            return True

        return self.to_dict() != other.to_dict()