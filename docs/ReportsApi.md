# ChronoSheetsAPI.ReportsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_get_all_charts_data_admin**](ReportsApi.md#reports_get_all_charts_data_admin) | **GET** /Reports/GetAllChartsDataAdmin | Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.    Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_all_charts_data_user**](ReportsApi.md#reports_get_all_charts_data_user) | **GET** /Reports/GetAllChartsDataUser | Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user&#39;s own reports.    Requires the &#39;ViewOwnReports&#39; permission.
[**reports_get_fleet_summary_admin**](ReportsApi.md#reports_get_fleet_summary_admin) | **GET** /Reports/GetFleetSummaryAdmin | Gets a summary report, which includes total distance travelled and total running costs, for vehicles within your organisation  Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_org_trip_by_id**](ReportsApi.md#reports_get_org_trip_by_id) | **GET** /Reports/GetOrgTripById | Get trip by Id, for reporting purposes.    Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_organisation_timesheet_file_attachments**](ReportsApi.md#reports_get_organisation_timesheet_file_attachments) | **GET** /Reports/GetOrganisationTimesheetFileAttachments | Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records)  Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_organisation_transcripts**](ReportsApi.md#reports_get_organisation_transcripts) | **GET** /Reports/GetOrganisationTranscripts | Reports on Organisation transcripts (When an audio file is attached, it will be automatically transcribed, these are the transcriptions)    Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_organisation_trips**](ReportsApi.md#reports_get_organisation_trips) | **GET** /Reports/GetOrganisationTrips | Reports on Organisation trips (GPS tracking from whole organisation).    Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_raw_data_admin**](ReportsApi.md#reports_get_raw_data_admin) | **GET** /Reports/GetRawDataAdmin | Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.    Requires the &#39;ReportAdmin&#39; permission.
[**reports_project_costings_admin**](ReportsApi.md#reports_project_costings_admin) | **GET** /Reports/ProjectCostingsAdmin | Gets project cost estimations VS actual cost for date range and users.    Requires the &#39;ReportAdmin&#39; permission.
[**reports_user_jobs_over_time**](ReportsApi.md#reports_user_jobs_over_time) | **GET** /Reports/UserJobsOverTime | Timeseries jobs data for the logged in user.    Requires the &#39;ViewOwnReports&#39; or &#39;SubmitTimesheets&#39;.


# **reports_get_all_charts_data_admin**
> ApiResponseCombinedReportsData reports_get_all_charts_data_admin(start_date, end_date, x_chronosheets_auth)

Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.    Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_combined_reports_data import ApiResponseCombinedReportsData
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)
    force_only_this_chart = "NotForced" # str | A flag to indicate which report data you require.  Choose a particular set of data, or if you want all data use the 'NotForced' option. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_all_charts_data_admin(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_all_charts_data_admin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_all_charts_data_admin(start_date, end_date, x_chronosheets_auth, user_ids=user_ids, force_only_this_chart=force_only_this_chart)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_all_charts_data_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]
 **force_only_this_chart** | **str**| A flag to indicate which report data you require.  Choose a particular set of data, or if you want all data use the &#39;NotForced&#39; option. | [optional]

### Return type

[**ApiResponseCombinedReportsData**](ApiResponseCombinedReportsData.md)

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

# **reports_get_all_charts_data_user**
> ApiResponseCombinedReportsData reports_get_all_charts_data_user(start_date, end_date, x_chronosheets_auth)

Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user's own reports.    Requires the 'ViewOwnReports' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_combined_reports_data import ApiResponseCombinedReportsData
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user's own reports.    Requires the 'ViewOwnReports' permission.
        api_response = api_instance.reports_get_all_charts_data_user(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_all_charts_data_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseCombinedReportsData**](ApiResponseCombinedReportsData.md)

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

# **reports_get_fleet_summary_admin**
> ApiResponseListFleetSummaryReportItem reports_get_fleet_summary_admin(start_date, end_date, x_chronosheets_auth)

Gets a summary report, which includes total distance travelled and total running costs, for vehicles within your organisation  Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_list_fleet_summary_report_item import ApiResponseListFleetSummaryReportItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a summary report, which includes total distance travelled and total running costs, for vehicles within your organisation  Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_fleet_summary_admin(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_fleet_summary_admin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a summary report, which includes total distance travelled and total running costs, for vehicles within your organisation  Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_fleet_summary_admin(start_date, end_date, x_chronosheets_auth, user_ids=user_ids)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_fleet_summary_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]

### Return type

[**ApiResponseListFleetSummaryReportItem**](ApiResponseListFleetSummaryReportItem.md)

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

# **reports_get_org_trip_by_id**
> ApiResponseTrip reports_get_org_trip_by_id(trip_id, x_chronosheets_auth)

Get trip by Id, for reporting purposes.    Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_trip import ApiResponseTrip
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    trip_id = 1 # int | The ID of the Trip you want to get
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get trip by Id, for reporting purposes.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_org_trip_by_id(trip_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_org_trip_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_id** | **int**| The ID of the Trip you want to get |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseTrip**](ApiResponseTrip.md)

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

# **reports_get_organisation_timesheet_file_attachments**
> ApiResponseForPaginatedListOrgReportTimesheetFileAttachment reports_get_organisation_timesheet_file_attachments(start_date, end_date, x_chronosheets_auth)

Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records)  Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_org_report_timesheet_file_attachment import ApiResponseForPaginatedListOrgReportTimesheetFileAttachment
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many items (optional)
    take = 1 # int | Take this many items (optional)
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records)  Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_organisation_timesheet_file_attachments(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_organisation_timesheet_file_attachments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records)  Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_organisation_timesheet_file_attachments(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, user_ids=user_ids)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_organisation_timesheet_file_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many items | [optional]
 **take** | **int**| Take this many items | [optional]
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]

