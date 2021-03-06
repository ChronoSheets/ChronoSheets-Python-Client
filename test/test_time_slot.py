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
from ChronoSheetsAPI.ChronoSheetsClientLibModel.time_slot import TimeSlot  # noqa: E501
from ChronoSheetsAPI.rest import ApiException

class TestTimeSlot(unittest.TestCase):
    """TimeSlot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TimeSlot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ChronoSheetsAPI.models.time_slot.TimeSlot()  # noqa: E501
        if include_optional :
            return TimeSlot(
                day_type = 'Monday', 
                usual_hour_id = 56, 
                start_hour = 56, 
                start_minute = 56, 
                end_hour = 56, 
                end_minute = 56, 
                is_valid = True
            )
        else :
            return TimeSlot(
        )

    def testTimeSlot(self):
        """Test TimeSlot"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
