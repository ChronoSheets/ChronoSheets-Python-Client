# ChronoSheetsAPI.TimesheetAutomationApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheet_automation_create_automation_step**](TimesheetAutomationApi.md#timesheet_automation_create_automation_step) | **POST** /TimesheetAutomation/CreateAutomationStep | Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheet_automation_get_timesheet_automation_audit_trail**](TimesheetAutomationApi.md#timesheet_automation_get_timesheet_automation_audit_trail) | **GET** /TimesheetAutomation/GetTimesheetAutomationAuditTrail | Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the &#39;ManageGeofencing&#39; permission.


# **timesheet_automation_create_automation_step**
> CSApiResponseInt32 timesheet_automation_create_automation_step(request, x_chronosheets_auth)

Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TimesheetAutomationApi()
request = ChronoSheetsAPI.CSCreateAutomationStepRequest() # CSCreateAutomationStepRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the 'SubmitTimesheets' permission.
    api_response = api_instance.timesheet_automation_create_automation_step(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetAutomationApi->timesheet_automation_create_automation_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSCreateAutomationStepRequest**](CSCreateAutomationStepRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timesheet_automation_get_timesheet_automation_audit_trail**
> CSApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence timesheet_automation_get_timesheet_automation_audit_trail(geofence_id, user_id, sort, order, x_chronosheets_auth, skip=skip, take=take)

Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the 'ManageGeofencing' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TimesheetAutomationApi()
geofence_id = 56 # int | The ID of the Geofence
user_id = 56 # int | 
sort = 'sort_example' # str | 
order = 'order_example' # str | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
skip = 56 # int | Skip this many records (optional)
take = 56 # int | Take this many records (optional)

try:
    # Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the 'ManageGeofencing' permission.
    api_response = api_instance.timesheet_automation_get_timesheet_automation_audit_trail(geofence_id, user_id, sort, order, x_chronosheets_auth, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetAutomationApi->timesheet_automation_get_timesheet_automation_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **int**| The ID of the Geofence | 
 **user_id** | **int**|  | 
 **sort** | **str**|  | 
 **order** | **str**|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **skip** | **int**| Skip this many records | [optional] 
 **take** | **int**| Take this many records | [optional] 

### Return type

[**CSApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence**](CSApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

