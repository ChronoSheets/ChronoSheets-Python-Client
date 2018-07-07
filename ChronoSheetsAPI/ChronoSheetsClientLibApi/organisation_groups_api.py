# coding: utf-8

"""
    The ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ChronoSheetsAPI.api_client import ApiClient


class OrganisationGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def organisation_groups_create_organisation_group(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_create_organisation_group(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertOrganisationGroupRequest request: An Insert OrganisationGroup Request object containing values for the new OrganisationGroup to create (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInt32
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.organisation_groups_create_organisation_group_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.organisation_groups_create_organisation_group_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def organisation_groups_create_organisation_group_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_create_organisation_group_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertOrganisationGroupRequest request: An Insert OrganisationGroup Request object containing values for the new OrganisationGroup to create (required)
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
                    " to method organisation_groups_create_organisation_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `organisation_groups_create_organisation_group`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `organisation_groups_create_organisation_group`")  # noqa: E501

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
            '/api/OrganisationGroups/CreateOrganisationGroup', 'PUT',
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

    def organisation_groups_get_organisation_group(self, organisation_group_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular organisation group.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_group(organisation_group_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int organisation_group_id: The ID of the OrganisationGroup you want to get (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.organisation_groups_get_organisation_group_with_http_info(organisation_group_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.organisation_groups_get_organisation_group_with_http_info(organisation_group_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def organisation_groups_get_organisation_group_with_http_info(self, organisation_group_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular organisation group.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_group_with_http_info(organisation_group_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int organisation_group_id: The ID of the OrganisationGroup you want to get (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organisation_group_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisation_groups_get_organisation_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organisation_group_id' is set
        if ('organisation_group_id' not in params or
                params['organisation_group_id'] is None):
            raise ValueError("Missing the required parameter `organisation_group_id` when calling `organisation_groups_get_organisation_group`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `organisation_groups_get_organisation_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organisation_group_id' in params:
            query_params.append(('OrganisationGroupId', params['organisation_group_id']))  # noqa: E501

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
            '/api/OrganisationGroups/GetOrganisationGroup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseOrganisationGroup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def organisation_groups_get_organisation_groups(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a collection of organisation groups that are under your organisation.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_groups(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.organisation_groups_get_organisation_groups_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.organisation_groups_get_organisation_groups_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def organisation_groups_get_organisation_groups_with_http_info(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a collection of organisation groups that are under your organisation.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_groups_with_http_info(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisation_groups_get_organisation_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `organisation_groups_get_organisation_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/api/OrganisationGroups/GetOrganisationGroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListOrganisationGroup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def organisation_groups_get_organisation_groups_for_job(self, job_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get org groups for a particular job.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_groups_for_job(job_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int job_id: The ID of the job (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.organisation_groups_get_organisation_groups_for_job_with_http_info(job_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.organisation_groups_get_organisation_groups_for_job_with_http_info(job_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def organisation_groups_get_organisation_groups_for_job_with_http_info(self, job_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get org groups for a particular job.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_groups_for_job_with_http_info(job_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int job_id: The ID of the job (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method organisation_groups_get_organisation_groups_for_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `organisation_groups_get_organisation_groups_for_job`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `organisation_groups_get_organisation_groups_for_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('JobId', params['job_id']))  # noqa: E501

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
            '/api/OrganisationGroups/GetOrganisationGroupsForJob', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListOrganisationGroup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def organisation_groups_get_organisation_groups_for_vehicle(self, vehicle_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get org groups for a particular vehicle.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageFleet&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_groups_for_vehicle(vehicle_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vehicle_id: The ID of the vehicle (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListOrganisationGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.organisation_groups_get_organisation_groups_for_vehicle_with_http_info(vehicle_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.organisation_groups_get_organisation_groups_for_vehicle_with_http_info(vehicle_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def organisation_groups_get_organisation_groups_for_vehicle_with_http_info(self, vehicle_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get org groups for a particular vehicle.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageFleet&#39; or &#39;ManageOrganisationUsers&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_get_organisation_groups_for_vehicle_with_http_info(vehicle_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vehicle_id: The ID of the vehicle (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListOrganisationGroup
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
                    " to method organisation_groups_get_organisation_groups_for_vehicle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vehicle_id' is set
        if ('vehicle_id' not in params or
                params['vehicle_id'] is None):
            raise ValueError("Missing the required parameter `vehicle_id` when calling `organisation_groups_get_organisation_groups_for_vehicle`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `organisation_groups_get_organisation_groups_for_vehicle`")  # noqa: E501

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
            '/api/OrganisationGroups/GetOrganisationGroupsForVehicle', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListOrganisationGroup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def organisation_groups_update_organisation_group(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_update_organisation_group(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSSaveOrganisationGroupRequest request: A Save OrganisationGroup Request object containing updated fields.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.organisation_groups_update_organisation_group_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.organisation_groups_update_organisation_group_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def organisation_groups_update_organisation_group_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.organisation_groups_update_organisation_group_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSSaveOrganisationGroupRequest request: A Save OrganisationGroup Request object containing updated fields.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update (required)
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
                    " to method organisation_groups_update_organisation_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `organisation_groups_update_organisation_group`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `organisation_groups_update_organisation_group`")  # noqa: E501

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
            '/api/OrganisationGroups/UpdateOrganisationGroup', 'POST',
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
