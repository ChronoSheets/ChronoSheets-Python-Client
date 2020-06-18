# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.timesheet_automation_api import TimesheetAutomationApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestTimesheetAutomationApi(unittest.TestCase):
    """TimesheetAutomationApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.timesheet_automation_api.TimesheetAutomationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_timesheet_automation_create_automation_step(self):
        """Test case for timesheet_automation_create_automation_step

        Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the 'SubmitTimesheets' permission.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
