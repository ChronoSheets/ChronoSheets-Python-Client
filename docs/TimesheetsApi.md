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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import timesheets_api
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.timesheet import Timesheet
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = timesheets_api.TimesheetsApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = Timesheet(
        timesheet_id=1,
        user_id=1,
        job_id=1,
        task_id=1,
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        description="description_example",
        trip_id=1,
        file_attachment_count=1,
        pay_amount=3.14,
        overtime_pay_amount=3.14,
        includes_overtime=True,
    ) # Timesheet | A Timesheet Request object containing values for the new Timesheet to create

    # example passing only required values which don't have defaults set
    try:
        # Inserts a single timesheet record.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_create_single_timesheet(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import timesheets_api
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
    api_instance = timesheets_api.TimesheetsApi(api_client)
    timesheet_id = 1 # int | The ID of the Timesheet you want to delete
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Delete a timesheet.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_delete_timesheet(timesheet_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import timesheets_api
from ChronoSheetsAPI.model.api_response_list_timesheet import ApiResponseListTimesheet
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = timesheets_api.TimesheetsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date of the date range
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date of the date range
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get timesheets between start and end dates.  Note: the date range cannot exceed 24 hours.  This method is generally used to get timesheets for a particular day.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_get_timesheets(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import timesheets_api
from ChronoSheetsAPI.model.api_response_list_int32 import ApiResponseListInt32
from ChronoSheetsAPI.model.batch_update_timesheet_request import BatchUpdateTimesheetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = timesheets_api.TimesheetsApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = BatchUpdateTimesheetRequest(
        timesheets=[
            Timesheet(
                timesheet_id=1,
                user_id=1,
                job_id=1,
                task_id=1,
                start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                description="description_example",
                trip_id=1,
                file_attachment_count=1,
                pay_amount=3.14,
                overtime_pay_amount=3.14,
                includes_overtime=True,
            ),
        ],
    ) # BatchUpdateTimesheetRequest | A BatchUpdateTimesheet Request object containing values for the new Timesheets to create or update.  If the timesheet Id is specified, then an update will be performed, else the timesheet record will be created.

    # example passing only required values which don't have defaults set
    try:
        # Batch update timesheets.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheets_update_timesheets(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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

