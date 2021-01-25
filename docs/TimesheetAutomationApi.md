# ChronoSheetsAPI.TimesheetAutomationApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheet_automation_create_automation_step**](TimesheetAutomationApi.md#timesheet_automation_create_automation_step) | **POST** /TimesheetAutomation/CreateAutomationStep | Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the &#39;SubmitTimesheets&#39; permission.
[**timesheet_automation_get_timesheet_automation_audit_trail**](TimesheetAutomationApi.md#timesheet_automation_get_timesheet_automation_audit_trail) | **GET** /TimesheetAutomation/GetTimesheetAutomationAuditTrail | Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the &#39;ManageGeofencing&#39; permission.


# **timesheet_automation_create_automation_step**
> ApiResponseInt32 timesheet_automation_create_automation_step(x_chronosheets_auth, request)

Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the 'SubmitTimesheets' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import timesheet_automation_api
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.create_automation_step_request import CreateAutomationStepRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = timesheet_automation_api.TimesheetAutomationApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = CreateAutomationStepRequest(
        geofencing_id=1,
        nfc_id=1,
        automation_action_type="EnterGeofence",
        latitude=3.14,
        longitude=3.14,
        client_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CreateAutomationStepRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.timesheet_automation_create_automation_step(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TimesheetAutomationApi->timesheet_automation_create_automation_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**CreateAutomationStepRequest**](CreateAutomationStepRequest.md)|  |

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

# **timesheet_automation_get_timesheet_automation_audit_trail**
> ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence timesheet_automation_get_timesheet_automation_audit_trail(geofence_id, nfc_id, user_id, sort, order, x_chronosheets_auth)

Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the 'ManageGeofencing' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import timesheet_automation_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_timesheet_automation_with_org_and_geofence import ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = timesheet_automation_api.TimesheetAutomationApi(api_client)
    geofence_id = 1 # int | The ID of the Geofence
    nfc_id = 1 # int | 
    user_id = 1 # int | 
    sort = "UserName" # str | 
    order = "Ascending" # str | 
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many records (optional)
    take = 1 # int | Take this many records (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the 'ManageGeofencing' permission.
        api_response = api_instance.timesheet_automation_get_timesheet_automation_audit_trail(geofence_id, nfc_id, user_id, sort, order, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TimesheetAutomationApi->timesheet_automation_get_timesheet_automation_audit_trail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the 'ManageGeofencing' permission.
        api_response = api_instance.timesheet_automation_get_timesheet_automation_audit_trail(geofence_id, nfc_id, user_id, sort, order, x_chronosheets_auth, skip=skip, take=take)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TimesheetAutomationApi->timesheet_automation_get_timesheet_automation_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **int**| The ID of the Geofence |
 **nfc_id** | **int**|  |
 **user_id** | **int**|  |
 **sort** | **str**|  |
 **order** | **str**|  |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many records | [optional]
 **take** | **int**| Take this many records | [optional]

### Return type

[**ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence**](ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence.md)

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

