# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ChronoSheetsAPI.api_client import ApiClient


class FleetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fleet_create_vehicle(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create a vehicle.    Requires the &#39;ManageFleet&#39; permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_create_vehicle(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertVehicleRequest request: An Insert Vehicle Request object containing values for the new Vehicle to create (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInt32
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.fleet_create_vehicle_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.fleet_create_vehicle_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def fleet_create_vehicle_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create a vehicle.    Requires the &#39;ManageFleet&#39; permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_create_vehicle_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertVehicleRequest request: An Insert Vehicle Request object containing values for the new Vehicle to create (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInt32
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fleet_create_vehicle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `fleet_create_vehicle`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `fleet_create_vehicle`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Fleet/CreateVehicle', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseInt32',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fleet_get_vehicle_by_id(self, vehicle_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular vehicle.  Does not require any special permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vehicle_id: The ID of the Vehicle you want to get (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseFleetVehicle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.fleet_get_vehicle_by_id_with_http_info(vehicle_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.fleet_get_vehicle_by_id_with_http_info(vehicle_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def fleet_get_vehicle_by_id_with_http_info(self, vehicle_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular vehicle.  Does not require any special permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_get_vehicle_by_id_with_http_info(vehicle_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vehicle_id: The ID of the Vehicle you want to get (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseFleetVehicle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vehicle_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fleet_get_vehicle_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vehicle_id' is set
        if ('vehicle_id' not in params or
                params['vehicle_id'] is None):
            raise ValueError("Missing the required parameter `vehicle_id` when calling `fleet_get_vehicle_by_id`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `fleet_get_vehicle_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vehicle_id' in params:
            query_params.append(('VehicleId', params['vehicle_id']))  # noqa: E501

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Fleet/GetVehicleById', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseFleetVehicle',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fleet_get_vehicles(self, include_deleted, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a collection of vehicles that are under your organisation.    Does not require any special permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_get_vehicles(include_deleted, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param bool include_deleted: Whether or not to include deleted vehicles (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListFleetVehicle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.fleet_get_vehicles_with_http_info(include_deleted, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.fleet_get_vehicles_with_http_info(include_deleted, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def fleet_get_vehicles_with_http_info(self, include_deleted, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a collection of vehicles that are under your organisation.    Does not require any special permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_get_vehicles_with_http_info(include_deleted, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param bool include_deleted: Whether or not to include deleted vehicles (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListFleetVehicle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_deleted', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fleet_get_vehicles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'include_deleted' is set
        if ('include_deleted' not in params or
                params['include_deleted'] is None):
            raise ValueError("Missing the required parameter `include_deleted` when calling `fleet_get_vehicles`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `fleet_get_vehicles`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_deleted' in params:
            query_params.append(('IncludeDeleted', params['include_deleted']))  # noqa: E501

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Fleet/GetVehicles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListFleetVehicle',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fleet_update_vehicle(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update a vehicle.    Requires the &#39;ManageFleet&#39; permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_update_vehicle(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSSaveVehicleRequest request: A Save Vehicle Request object containing updated fields.  Make sure to specify the Vehicle Id in the request object so that ChronoSheets knows which Vehicle to update (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.fleet_update_vehicle_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.fleet_update_vehicle_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def fleet_update_vehicle_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update a vehicle.    Requires the &#39;ManageFleet&#39; permission.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.fleet_update_vehicle_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSSaveVehicleRequest request: A Save Vehicle Request object containing updated fields.  Make sure to specify the Vehicle Id in the request object so that ChronoSheets knows which Vehicle to update (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fleet_update_vehicle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `fleet_update_vehicle`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `fleet_update_vehicle`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Fleet/UpdateVehicle', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
