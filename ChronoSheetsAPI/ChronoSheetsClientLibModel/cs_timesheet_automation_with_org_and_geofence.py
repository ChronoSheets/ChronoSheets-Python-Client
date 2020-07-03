# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CSTimesheetAutomationWithOrgAndGeofence(object):
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
        'org_id': 'int',
        'geofence_name': 'str',
        'coordinates': 'list[CSBasicCoordinate]',
        'user_id': 'int',
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'automation_id': 'int',
        'automation_action_type': 'str',
        'created': 'datetime',
        'latitude': 'float',
        'longitude': 'float',
        'is_processed': 'bool',
        'expires': 'datetime',
        'client_date_time': 'datetime'
    }

    attribute_map = {
        'org_id': 'OrgId',
        'geofence_name': 'GeofenceName',
        'coordinates': 'Coordinates',
        'user_id': 'UserId',
        'user_name': 'UserName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'automation_id': 'AutomationId',
        'automation_action_type': 'AutomationActionType',
        'created': 'Created',
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'is_processed': 'IsProcessed',
        'expires': 'Expires',
        'client_date_time': 'ClientDateTime'
    }

    def __init__(self, org_id=None, geofence_name=None, coordinates=None, user_id=None, user_name=None, first_name=None, last_name=None, automation_id=None, automation_action_type=None, created=None, latitude=None, longitude=None, is_processed=None, expires=None, client_date_time=None):  # noqa: E501
        """CSTimesheetAutomationWithOrgAndGeofence - a model defined in Swagger"""  # noqa: E501

        self._org_id = None
        self._geofence_name = None
        self._coordinates = None
        self._user_id = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._automation_id = None
        self._automation_action_type = None
        self._created = None
        self._latitude = None
        self._longitude = None
        self._is_processed = None
        self._expires = None
        self._client_date_time = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        if geofence_name is not None:
            self.geofence_name = geofence_name
        if coordinates is not None:
            self.coordinates = coordinates
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if automation_id is not None:
            self.automation_id = automation_id
        if automation_action_type is not None:
            self.automation_action_type = automation_action_type
        if created is not None:
            self.created = created
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if is_processed is not None:
            self.is_processed = is_processed
        if expires is not None:
            self.expires = expires
        if client_date_time is not None:
            self.client_date_time = client_date_time

    @property
    def org_id(self):
        """Gets the org_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The org_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CSTimesheetAutomationWithOrgAndGeofence.


        :param org_id: The org_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def geofence_name(self):
        """Gets the geofence_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The geofence_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: str
        """
        return self._geofence_name

    @geofence_name.setter
    def geofence_name(self, geofence_name):
        """Sets the geofence_name of this CSTimesheetAutomationWithOrgAndGeofence.


        :param geofence_name: The geofence_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: str
        """

        self._geofence_name = geofence_name

    @property
    def coordinates(self):
        """Gets the coordinates of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The coordinates of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: list[CSBasicCoordinate]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this CSTimesheetAutomationWithOrgAndGeofence.


        :param coordinates: The coordinates of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: list[CSBasicCoordinate]
        """

        self._coordinates = coordinates

    @property
    def user_id(self):
        """Gets the user_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The user_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSTimesheetAutomationWithOrgAndGeofence.


        :param user_id: The user_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The user_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CSTimesheetAutomationWithOrgAndGeofence.


        :param user_name: The user_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The first_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CSTimesheetAutomationWithOrgAndGeofence.


        :param first_name: The first_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The last_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CSTimesheetAutomationWithOrgAndGeofence.


        :param last_name: The last_name of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def automation_id(self):
        """Gets the automation_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The automation_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: int
        """
        return self._automation_id

    @automation_id.setter
    def automation_id(self, automation_id):
        """Sets the automation_id of this CSTimesheetAutomationWithOrgAndGeofence.


        :param automation_id: The automation_id of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: int
        """

        self._automation_id = automation_id

    @property
    def automation_action_type(self):
        """Gets the automation_action_type of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The automation_action_type of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: str
        """
        return self._automation_action_type

    @automation_action_type.setter
    def automation_action_type(self, automation_action_type):
        """Sets the automation_action_type of this CSTimesheetAutomationWithOrgAndGeofence.


        :param automation_action_type: The automation_action_type of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: str
        """
        allowed_values = ["EnterGeofence", "ExitGeofence", "TapOnNfc"]  # noqa: E501
        if automation_action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `automation_action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(automation_action_type, allowed_values)
            )

        self._automation_action_type = automation_action_type

    @property
    def created(self):
        """Gets the created of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The created of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CSTimesheetAutomationWithOrgAndGeofence.


        :param created: The created of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def latitude(self):
        """Gets the latitude of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The latitude of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this CSTimesheetAutomationWithOrgAndGeofence.


        :param latitude: The latitude of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The longitude of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this CSTimesheetAutomationWithOrgAndGeofence.


        :param longitude: The longitude of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def is_processed(self):
        """Gets the is_processed of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The is_processed of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: bool
        """
        return self._is_processed

    @is_processed.setter
    def is_processed(self, is_processed):
        """Sets the is_processed of this CSTimesheetAutomationWithOrgAndGeofence.


        :param is_processed: The is_processed of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: bool
        """

        self._is_processed = is_processed

    @property
    def expires(self):
        """Gets the expires of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The expires of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this CSTimesheetAutomationWithOrgAndGeofence.


        :param expires: The expires of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def client_date_time(self):
        """Gets the client_date_time of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501


        :return: The client_date_time of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :rtype: datetime
        """
        return self._client_date_time

    @client_date_time.setter
    def client_date_time(self, client_date_time):
        """Sets the client_date_time of this CSTimesheetAutomationWithOrgAndGeofence.


        :param client_date_time: The client_date_time of this CSTimesheetAutomationWithOrgAndGeofence.  # noqa: E501
        :type: datetime
        """

        self._client_date_time = client_date_time

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
        if issubclass(CSTimesheetAutomationWithOrgAndGeofence, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CSTimesheetAutomationWithOrgAndGeofence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other