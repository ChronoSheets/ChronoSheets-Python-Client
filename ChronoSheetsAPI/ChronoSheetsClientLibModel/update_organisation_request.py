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


class UpdateOrganisationRequest(object):
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
        'organsation_id': 'int',
        'organisation_name': 'str',
        'address_line01': 'str',
        'address_line02': 'str',
        'organisation_suburb': 'str',
        'organisation_state': 'str',
        'organisation_postcode': 'str',
        'organisation_country': 'str',
        'organisation_phone': 'str',
        'organisation_email_address': 'str'
    }

    attribute_map = {
        'organsation_id': 'OrgansationId',
        'organisation_name': 'OrganisationName',
        'address_line01': 'AddressLine01',
        'address_line02': 'AddressLine02',
        'organisation_suburb': 'OrganisationSuburb',
        'organisation_state': 'OrganisationState',
        'organisation_postcode': 'OrganisationPostcode',
        'organisation_country': 'OrganisationCountry',
        'organisation_phone': 'OrganisationPhone',
        'organisation_email_address': 'OrganisationEmailAddress'
    }

    def __init__(self, organsation_id=None, organisation_name=None, address_line01=None, address_line02=None, organisation_suburb=None, organisation_state=None, organisation_postcode=None, organisation_country=None, organisation_phone=None, organisation_email_address=None, local_vars_configuration=None):  # noqa: E501
        """UpdateOrganisationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._organsation_id = None
        self._organisation_name = None
        self._address_line01 = None
        self._address_line02 = None
        self._organisation_suburb = None
        self._organisation_state = None
        self._organisation_postcode = None
        self._organisation_country = None
        self._organisation_phone = None
        self._organisation_email_address = None
        self.discriminator = None

        if organsation_id is not None:
            self.organsation_id = organsation_id
        if organisation_name is not None:
            self.organisation_name = organisation_name
        if address_line01 is not None:
            self.address_line01 = address_line01
        if address_line02 is not None:
            self.address_line02 = address_line02
        if organisation_suburb is not None:
            self.organisation_suburb = organisation_suburb
        if organisation_state is not None:
            self.organisation_state = organisation_state
        if organisation_postcode is not None:
            self.organisation_postcode = organisation_postcode
        if organisation_country is not None:
            self.organisation_country = organisation_country
        if organisation_phone is not None:
            self.organisation_phone = organisation_phone
        if organisation_email_address is not None:
            self.organisation_email_address = organisation_email_address

    @property
    def organsation_id(self):
        """Gets the organsation_id of this UpdateOrganisationRequest.  # noqa: E501

        The Id of your Organisation.  This is validated based on your current Auth Token  # noqa: E501

        :return: The organsation_id of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: int
        """
        return self._organsation_id

    @organsation_id.setter
    def organsation_id(self, organsation_id):
        """Sets the organsation_id of this UpdateOrganisationRequest.

        The Id of your Organisation.  This is validated based on your current Auth Token  # noqa: E501

        :param organsation_id: The organsation_id of this UpdateOrganisationRequest.  # noqa: E501
        :type: int
        """

        self._organsation_id = organsation_id

    @property
    def organisation_name(self):
        """Gets the organisation_name of this UpdateOrganisationRequest.  # noqa: E501

        The updated organisation name  # noqa: E501

        :return: The organisation_name of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this UpdateOrganisationRequest.

        The updated organisation name  # noqa: E501

        :param organisation_name: The organisation_name of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_name = organisation_name

    @property
    def address_line01(self):
        """Gets the address_line01 of this UpdateOrganisationRequest.  # noqa: E501

        The updated Address Line 1 value  # noqa: E501

        :return: The address_line01 of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_line01

    @address_line01.setter
    def address_line01(self, address_line01):
        """Sets the address_line01 of this UpdateOrganisationRequest.

        The updated Address Line 1 value  # noqa: E501

        :param address_line01: The address_line01 of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._address_line01 = address_line01

    @property
    def address_line02(self):
        """Gets the address_line02 of this UpdateOrganisationRequest.  # noqa: E501

        The updated Address Line 2 value  # noqa: E501

        :return: The address_line02 of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_line02

    @address_line02.setter
    def address_line02(self, address_line02):
        """Sets the address_line02 of this UpdateOrganisationRequest.

        The updated Address Line 2 value  # noqa: E501

        :param address_line02: The address_line02 of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._address_line02 = address_line02

    @property
    def organisation_suburb(self):
        """Gets the organisation_suburb of this UpdateOrganisationRequest.  # noqa: E501

        The updated address suburb  # noqa: E501

        :return: The organisation_suburb of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_suburb

    @organisation_suburb.setter
    def organisation_suburb(self, organisation_suburb):
        """Sets the organisation_suburb of this UpdateOrganisationRequest.

        The updated address suburb  # noqa: E501

        :param organisation_suburb: The organisation_suburb of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_suburb = organisation_suburb

    @property
    def organisation_state(self):
        """Gets the organisation_state of this UpdateOrganisationRequest.  # noqa: E501

        The updated address state  # noqa: E501

        :return: The organisation_state of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_state

    @organisation_state.setter
    def organisation_state(self, organisation_state):
        """Sets the organisation_state of this UpdateOrganisationRequest.

        The updated address state  # noqa: E501

        :param organisation_state: The organisation_state of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_state = organisation_state

    @property
    def organisation_postcode(self):
        """Gets the organisation_postcode of this UpdateOrganisationRequest.  # noqa: E501

        The updated address postcode  # noqa: E501

        :return: The organisation_postcode of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_postcode

    @organisation_postcode.setter
    def organisation_postcode(self, organisation_postcode):
        """Sets the organisation_postcode of this UpdateOrganisationRequest.

        The updated address postcode  # noqa: E501

        :param organisation_postcode: The organisation_postcode of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_postcode = organisation_postcode

    @property
    def organisation_country(self):
        """Gets the organisation_country of this UpdateOrganisationRequest.  # noqa: E501

        The updated address country  # noqa: E501

        :return: The organisation_country of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_country

    @organisation_country.setter
    def organisation_country(self, organisation_country):
        """Sets the organisation_country of this UpdateOrganisationRequest.

        The updated address country  # noqa: E501

        :param organisation_country: The organisation_country of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_country = organisation_country

    @property
    def organisation_phone(self):
        """Gets the organisation_phone of this UpdateOrganisationRequest.  # noqa: E501

        The updated contact phone number  # noqa: E501

        :return: The organisation_phone of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_phone

    @organisation_phone.setter
    def organisation_phone(self, organisation_phone):
        """Sets the organisation_phone of this UpdateOrganisationRequest.

        The updated contact phone number  # noqa: E501

        :param organisation_phone: The organisation_phone of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_phone = organisation_phone

    @property
    def organisation_email_address(self):
        """Gets the organisation_email_address of this UpdateOrganisationRequest.  # noqa: E501

        The update organisation email address  # noqa: E501

        :return: The organisation_email_address of this UpdateOrganisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_email_address

    @organisation_email_address.setter
    def organisation_email_address(self, organisation_email_address):
        """Sets the organisation_email_address of this UpdateOrganisationRequest.

        The update organisation email address  # noqa: E501

        :param organisation_email_address: The organisation_email_address of this UpdateOrganisationRequest.  # noqa: E501
        :type: str
        """

        self._organisation_email_address = organisation_email_address

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
        if not isinstance(other, UpdateOrganisationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateOrganisationRequest):
            return True

        return self.to_dict() != other.to_dict()