### Return type

[**ApiResponseForPaginatedListOrgReportTimesheetFileAttachment**](ApiResponseForPaginatedListOrgReportTimesheetFileAttachment.md)

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

# **reports_get_organisation_transcripts**
> ApiResponseForPaginatedListOrgReportTranscript reports_get_organisation_transcripts(start_date, end_date, x_chronosheets_auth)

Reports on Organisation transcripts (When an audio file is attached, it will be automatically transcribed, these are the transcriptions)    Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_org_report_transcript import ApiResponseForPaginatedListOrgReportTranscript
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many items (optional)
    take = 1 # int | Take this many items (optional)
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)
    keywords = "Keywords_example" # str | Search the transcripts by keyword(s) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reports on Organisation transcripts (When an audio file is attached, it will be automatically transcribed, these are the transcriptions)    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_organisation_transcripts(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_organisation_transcripts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reports on Organisation transcripts (When an audio file is attached, it will be automatically transcribed, these are the transcriptions)    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_organisation_transcripts(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, user_ids=user_ids, keywords=keywords)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_organisation_transcripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many items | [optional]
 **take** | **int**| Take this many items | [optional]
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]
 **keywords** | **str**| Search the transcripts by keyword(s) | [optional]

### Return type

[**ApiResponseForPaginatedListOrgReportTranscript**](ApiResponseForPaginatedListOrgReportTranscript.md)

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

# **reports_get_organisation_trips**
> ApiResponseForPaginatedListOrgReportTrip reports_get_organisation_trips(start_date, end_date, x_chronosheets_auth)

Reports on Organisation trips (GPS tracking from whole organisation).    Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_org_report_trip import ApiResponseForPaginatedListOrgReportTrip
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many items (optional)
    take = 1 # int | Take this many items (optional)
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reports on Organisation trips (GPS tracking from whole organisation).    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_organisation_trips(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_organisation_trips: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reports on Organisation trips (GPS tracking from whole organisation).    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_organisation_trips(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, user_ids=user_ids)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_organisation_trips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many items | [optional]
 **take** | **int**| Take this many items | [optional]
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]

### Return type

[**ApiResponseForPaginatedListOrgReportTrip**](ApiResponseForPaginatedListOrgReportTrip.md)

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

# **reports_get_raw_data_admin**
> ApiResponseForPaginatedListRawReportItem reports_get_raw_data_admin(start_date, end_date, x_chronosheets_auth)

Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.    Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_raw_report_item import ApiResponseForPaginatedListRawReportItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)
    sort = "EmailAddress" # str | Decide which column to sort on (optional)
    order = "Ascending" # str | Decide which direction to sort the column (optional)
    skip = 1 # int | Skip this many rows (optional)
    take = 1 # int | Take this many rows (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_raw_data_admin(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_raw_data_admin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_get_raw_data_admin(start_date, end_date, x_chronosheets_auth, user_ids=user_ids, sort=sort, order=order, skip=skip, take=take)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_get_raw_data_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]
 **sort** | **str**| Decide which column to sort on | [optional]
 **order** | **str**| Decide which direction to sort the column | [optional]
 **skip** | **int**| Skip this many rows | [optional]
 **take** | **int**| Take this many rows | [optional]

### Return type

[**ApiResponseForPaginatedListRawReportItem**](ApiResponseForPaginatedListRawReportItem.md)

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

# **reports_project_costings_admin**
> ApiResponseListProjectCostingReportItem reports_project_costings_admin(start_date, end_date, x_chronosheets_auth)

Gets project cost estimations VS actual cost for date range and users.    Requires the 'ReportAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_list_project_costing_report_item import ApiResponseListProjectCostingReportItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    user_ids = "UserIds_example" # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets project cost estimations VS actual cost for date range and users.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_project_costings_admin(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_project_costings_admin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets project cost estimations VS actual cost for date range and users.    Requires the 'ReportAdmin' permission.
        api_response = api_instance.reports_project_costings_admin(start_date, end_date, x_chronosheets_auth, user_ids=user_ids)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_project_costings_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | [optional]

### Return type

[**ApiResponseListProjectCostingReportItem**](ApiResponseListProjectCostingReportItem.md)

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

# **reports_user_jobs_over_time**
> ApiResponseListJobSeriesReportItem reports_user_jobs_over_time(start_date, end_date, x_chronosheets_auth)

Timeseries jobs data for the logged in user.    Requires the 'ViewOwnReports' or 'SubmitTimesheets'.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import reports_api
from ChronoSheetsAPI.model.api_response_list_job_series_report_item import ApiResponseListJobSeriesReportItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reports_api.ReportsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The start date for the date range.  Report data in the response is after this date
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The end date for the date range.  Report data in the response is before this date
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Timeseries jobs data for the logged in user.    Requires the 'ViewOwnReports' or 'SubmitTimesheets'.
        api_response = api_instance.reports_user_jobs_over_time(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling ReportsApi->reports_user_jobs_over_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date |
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseListJobSeriesReportItem**](ApiResponseListJobSeriesReportItem.md)

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

