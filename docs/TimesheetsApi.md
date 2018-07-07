# ChronoSheetsAPI.TimesheetsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheets_create_single_timesheet**](TimesheetsApi.md#timesheets_create_single_timesheet) | **PUT** /api/Timesheets/CreateSingleTimesheet | Inserts a single timesheet record.    Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheets_delete_timesheet**](TimesheetsApi.md#timesheets_delete_timesheet) | **DELETE** /api/Timesheets/DeleteTimesheet | Delete a timesheet.    Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheets_get_timesheets**](TimesheetsApi.md#timesheets_get_timesheets) | **GET** /api/Timesheets/GetTimesheets | Get timesheets between start and end dates.  Note: the date range cannot exceed 24 hours.  This method is generally used to get timesheets for a particular day.    Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheets_update_timesheets**](TimesheetsApi.md#timesheets_update_timesheets) | **POST** /api/Timesheets/UpdateTimesheets | Batch update timesheets.    Requires the &#39;SubmitTimesheets&#39; permission.


# **timesheets_create_single_timesheet**
> CSApiResponseInt32 timesheets_create_single_timesheet(request, x_chronosheets_auth)

Inserts a single timesheet record.    Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TimesheetsApi()
request = ChronoSheetsAPI.CSTimesheet() # CSTimesheet | A Timesheet Request object containing values for the new Timesheet to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Inserts a single timesheet record.    Requires the 'SubmitTimesheets' permission.
    api_response = api_instance.timesheets_create_single_timesheet(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetsApi->timesheets_create_single_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSTimesheet**](CSTimesheet.md)| A Timesheet Request object containing values for the new Timesheet to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheets_delete_timesheet**
> CSApiResponseBoolean timesheets_delete_timesheet(timesheet_id, x_chronosheets_auth)

Delete a timesheet.    Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TimesheetsApi()
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

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheets_get_timesheets**
> CSApiResponseListTimesheet timesheets_get_timesheets(start_date, end_date, x_chronosheets_auth)

Get timesheets between start and end dates.  Note: the date range cannot exceed 24 hours.  This method is generally used to get timesheets for a particular day.    Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TimesheetsApi()
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

[**CSApiResponseListTimesheet**](CSApiResponseListTimesheet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheets_update_timesheets**
> CSApiResponseListInt32 timesheets_update_timesheets(request, x_chronosheets_auth)

Batch update timesheets.    Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TimesheetsApi()
request = ChronoSheetsAPI.CSBatchUpdateTimesheetRequest() # CSBatchUpdateTimesheetRequest | A BatchUpdateTimesheet Request object containing values for the new Timesheets to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Batch update timesheets.    Requires the 'SubmitTimesheets' permission.
    api_response = api_instance.timesheets_update_timesheets(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetsApi->timesheets_update_timesheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSBatchUpdateTimesheetRequest**](CSBatchUpdateTimesheetRequest.md)| A BatchUpdateTimesheet Request object containing values for the new Timesheets to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListInt32**](CSApiResponseListInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

