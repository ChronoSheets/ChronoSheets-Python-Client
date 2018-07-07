# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.aggregate_job_tasks_api import AggregateJobTasksApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestAggregateJobTasksApi(unittest.TestCase):
    """AggregateJobTasksApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.aggregate_job_tasks_api.AggregateJobTasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aggregate_job_tasks_get_aggregate_job_tasks(self):
        """Test case for aggregate_job_tasks_get_aggregate_job_tasks

        Get jobs and tasks information, aggregated.    Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
