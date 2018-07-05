# ChronoSheetsAPI.ReportsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_get_all_charts_data_admin**](ReportsApi.md#reports_get_all_charts_data_admin) | **GET** /api/Reports/GetAllChartsDataAdmin | Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.  Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_all_charts_data_user**](ReportsApi.md#reports_get_all_charts_data_user) | **GET** /api/Reports/GetAllChartsDataUser | Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user&#39;s own reports.  Requires the &#39;ViewOwnReports&#39; permission.
[**reports_get_org_trip_by_id**](ReportsApi.md#reports_get_org_trip_by_id) | **GET** /api/Reports/GetOrgTripById | Get trip by Id, for reporting purposes.  Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_organisation_timesheet_file_attachments**](ReportsApi.md#reports_get_organisation_timesheet_file_attachments) | **GET** /api/Reports/GetOrganisationTimesheetFileAttachments | Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records.  Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_organisation_trips**](ReportsApi.md#reports_get_organisation_trips) | **GET** /api/Reports/GetOrganisationTrips | Reports on Organisation trips (GPS tracking from whole organisation).  Requires the &#39;ReportAdmin&#39; permission.
[**reports_get_raw_data_admin**](ReportsApi.md#reports_get_raw_data_admin) | **GET** /api/Reports/GetRawDataAdmin | Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.  Requires the &#39;ReportAdmin&#39; permission.
[**reports_project_costings_admin**](ReportsApi.md#reports_project_costings_admin) | **GET** /api/Reports/ProjectCostingsAdmin | Gets project cost estimations VS actual cost for date range and users.  Requires the &#39;ReportAdmin&#39; permission.
[**reports_user_jobs_over_time**](ReportsApi.md#reports_user_jobs_over_time) | **GET** /api/Reports/UserJobsOverTime | Timeseries jobs data for the logged in user.  Requires the &#39;ViewOwnReports&#39; or &#39;SubmitTimesheets&#39;.


# **reports_get_all_charts_data_admin**
> CSApiResponseCombinedReportsData reports_get_all_charts_data_admin(start_date, end_date, user_ids, x_chronosheets_auth)

Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.  Requires the 'ReportAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
user_ids = 'user_ids_example' # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get Consolidated Admin Reports Data (Jobs, Tasks, Clients and Projects).  These are the organisation wide reports, with data from potentially all employees.  Requires the 'ReportAdmin' permission.
    api_response = api_instance.reports_get_all_charts_data_admin(start_date, end_date, user_ids, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get_all_charts_data_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseCombinedReportsData**](CSApiResponseCombinedReportsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get_all_charts_data_user**
> CSApiResponseCombinedReportsData reports_get_all_charts_data_user(start_date, end_date, x_chronosheets_auth)

Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user's own reports.  Requires the 'ViewOwnReports' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get Consolidated User Reports Data (Jobs, Tasks, Clients and Projects).  These are the user's own reports.  Requires the 'ViewOwnReports' permission.
    api_response = api_instance.reports_get_all_charts_data_user(start_date, end_date, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get_all_charts_data_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseCombinedReportsData**](CSApiResponseCombinedReportsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get_org_trip_by_id**
> CSApiResponseTrip reports_get_org_trip_by_id(trip_id, x_chronosheets_auth)

Get trip by Id, for reporting purposes.  Requires the 'ReportAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
trip_id = 56 # int | The ID of the Trip you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get trip by Id, for reporting purposes.  Requires the 'ReportAdmin' permission.
    api_response = api_instance.reports_get_org_trip_by_id(trip_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get_org_trip_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_id** | **int**| The ID of the Trip you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseTrip**](CSApiResponseTrip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get_organisation_timesheet_file_attachments**
> CSApiResponseForPaginatedListOrgReportTimesheetFileAttachment reports_get_organisation_timesheet_file_attachments(start_date, end_date, skip, take, user_ids, x_chronosheets_auth)

Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records.  Requires the 'ReportAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
skip = 56 # int | Skip this many items
take = 56 # int | Take this many items
user_ids = 'user_ids_example' # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Reports on Organisation timesheet file attachments (files uploaded and attached to timesheet records.  Requires the 'ReportAdmin' permission.
    api_response = api_instance.reports_get_organisation_timesheet_file_attachments(start_date, end_date, skip, take, user_ids, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get_organisation_timesheet_file_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **skip** | **int**| Skip this many items | 
 **take** | **int**| Take this many items | 
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseForPaginatedListOrgReportTimesheetFileAttachment**](CSApiResponseForPaginatedListOrgReportTimesheetFileAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get_organisation_trips**
> CSApiResponseForPaginatedListOrgReportTrip reports_get_organisation_trips(start_date, end_date, skip, take, user_ids, x_chronosheets_auth)

Reports on Organisation trips (GPS tracking from whole organisation).  Requires the 'ReportAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
skip = 56 # int | Skip this many items
take = 56 # int | Take this many items
user_ids = 'user_ids_example' # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Reports on Organisation trips (GPS tracking from whole organisation).  Requires the 'ReportAdmin' permission.
    api_response = api_instance.reports_get_organisation_trips(start_date, end_date, skip, take, user_ids, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get_organisation_trips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **skip** | **int**| Skip this many items | 
 **take** | **int**| Take this many items | 
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseForPaginatedListOrgReportTrip**](CSApiResponseForPaginatedListOrgReportTrip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get_raw_data_admin**
> CSApiResponseForPaginatedListRawReportItem reports_get_raw_data_admin(start_date, end_date, user_ids, sort, order, skip, take, x_chronosheets_auth)

Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.  Requires the 'ReportAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
user_ids = 'user_ids_example' # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string.
sort = 'sort_example' # str | Decide which column to sort on
order = 'order_example' # str | Decide which direction to sort the column
skip = 56 # int | Skip this many rows
take = 56 # int | Take this many rows
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get Timesheets Raw Data.  This data details each timesheet record.  These are the organisation wide timesheet records, with data from potentially all employees.  Requires the 'ReportAdmin' permission.
    api_response = api_instance.reports_get_raw_data_admin(start_date, end_date, user_ids, sort, order, skip, take, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get_raw_data_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | 
 **sort** | **str**| Decide which column to sort on | 
 **order** | **str**| Decide which direction to sort the column | 
 **skip** | **int**| Skip this many rows | 
 **take** | **int**| Take this many rows | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseForPaginatedListRawReportItem**](CSApiResponseForPaginatedListRawReportItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_project_costings_admin**
> CSApiResponseListProjectCostingReportItem reports_project_costings_admin(start_date, end_date, user_ids, x_chronosheets_auth)

Gets project cost estimations VS actual cost for date range and users.  Requires the 'ReportAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
user_ids = 'user_ids_example' # str | A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Gets project cost estimations VS actual cost for date range and users.  Requires the 'ReportAdmin' permission.
    api_response = api_instance.reports_project_costings_admin(start_date, end_date, user_ids, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_project_costings_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **user_ids** | **str**| A comma-separated list of user Ids, if you want to filter the report data to particular users.  If you want all, send a blank string. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListProjectCostingReportItem**](CSApiResponseListProjectCostingReportItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_user_jobs_over_time**
> CSApiResponseListJobSeriesReportItem reports_user_jobs_over_time(start_date, end_date, x_chronosheets_auth)

Timeseries jobs data for the logged in user.  Requires the 'ViewOwnReports' or 'SubmitTimesheets'.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ReportsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date for the date range.  Report data in the response is after this date
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date for the date range.  Report data in the response is before this date
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Timeseries jobs data for the logged in user.  Requires the 'ViewOwnReports' or 'SubmitTimesheets'.
    api_response = api_instance.reports_user_jobs_over_time(start_date, end_date, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_user_jobs_over_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The start date for the date range.  Report data in the response is after this date | 
 **end_date** | **datetime**| The end date for the date range.  Report data in the response is before this date | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListJobSeriesReportItem**](CSApiResponseListJobSeriesReportItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

