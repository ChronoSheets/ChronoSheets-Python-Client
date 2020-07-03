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
from ChronoSheetsAPI.ChronoSheetsClientLibModel.organisation import Organisation  # noqa: E501
from ChronoSheetsAPI.rest import ApiException

class TestOrganisation(unittest.TestCase):
    """Organisation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Organisation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ChronoSheetsAPI.models.organisation.Organisation()  # noqa: E501
        if include_optional :
            return Organisation(
                id = 56, 
                name = '0', 
                address_line01 = '0', 
                address_line02 = '0', 
                suburb = '0', 
                state = '0', 
                postcode = '0', 
                country = '0', 
                phone = '0', 
                email_address = '0', 
                timezone = '0', 
                subscription_customer_id = '0', 
                signup_token = '0', 
                is_active = True, 
                stripe_coupon_code = '0', 
                subscription_source = 'None', 
                sign_up_source = 'Desktop', 
                mobile_sign_up_code = '0', 
                subscription_cycle_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                subscription_cycle_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pricing_plans = [
                    ChronoSheetsAPI.models.organisation_pricing_plan.OrganisationPricingPlan(
                        plan_id = '0', 
                        quantity = 56, )
                    ]
            )
        else :
            return Organisation(
        )

    def testOrganisation(self):
        """Test Organisation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
