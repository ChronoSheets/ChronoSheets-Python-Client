# ChronoSheetsAPI.TasksApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_create_task**](TasksApi.md#tasks_create_task) | **POST** /Tasks/CreateTask | Create a task.    Requires the &#39;ManageJobsAndTask&#39; permission.
[**tasks_delete_task**](TasksApi.md#tasks_delete_task) | **DELETE** /Tasks/DeleteTask | Delete a task.    Requires the &#39;ManageJobsAndTask&#39; permission.
[**tasks_get_task_by_id**](TasksApi.md#tasks_get_task_by_id) | **GET** /Tasks/GetTaskById | Get a particular task by Id.   Requires the &#39;SubmitTimesheets&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**tasks_get_tasks**](TasksApi.md#tasks_get_tasks) | **GET** /Tasks/GetTasks | Get tasks in your organisation.   Requires the &#39;SubmitTimesheets&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**tasks_get_tasks_for_job**](TasksApi.md#tasks_get_tasks_for_job) | **GET** /Tasks/GetTasksForJob | Get a collection of tasks for a particular Job, specified by JobId.    Requires the &#39;SubmitTimesheets&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**tasks_update_task**](TasksApi.md#tasks_update_task) | **PUT** /Tasks/UpdateTask | Update a task.    Requires the &#39;ManageJobsAndTask&#39; permission.


# **tasks_create_task**
> ApiResponseInt32 tasks_create_task(x_chronosheets_auth, request)

Create a task.    Requires the 'ManageJobsAndTask' permission.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.TasksApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.InsertTaskRequest() # InsertTaskRequest | An Insert Task Request object containing values for the new Task to create

    try:
        # Create a task.    Requires the 'ManageJobsAndTask' permission.
        api_response = api_instance.tasks_create_task(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **request** | [**InsertTaskRequest**](InsertTaskRequest.md)| An Insert Task Request object containing values for the new Task to create | 

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

# **tasks_delete_task**
> ApiResponseBoolean tasks_delete_task(task_id, x_chronosheets_auth)

Delete a task.    Requires the 'ManageJobsAndTask' permission.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.TasksApi(api_client)
    task_id = 56 # int | The ID of the Task you want to delete
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Delete a task.    Requires the 'ManageJobsAndTask' permission.
        api_response = api_instance.tasks_delete_task(task_id, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| The ID of the Task you want to delete | 
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

# **tasks_get_task_by_id**
> ApiResponseTimesheetTask tasks_get_task_by_id(task_id, x_chronosheets_auth)

Get a particular task by Id.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.TasksApi(api_client)
    task_id = 56 # int | The ID of the TimesheetTask you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get a particular task by Id.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.
        api_response = api_instance.tasks_get_task_by_id(task_id, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| The ID of the TimesheetTask you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**ApiResponseTimesheetTask**](ApiResponseTimesheetTask.md)

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

# **tasks_get_tasks**
> ApiResponseListTimesheetTask tasks_get_tasks(x_chronosheets_auth)

Get tasks in your organisation.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.TasksApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get tasks in your organisation.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.
        api_response = api_instance.tasks_get_tasks(x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**ApiResponseListTimesheetTask**](ApiResponseListTimesheetTask.md)

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

# **tasks_get_tasks_for_job**
> ApiResponseListTimesheetTask tasks_get_tasks_for_job(job_id, x_chronosheets_auth)

Get a collection of tasks for a particular Job, specified by JobId.    Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.TasksApi(api_client)
    job_id = 56 # int | The ID of the job
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get a collection of tasks for a particular Job, specified by JobId.    Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.
        api_response = api_instance.tasks_get_tasks_for_job(job_id, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_tasks_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| The ID of the job | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**ApiResponseListTimesheetTask**](ApiResponseListTimesheetTask.md)

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

# **tasks_update_task**
> ApiResponseBoolean tasks_update_task(x_chronosheets_auth, request)

Update a task.    Requires the 'ManageJobsAndTask' permission.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.TasksApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.UpdateTaskRequest() # UpdateTaskRequest | An Update Task Request object containing updated fields.  Make sure to specify the Task Id in the request object so that ChronoSheets knows which Task to update

    try:
        # Update a task.    Requires the 'ManageJobsAndTask' permission.
        api_response = api_instance.tasks_update_task(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **request** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| An Update Task Request object containing updated fields.  Make sure to specify the Task Id in the request object so that ChronoSheets knows which Task to update | 

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

