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
> CSApiResponseInt32 tasks_create_task(request, x_chronosheets_auth)

Create a task.    Requires the 'ManageJobsAndTask' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TasksApi()
request = ChronoSheetsAPI.CSInsertTaskRequest() # CSInsertTaskRequest | An Insert Task Request object containing values for the new Task to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a task.    Requires the 'ManageJobsAndTask' permission.
    api_response = api_instance.tasks_create_task(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertTaskRequest**](CSInsertTaskRequest.md)| An Insert Task Request object containing values for the new Task to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_delete_task**
> CSApiResponseBoolean tasks_delete_task(task_id, x_chronosheets_auth)

Delete a task.    Requires the 'ManageJobsAndTask' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TasksApi()
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

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get_task_by_id**
> CSApiResponseTimesheetTask tasks_get_task_by_id(task_id, x_chronosheets_auth)

Get a particular task by Id.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TasksApi()
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

[**CSApiResponseTimesheetTask**](CSApiResponseTimesheetTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get_tasks**
> CSApiResponseListTimesheetTask tasks_get_tasks(x_chronosheets_auth)

Get tasks in your organisation.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TasksApi()
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

[**CSApiResponseListTimesheetTask**](CSApiResponseListTimesheetTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get_tasks_for_job**
> CSApiResponseListTimesheetTask tasks_get_tasks_for_job(job_id, x_chronosheets_auth)

Get a collection of tasks for a particular Job, specified by JobId.    Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TasksApi()
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

[**CSApiResponseListTimesheetTask**](CSApiResponseListTimesheetTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update_task**
> CSApiResponseBoolean tasks_update_task(request, x_chronosheets_auth)

Update a task.    Requires the 'ManageJobsAndTask' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TasksApi()
request = ChronoSheetsAPI.CSUpdateTaskRequest() # CSUpdateTaskRequest | An Update Task Request object containing updated fields.  Make sure to specify the Task Id in the request object so that ChronoSheets knows which Task to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a task.    Requires the 'ManageJobsAndTask' permission.
    api_response = api_instance.tasks_update_task(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSUpdateTaskRequest**](CSUpdateTaskRequest.md)| An Update Task Request object containing updated fields.  Make sure to specify the Task Id in the request object so that ChronoSheets knows which Task to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

