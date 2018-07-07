# coding: utf-8

"""
    The ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.reports_api import ReportsApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.reports_api.ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reports_get_all_charts_data_admin(self):
        """Test case for reports_get_all_charts_data_admin

        Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.    Requires the 'ReportAdmin' permission.  # noqa: E501
        """
        pass

    def test_reports_get_all_charts_data_user(self):
        """Test case for reports_get_all_charts_data_user

        Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user's own reports.    Requires the 'ViewOwnReports' permission.  # noqa: E501
        """
        pass

    def test_reports_get_org_trip_by_id(self):
        """Test case for reports_get_org_trip_by_id

        Get trip by Id, for reporting purposes.    Requires the 'ReportAdmin' permission.  # noqa: E501
        """
        pass

    def test_reports_get_organisation_timesheet_file_attachments(self):
        """Test case for reports_get_organisation_timesheet_file_attachments

        Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records.    Requires the 'ReportAdmin' permission.  # noqa: E501
        """
        pass

    def test_reports_get_organisation_trips(self):
        """Test case for reports_get_organisation_trips

        Reports on Organisation trips (GPS tracking from whole organisation).    Requires the 'ReportAdmin' permission.  # noqa: E501
        """
        pass

    def test_reports_get_raw_data_admin(self):
        """Test case for reports_get_raw_data_admin

        Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.    Requires the 'ReportAdmin' permission.  # noqa: E501
        """
        pass

    def test_reports_project_costings_admin(self):
        """Test case for reports_project_costings_admin

        Gets project cost estimations VS actual cost for date range and users.    Requires the 'ReportAdmin' permission.  # noqa: E501
        """
        pass

    def test_reports_user_jobs_over_time(self):
        """Test case for reports_user_jobs_over_time

        Timeseries jobs data for the logged in user.    Requires the 'ViewOwnReports' or 'SubmitTimesheets'.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
