# ChronoSheetsAPI.JobCodesApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_codes_create_job_code**](JobCodesApi.md#job_codes_create_job_code) | **POST** /JobCodes/CreateJobCode | Create a job code.    Requires the &#39;ManageJobsAndTask&#39; permission.
[**job_codes_delete_job_code**](JobCodesApi.md#job_codes_delete_job_code) | **DELETE** /JobCodes/DeleteJobCode | Delete a job code.    Requires the &#39;ManageJobsAndTask&#39; permission.
[**job_codes_get_job_code_by_id**](JobCodesApi.md#job_codes_get_job_code_by_id) | **GET** /JobCodes/GetJobCodeById | Get a particular job code by job code id.    Requires &#39;SubmitTimesheets&#39; or &#39;ManageJobsAndTasks&#39; permissions.
[**job_codes_get_job_codes**](JobCodesApi.md#job_codes_get_job_codes) | **GET** /JobCodes/GetJobCodes | Get job codes for your organisation.    Requires &#39;SubmitTimesheets&#39; or &#39;ManageJobsAndTasks&#39; permissions.
[**job_codes_update_job_code**](JobCodesApi.md#job_codes_update_job_code) | **PUT** /JobCodes/UpdateJobCode | Update a job code.    Requires the &#39;ManageJobsAndTask&#39; permission.


# **job_codes_create_job_code**
> ApiResponseInt32 job_codes_create_job_code(x_chronosheets_auth, request)

Create a job code.    Requires the 'ManageJobsAndTask' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import job_codes_api
from ChronoSheetsAPI.model.insert_job_code_request import InsertJobCodeRequest
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_codes_api.JobCodesApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = InsertJobCodeRequest(
        code="code_example",
        project_id=1,
        client_id=1,
        linked_task_ids=[
            1,
        ],
        linked_org_group_ids=[
            1,
        ],
    ) # InsertJobCodeRequest | An Insert JobCode Request object containing values for the new JobCode to create

    # example passing only required values which don't have defaults set
    try:
        # Create a job code.    Requires the 'ManageJobsAndTask' permission.
        api_response = api_instance.job_codes_create_job_code(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling JobCodesApi->job_codes_create_job_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**InsertJobCodeRequest**](InsertJobCodeRequest.md)| An Insert JobCode Request object containing values for the new JobCode to create |

### Return type

[**ApiResponseInt32**](ApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_delete_job_code**
> ApiResponseBoolean job_codes_delete_job_code(job_code_id, x_chronosheets_auth)

Delete a job code.    Requires the 'ManageJobsAndTask' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import job_codes_api
from ChronoSheetsAPI.model.api_response_boolean import ApiResponseBoolean
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_codes_api.JobCodesApi(api_client)
    job_code_id = 1 # int | The ID of the job code you want to delete
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Delete a job code.    Requires the 'ManageJobsAndTask' permission.
        api_response = api_instance.job_codes_delete_job_code(job_code_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling JobCodesApi->job_codes_delete_job_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_code_id** | **int**| The ID of the job code you want to delete |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseBoolean**](ApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_get_job_code_by_id**
> ApiResponseJobCode job_codes_get_job_code_by_id(job_code_id, x_chronosheets_auth)

Get a particular job code by job code id.    Requires 'SubmitTimesheets' or 'ManageJobsAndTasks' permissions.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import job_codes_api
from ChronoSheetsAPI.model.api_response_job_code import ApiResponseJobCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_codes_api.JobCodesApi(api_client)
    job_code_id = 1 # int | The ID of the JobCode you want to get
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get a particular job code by job code id.    Requires 'SubmitTimesheets' or 'ManageJobsAndTasks' permissions.
        api_response = api_instance.job_codes_get_job_code_by_id(job_code_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling JobCodesApi->job_codes_get_job_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_code_id** | **int**| The ID of the JobCode you want to get |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseJobCode**](ApiResponseJobCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_get_job_codes**
> ApiResponseListJobCode job_codes_get_job_codes(x_chronosheets_auth)

Get job codes for your organisation.    Requires 'SubmitTimesheets' or 'ManageJobsAndTasks' permissions.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import job_codes_api
from ChronoSheetsAPI.model.api_response_list_job_code import ApiResponseListJobCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_codes_api.JobCodesApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get job codes for your organisation.    Requires 'SubmitTimesheets' or 'ManageJobsAndTasks' permissions.
        api_response = api_instance.job_codes_get_job_codes(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling JobCodesApi->job_codes_get_job_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseListJobCode**](ApiResponseListJobCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_update_job_code**
> ApiResponseBoolean job_codes_update_job_code(x_chronosheets_auth, request)

Update a job code.    Requires the 'ManageJobsAndTask' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import job_codes_api
from ChronoSheetsAPI.model.update_job_code_request import UpdateJobCodeRequest
from ChronoSheetsAPI.model.api_response_boolean import ApiResponseBoolean
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = job_codes_api.JobCodesApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = UpdateJobCodeRequest(
        id=1,
        code="code_example",
        project_id=1,
        client_id=1,
        linked_task_ids=[
            1,
        ],
        linked_org_group_ids=[
            1,
        ],
        is_deleted=True,
    ) # UpdateJobCodeRequest | A Update JobCode Request object containing updated fields.  Make sure to specify the JobCode Id in the request object so that ChronoSheets knows which JobCode to update

    # example passing only required values which don't have defaults set
    try:
        # Update a job code.    Requires the 'ManageJobsAndTask' permission.
        api_response = api_instance.job_codes_update_job_code(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling JobCodesApi->job_codes_update_job_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**UpdateJobCodeRequest**](UpdateJobCodeRequest.md)| A Update JobCode Request object containing updated fields.  Make sure to specify the JobCode Id in the request object so that ChronoSheets knows which JobCode to update |

### Return type

[**ApiResponseBoolean**](ApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

