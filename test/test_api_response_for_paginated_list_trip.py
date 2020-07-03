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
from ChronoSheetsAPI.ChronoSheetsClientLibModel.api_response_for_paginated_list_trip import ApiResponseForPaginatedListTrip  # noqa: E501
from ChronoSheetsAPI.rest import ApiException

class TestApiResponseForPaginatedListTrip(unittest.TestCase):
    """ApiResponseForPaginatedListTrip unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseForPaginatedListTrip
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ChronoSheetsAPI.models.api_response_for_paginated_list_trip.ApiResponseForPaginatedListTrip()  # noqa: E501
        if include_optional :
            return ApiResponseForPaginatedListTrip(
                total_set_count = 56, 
                data = [
                    ChronoSheetsAPI.models.trip.Trip(
                        trip_id = 56, 
                        timesheet_id = 56, 
                        vehicle_id = 56, 
                        user_id = 56, 
                        org_id = 56, 
                        mobile_platform = 'Unknown', 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        vehicle_name = '0', 
                        vehicle_make = '0', 
                        vehicle_model = '0', 
                        vehicle_year = '0', 
                        cost_per_kilometer = 1.337, 
                        trip_total_cost = 1.337, 
                        total_trip_distance_meters = 1.337, 
                        start_address = '0', 
                        end_address = '0', 
                        path_coordinates = [
                            ChronoSheetsAPI.models.trip_coordinate.TripCoordinate(
                                latitude = 1.337, 
                                longitude = 1.337, )
                            ], 
                        cache_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                status = 'Succeeded', 
                message = '0'
            )
        else :
            return ApiResponseForPaginatedListTrip(
        )

    def testApiResponseForPaginatedListTrip(self):
        """Test ApiResponseForPaginatedListTrip"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
