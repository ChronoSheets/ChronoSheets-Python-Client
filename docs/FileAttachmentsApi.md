# ChronoSheetsAPI.FileAttachmentsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_attachments_delete_timesheet_file_attachment**](FileAttachmentsApi.md#file_attachments_delete_timesheet_file_attachment) | **DELETE** /FileAttachments/DeleteTimesheetFileAttachment | Delete a particular timesheet file attachment  Requires the &#39;SubmitTimesheets&#39; permission.
[**file_attachments_get_file_attachment_by_id**](FileAttachmentsApi.md#file_attachments_get_file_attachment_by_id) | **GET** /FileAttachments/GetFileAttachmentById | Get a particular file attachment by ID.  User must own the file attachment for access.
[**file_attachments_get_my_file_attachments**](FileAttachmentsApi.md#file_attachments_get_my_file_attachments) | **GET** /FileAttachments/GetMyFileAttachments | Get my file attachments.  Get files you&#39;ve attached to timesheets.


# **file_attachments_delete_timesheet_file_attachment**
> ApiResponseBoolean file_attachments_delete_timesheet_file_attachment(file_attachment_id, x_chronosheets_auth)

Delete a particular timesheet file attachment  Requires the 'SubmitTimesheets' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import file_attachments_api
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
    api_instance = file_attachments_api.FileAttachmentsApi(api_client)
    file_attachment_id = 1 # int | The Id of the file attachment to delete
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Delete a particular timesheet file attachment  Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.file_attachments_delete_timesheet_file_attachment(file_attachment_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FileAttachmentsApi->file_attachments_delete_timesheet_file_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_attachment_id** | **int**| The Id of the file attachment to delete |
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

# **file_attachments_get_file_attachment_by_id**
> ApiResponseTimesheetFileAttachment file_attachments_get_file_attachment_by_id(file_attachment_id, x_chronosheets_auth)

Get a particular file attachment by ID.  User must own the file attachment for access.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import file_attachments_api
from ChronoSheetsAPI.model.api_response_timesheet_file_attachment import ApiResponseTimesheetFileAttachment
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = file_attachments_api.FileAttachmentsApi(api_client)
    file_attachment_id = 1 # int | The ID of the file attachment
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get a particular file attachment by ID.  User must own the file attachment for access.
        api_response = api_instance.file_attachments_get_file_attachment_by_id(file_attachment_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FileAttachmentsApi->file_attachments_get_file_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_attachment_id** | **int**| The ID of the file attachment |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseTimesheetFileAttachment**](ApiResponseTimesheetFileAttachment.md)

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

# **file_attachments_get_my_file_attachments**
> ApiResponseForPaginatedListTimesheetFileAttachment file_attachments_get_my_file_attachments(start_date, end_date, x_chronosheets_auth)

Get my file attachments.  Get files you've attached to timesheets.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import file_attachments_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_timesheet_file_attachment import ApiResponseForPaginatedListTimesheetFileAttachment
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = file_attachments_api.FileAttachmentsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The Start date of the date range.  File attachments after this date will be obtained.
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The End date of the date range.  File attachments before this date will be obtained.
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many File attachments (optional)
    take = 1 # int | Take this many File attachments (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get my file attachments.  Get files you've attached to timesheets.
        api_response = api_instance.file_attachments_get_my_file_attachments(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FileAttachmentsApi->file_attachments_get_my_file_attachments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get my file attachments.  Get files you've attached to timesheets.
        api_response = api_instance.file_attachments_get_my_file_attachments(start_date, end_date, x_chronosheets_auth, skip=skip, take=take)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FileAttachmentsApi->file_attachments_get_my_file_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The Start date of the date range.  File attachments after this date will be obtained. |
 **end_date** | **datetime**| The End date of the date range.  File attachments before this date will be obtained. |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many File attachments | [optional]
 **take** | **int**| Take this many File attachments | [optional]

### Return type

[**ApiResponseForPaginatedListTimesheetFileAttachment**](ApiResponseForPaginatedListTimesheetFileAttachment.md)

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

