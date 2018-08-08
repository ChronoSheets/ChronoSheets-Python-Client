# ChronoSheetsAPI.AggregateClientProjectsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_client_projects_get_aggregate_client_projects**](AggregateClientProjectsApi.md#aggregate_client_projects_get_aggregate_client_projects) | **GET** /api/AggregateClientProjects/GetAggregateClientProjects | Get client and project information, aggregated.    Requires the &#39;SubmitTimesheets&#39; or &#39;ManageClientsAndProjects&#39; permissions.


# **aggregate_client_projects_get_aggregate_client_projects**
> CSApiResponseListAggregateClient aggregate_client_projects_get_aggregate_client_projects(x_chronosheets_auth)

Get client and project information, aggregated.    Requires the 'SubmitTimesheets' or 'ManageClientsAndProjects' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.AggregateClientProjectsApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get client and project information, aggregated.    Requires the 'SubmitTimesheets' or 'ManageClientsAndProjects' permissions.
    api_response = api_instance.aggregate_client_projects_get_aggregate_client_projects(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregateClientProjectsApi->aggregate_client_projects_get_aggregate_client_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListAggregateClient**](CSApiResponseListAggregateClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
