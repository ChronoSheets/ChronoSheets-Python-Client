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
from ChronoSheetsClientLibApi.user_job_favourites_api import UserJobFavouritesApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestUserJobFavouritesApi(unittest.TestCase):
    """UserJobFavouritesApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.user_job_favourites_api.UserJobFavouritesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_job_favourites_create_job_favourite(self):
        """Test case for user_job_favourites_create_job_favourite

        Create a job favourite.    Requires the 'SubmitTimesheets' permission.  # noqa: E501
        """
        pass

    def test_user_job_favourites_delete_job_favourite(self):
        """Test case for user_job_favourites_delete_job_favourite

        Delete a job favourite.    Requires the 'SubmitTimesheets' permission.  # noqa: E501
        """
        pass

    def test_user_job_favourites_get_job_favourites(self):
        """Test case for user_job_favourites_get_job_favourites

        Get your job favourites.    Requires the 'SubmitTimesheets' permission.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
