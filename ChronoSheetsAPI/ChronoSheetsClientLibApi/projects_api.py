"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ChronoSheetsAPI.api_client import ApiClient, Endpoint
from ChronoSheetsAPI.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ChronoSheetsAPI.model.api_response_boolean import ApiResponseBoolean
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.api_response_list_project import ApiResponseListProject
from ChronoSheetsAPI.model.api_response_project import ApiResponseProject
from ChronoSheetsAPI.model.insert_project_request import InsertProjectRequest
from ChronoSheetsAPI.model.update_project_request import UpdateProjectRequest


class ProjectsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __projects_create_project(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Create a project.    Requires the 'ManageClientsAndProjects' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_create_project(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (InsertProjectRequest): An Insert Project Request object containing values for the new Project to create.  Make sure to specify a correct Client Id - this will be used to attach the new project under that client.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponseInt32
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            kwargs['request'] = \
                request
            return self.call_with_http_info(**kwargs)

        self.projects_create_project = Endpoint(
            settings={
                'response_type': (ApiResponseInt32,),
                'auth': [],
                'endpoint_path': '/Projects/CreateProject',
                'operation_id': 'projects_create_project',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_chronosheets_auth',
                    'request',
                ],
                'required': [
                    'x_chronosheets_auth',
                    'request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_chronosheets_auth':
                        (str,),
                    'request':
                        (InsertProjectRequest,),
                },
                'attribute_map': {
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'x_chronosheets_auth': 'header',
                    'request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'multipart/form-data'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__projects_create_project
        )

        def __projects_get_project_by_id(
            self,
            project_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get a project by its Id.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_get_project_by_id(project_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (int): The ID of the Project you want to get
                x_chronosheets_auth (str): The ChronoSheets Auth Token

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponseProject
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.projects_get_project_by_id = Endpoint(
            settings={
                'response_type': (ApiResponseProject,),
                'auth': [],
                'endpoint_path': '/Projects/GetProjectById',
                'operation_id': 'projects_get_project_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'project_id',
                    'x_chronosheets_auth',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'ProjectId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'project_id': 'query',
                    'x_chronosheets_auth': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'multipart/form-data'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__projects_get_project_by_id
        )

        def __projects_get_projects_for_client(
            self,
            client_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get projects for a particular client.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_get_projects_for_client(client_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                client_id (int): The ID of the client
                x_chronosheets_auth (str): The ChronoSheets Auth Token

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponseListProject
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['client_id'] = \
                client_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.projects_get_projects_for_client = Endpoint(
            settings={
                'response_type': (ApiResponseListProject,),
                'auth': [],
                'endpoint_path': '/Projects/GetProjectsForClient',
                'operation_id': 'projects_get_projects_for_client',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'client_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'client_id',
                    'x_chronosheets_auth',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'client_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'client_id': 'ClientId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'client_id': 'query',
                    'x_chronosheets_auth': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'multipart/form-data'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__projects_get_projects_for_client
        )

        def __projects_update_project(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Update a project.    Requires the 'ManageClientsAndProjects' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_update_project(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (UpdateProjectRequest): An Update Project Request object containing updated fields.  Make sure to specify the Project Id in the request object so that ChronoSheets knows which Project to update

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponseBoolean
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            kwargs['request'] = \
                request
            return self.call_with_http_info(**kwargs)

        self.projects_update_project = Endpoint(
            settings={
                'response_type': (ApiResponseBoolean,),
                'auth': [],
                'endpoint_path': '/Projects/UpdateProject',
                'operation_id': 'projects_update_project',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_chronosheets_auth',
                    'request',
                ],
                'required': [
                    'x_chronosheets_auth',
                    'request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_chronosheets_auth':
                        (str,),
                    'request':
                        (UpdateProjectRequest,),
                },
                'attribute_map': {
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'x_chronosheets_auth': 'header',
                    'request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'multipart/form-data'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__projects_update_project
        )
