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
from ChronoSheetsAPI.ChronoSheetsClientLibModel.api_response_list_organisation_group import ApiResponseListOrganisationGroup  # noqa: E501
from ChronoSheetsAPI.rest import ApiException

class TestApiResponseListOrganisationGroup(unittest.TestCase):
    """ApiResponseListOrganisationGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseListOrganisationGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ChronoSheetsAPI.models.api_response_list_organisation_group.ApiResponseListOrganisationGroup()  # noqa: E501
        if include_optional :
            return ApiResponseListOrganisationGroup(
                data = [
                    ChronoSheetsAPI.models.organisation_group.OrganisationGroup(
                        id = 56, 
                        organisation_id = 56, 
                        organisation_group_name = '0', 
                        is_deleted = True, )
                    ], 
                status = 'Succeeded', 
                message = '0'
            )
        else :
            return ApiResponseListOrganisationGroup(
        )

    def testApiResponseListOrganisationGroup(self):
        """Test ApiResponseListOrganisationGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
