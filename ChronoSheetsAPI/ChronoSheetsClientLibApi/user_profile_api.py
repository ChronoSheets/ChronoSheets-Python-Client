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


class UserProfileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_profile_do_login(self, request, **kwargs):  # noqa: E501
        """Login to your ChronoSheets account and obtain an Auth Token which you can use for other ChronoSheets API methods.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_do_login(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSDoLoginRequest request: A request object containing your username/email and password. (required)
        :return: CSApiResponseDoLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.user_profile_do_login_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.user_profile_do_login_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def user_profile_do_login_with_http_info(self, request, **kwargs):  # noqa: E501
        """Login to your ChronoSheets account and obtain an Auth Token which you can use for other ChronoSheets API methods.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_do_login_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSDoLoginRequest request: A request object containing your username/email and password. (required)
        :return: CSApiResponseDoLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_profile_do_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `user_profile_do_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/api/UserProfile/DoLogin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseDoLoginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_profile_do_logout(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Logout of your ChronoSheets account.  This method ends and deletes your active session.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_do_logout(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.user_profile_do_logout_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.user_profile_do_logout_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def user_profile_do_logout_with_http_info(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Logout of your ChronoSheets account.  This method ends and deletes your active session.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_do_logout_with_http_info(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
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
                    " to method user_profile_do_logout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `user_profile_do_logout`")  # noqa: E501

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
            '/api/UserProfile/DoLogout', 'DELETE',
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

    def user_profile_get_my_profile(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get your own profile.  Use this method to obtain detailed information about your ChronoSheets user profile.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_get_my_profile(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUserProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.user_profile_get_my_profile_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.user_profile_get_my_profile_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def user_profile_get_my_profile_with_http_info(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get your own profile.  Use this method to obtain detailed information about your ChronoSheets user profile.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_get_my_profile_with_http_info(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUserProfile
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
                    " to method user_profile_get_my_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `user_profile_get_my_profile`")  # noqa: E501

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
            '/api/UserProfile/GetMyProfile', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseUserProfile',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_profile_keep_session_alive(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Keep a session alive.  Use this method to keep a session active.  You could use this to &#39;ping&#39; ChronoSheets every &#39;x&#39; minutes to make sure your Auth Token will keep working.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_keep_session_alive(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.user_profile_keep_session_alive_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.user_profile_keep_session_alive_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def user_profile_keep_session_alive_with_http_info(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Keep a session alive.  Use this method to keep a session active.  You could use this to &#39;ping&#39; ChronoSheets every &#39;x&#39; minutes to make sure your Auth Token will keep working.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_keep_session_alive_with_http_info(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
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
                    " to method user_profile_keep_session_alive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `user_profile_keep_session_alive`")  # noqa: E501

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
            '/api/UserProfile/KeepSessionAlive', 'GET',
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

    def user_profile_update_my_profile(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update your own profile.  Use this method to update your profile information or update/change your password.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_update_my_profile(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSUpdateMyProfileRequest request: An Update MyProfile Request object containing updated fields. (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUpdateProfileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.user_profile_update_my_profile_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.user_profile_update_my_profile_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def user_profile_update_my_profile_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update your own profile.  Use this method to update your profile information or update/change your password.    Does not require any special permissions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.user_profile_update_my_profile_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSUpdateMyProfileRequest request: An Update MyProfile Request object containing updated fields. (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUpdateProfileResponse
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
                    " to method user_profile_update_my_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `user_profile_update_my_profile`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `user_profile_update_my_profile`")  # noqa: E501

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
            '/api/UserProfile/UpdateMyProfile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseUpdateProfileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
