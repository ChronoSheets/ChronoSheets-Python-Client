# ChronoSheetsAPI.AggregateJobTasksApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_job_tasks_get_aggregate_job_tasks**](AggregateJobTasksApi.md#aggregate_job_tasks_get_aggregate_job_tasks) | **GET** /api/AggregateJobTasks/GetAggregateJobTasks | Get jobs and tasks information, aggregated.  Requires the &#39;SubmitTimesheets&#39; or &#39;ManageJobsAndTask&#39; permissions.


# **aggregate_job_tasks_get_aggregate_job_tasks**
> CSApiResponseListAggregateJobCode aggregate_job_tasks_get_aggregate_job_tasks(x_chronosheets_auth)

Get jobs and tasks information, aggregated.  Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.AggregateJobTasksApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get jobs and tasks information, aggregated.  Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.
    api_response = api_instance.aggregate_job_tasks_get_aggregate_job_tasks(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregateJobTasksApi->aggregate_job_tasks_get_aggregate_job_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListAggregateJobCode**](CSApiResponseListAggregateJobCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

