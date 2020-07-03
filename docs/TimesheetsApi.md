# ChronoSheetsAPI.TimesheetsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheets_create_single_timesheet**](TimesheetsApi.md#timesheets_create_single_timesheet) | **POST** /Timesheets/CreateSingleTimesheet | Inserts a single timesheet record.    Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheets_delete_timesheet**](TimesheetsApi.md#timesheets_delete_timesheet) | **DELETE** /Timesheets/DeleteTimesheet | Delete a timesheet.    Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheets_get_timesheets**](TimesheetsApi.md#timesheets_get_timesheets) | **GET** /Timesheets/GetTimesheets | Get timesheets between start and end dates.  Note: the date range cannot exceed 24 hours.  This method is generally used to get timesheets for a particular day.    Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheets_update_timesheets**](TimesheetsApi.md#timesheets_update_timesheets) | **PUT** /Timesheets/UpdateTimesheets | Batch update timesheets.    Requires the &#39;SubmitTimesheets&#39; permission.


# **timesheets_create_single_timesheet**
> ApiResponseInt32 timesheets_create_single_timesheet(x_chronosheets_auth, request)

Inserts a single timesheet record.    Requires the 'SubmitTimesheets' permission.

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
    api_instance = ChronoSheetsAPI.TimesheetsApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.Timesheet() # Timesheet | A Timesheet Request object containing values for the new Timesheet to create

    try:
        # Inserts a single timesheet record.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_create_single_timesheet(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimesheetsApi->timesheets_create_single_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **request** | [**Timesheet**](Timesheet.md)| A Timesheet Request object containing values for the new Timesheet to create | 

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

# **timesheets_delete_timesheet**
> ApiResponseBoolean timesheets_delete_timesheet(timesheet_id, x_chronosheets_auth)

Delete a timesheet.    Requires the 'SubmitTimesheets' permission.

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
    api_instance = ChronoSheetsAPI.TimesheetsApi(api_client)
    timesheet_id = 56 # int | The ID of the Timesheet you want to delete
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Delete a timesheet.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_delete_timesheet(timesheet_id, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimesheetsApi->timesheets_delete_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet_id** | **int**| The ID of the Timesheet you want to delete | 
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

# **timesheets_get_timesheets**
> ApiResponseListTimesheet timesheets_get_timesheets(start_date, end_date, x_chronosheets_auth)

Get timesheets between start and end dates.  Note: the date range cannot exceed 24 hours.  This method is generally used to get timesheets for a particular day.    Requires the 'SubmitTimesheets' permission.

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
    api_instance = ChronoSheetsAPI.TimesheetsApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date of the date range
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date of the date range
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get timesheets between start and end dates.  Note: the date range cannot exceed 24 hours.  This method is generally used to get timesheets for a particular day.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_get_timesheets(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimesheetsApi->timesheets_get_timesheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date of the date range | 
 **end_date** | **datetime**| The end date of the date range | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**ApiResponseListTimesheet**](ApiResponseListTimesheet.md)

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

# **timesheets_update_timesheets**
> ApiResponseListInt32 timesheets_update_timesheets(x_chronosheets_auth, request)

Batch update timesheets.    Requires the 'SubmitTimesheets' permission.

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
    api_instance = ChronoSheetsAPI.TimesheetsApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.BatchUpdateTimesheetRequest() # BatchUpdateTimesheetRequest | A BatchUpdateTimesheet Request object containing values for the new Timesheets to create or update.  If the timesheet Id is specified, then an update will be performed, else the timesheet record will be created.

    try:
        # Batch update timesheets.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_update_timesheets(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimesheetsApi->timesheets_update_timesheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **request** | [**BatchUpdateTimesheetRequest**](BatchUpdateTimesheetRequest.md)| A BatchUpdateTimesheet Request object containing values for the new Timesheets to create or update.  If the timesheet Id is specified, then an update will be performed, else the timesheet record will be created. | 

### Return type

[**ApiResponseListInt32**](ApiResponseListInt32.md)

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

