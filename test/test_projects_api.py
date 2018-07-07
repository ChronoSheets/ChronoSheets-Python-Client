# coding: utf-8

"""
    The ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  </p>  <p>      First Steps:       <ol>          <li>Make sure you've <a href='/HomeV2/App/sign-up'>signed up to ChronoSheets</a> to get yourself a user account</li>          <li>Confirm your account by following the link sent to your email address.  This will activate your account</li>          <li>Use your username and password to obtain an Auth Token by using the DoLogin method inside the UserProfile section below.  Use the Auth Token as an argument to the other methods</li>          <li>Try different methods in the API Playground to learn about the API</li>          <li>If you're stuck, try the full getting started guide on the <a href='/Home/ApiDocs'>API Toolkit</a> page.</li>      </ol>  </p>  <p>      Further Steps:       <ul>          <li>Create a mobile app (iOS, Android or Windows) using one of the ChronoSheets Mobile SDKs</li>          <li>Create a custom integration with your app using one of the ChronoSheets API Client Libraries.</li>      </ul>      Read more about the API Toolkit on the <a href='/Home/ApiDocs'>API Toolkit</a> page.  </p></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.projects_api import ProjectsApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_create_project(self):
        """Test case for projects_create_project

        Create a project.    Requires the 'ManageClientsAndProjects' permission.  # noqa: E501
        """
        pass

    def test_projects_get_project_by_id(self):
        """Test case for projects_get_project_by_id

        Get a project by its Id.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.  # noqa: E501
        """
        pass

    def test_projects_get_projects_for_client(self):
        """Test case for projects_get_projects_for_client

        Get projects for a particular client.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.  # noqa: E501
        """
        pass

    def test_projects_update_project(self):
        """Test case for projects_update_project

        Update a project.    Requires the 'ManageClientsAndProjects' permission.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
