# ChronoSheetsAPI.FileAttachmentsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_attachments_get_my_file_attachments**](FileAttachmentsApi.md#file_attachments_get_my_file_attachments) | **GET** /api/FileAttachments/GetMyFileAttachments | Get my file attachments.  Get files you&#39;ve attached to timesheets.


# **file_attachments_get_my_file_attachments**
> CSApiResponseForPaginatedListTimesheetFileAttachment file_attachments_get_my_file_attachments(start_date, end_date, skip, take, x_chronosheets_auth)

Get my file attachments.  Get files you've attached to timesheets.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FileAttachmentsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The Start date of the date range.  File attachments after this date will be obtained.
end_date = '2013-10-20T19:20:30+01:00' # datetime | The End date of the date range.  File attachments before this date will be obtained.
skip = 56 # int | Skip this many File attachments
take = 56 # int | Take this many File attachments
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get my file attachments.  Get files you've attached to timesheets.
    api_response = api_instance.file_attachments_get_my_file_attachments(start_date, end_date, skip, take, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileAttachmentsApi->file_attachments_get_my_file_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The Start date of the date range.  File attachments after this date will be obtained. | 
 **end_date** | **datetime**| The End date of the date range.  File attachments before this date will be obtained. | 
 **skip** | **int**| Skip this many File attachments | 
 **take** | **int**| Take this many File attachments | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseForPaginatedListTimesheetFileAttachment**](CSApiResponseForPaginatedListTimesheetFileAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

