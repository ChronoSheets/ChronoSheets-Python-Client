# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ChronoSheetsAPI
from ChronoSheetsAPI.ChronoSheetsClientLibModel.update_organisation_request import UpdateOrganisationRequest  # noqa: E501
from ChronoSheetsAPI.rest import ApiException

class TestUpdateOrganisationRequest(unittest.TestCase):
    """UpdateOrganisationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateOrganisationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ChronoSheetsAPI.models.update_organisation_request.UpdateOrganisationRequest()  # noqa: E501
        if include_optional :
            return UpdateOrganisationRequest(
                organsation_id = 56, 
                organisation_name = '0', 
                address_line01 = '0', 
                address_line02 = '0', 
                organisation_suburb = '0', 
                organisation_state = '0', 
                organisation_postcode = '0', 
                organisation_country = '0', 
                organisation_phone = '0', 
                organisation_email_address = '0'
            )
        else :
            return UpdateOrganisationRequest(
        )

    def testUpdateOrganisationRequest(self):
        """Test UpdateOrganisationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
