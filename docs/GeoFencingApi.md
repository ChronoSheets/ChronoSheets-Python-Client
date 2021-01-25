# ChronoSheetsAPI.GeoFencingApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geo_fencing_create_geofence**](GeoFencingApi.md#geo_fencing_create_geofence) | **POST** /GeoFencing/CreateGeofence | Create a geofencing with rules to be used for clock on/off automation.  Requires the &#39;ManageGeofencing&#39; permission.
[**geo_fencing_delete_geofence**](GeoFencingApi.md#geo_fencing_delete_geofence) | **DELETE** /GeoFencing/DeleteGeofence | Deletes a geofence.  Requires the &#39;ManageGeofencing&#39; permission.
[**geo_fencing_get_geofence_by_id**](GeoFencingApi.md#geo_fencing_get_geofence_by_id) | **GET** /GeoFencing/GetGeofenceById | Get a geofence by ID  Requires the &#39;SubmitTimesheets&#39; permission.
[**geo_fencing_get_geofences**](GeoFencingApi.md#geo_fencing_get_geofences) | **GET** /GeoFencing/GetGeofences | Get geofences belonging to your organisation  Requires the &#39;SubmitTimesheets&#39; permission.
[**geo_fencing_get_geofences_basic_info**](GeoFencingApi.md#geo_fencing_get_geofences_basic_info) | **GET** /GeoFencing/GetGeofencesBasicInfo | Gets a list of all geofences in your organisation, including just the name and ID.
[**geo_fencing_update_geofence**](GeoFencingApi.md#geo_fencing_update_geofence) | **PUT** /GeoFencing/UpdateGeofence | Updates a geofencing with rules to be used for clock on/off automation.  Requires the &#39;ManageGeofencing&#39; permission.


# **geo_fencing_create_geofence**
> ApiResponseInt32 geo_fencing_create_geofence(x_chronosheets_auth, request)

Create a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import geo_fencing_api
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.create_geo_fence_request import CreateGeoFenceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_fencing_api.GeoFencingApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = CreateGeoFenceRequest(
        name="name_example",
        fence_coordinates=[
            BasicCoordinate(
                latitude=3.14,
                longitude=3.14,
            ),
        ],
        trigger_job_code_id=1,
        trigger_task_id=1,
        send_alert_to_org_group_id=1,
        alert_settings="None",
        trigger_settings="None",
        start_time_hour=1,
        start_time_minute=1,
        end_time_hour=1,
        end_time_minute=1,
    ) # CreateGeoFenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.
        api_response = api_instance.geo_fencing_create_geofence(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_create_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**CreateGeoFenceRequest**](CreateGeoFenceRequest.md)|  |

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

# **geo_fencing_delete_geofence**
> ApiResponseGeofence geo_fencing_delete_geofence(geofence_id, x_chronosheets_auth)

Deletes a geofence.  Requires the 'ManageGeofencing' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import geo_fencing_api
from ChronoSheetsAPI.model.api_response_geofence import ApiResponseGeofence
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_fencing_api.GeoFencingApi(api_client)
    geofence_id = 1 # int | Specify the geofence you want to delete with the geofence ID.
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Deletes a geofence.  Requires the 'ManageGeofencing' permission.
        api_response = api_instance.geo_fencing_delete_geofence(geofence_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_delete_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **int**| Specify the geofence you want to delete with the geofence ID. |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseGeofence**](ApiResponseGeofence.md)

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

# **geo_fencing_get_geofence_by_id**
> ApiResponseGeofence geo_fencing_get_geofence_by_id(geofence_id, x_chronosheets_auth)

Get a geofence by ID  Requires the 'SubmitTimesheets' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import geo_fencing_api
from ChronoSheetsAPI.model.api_response_geofence import ApiResponseGeofence
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_fencing_api.GeoFencingApi(api_client)
    geofence_id = 1 # int | The ID of the geofence you want to obtain
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get a geofence by ID  Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.geo_fencing_get_geofence_by_id(geofence_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_get_geofence_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **int**| The ID of the geofence you want to obtain |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseGeofence**](ApiResponseGeofence.md)

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

# **geo_fencing_get_geofences**
> ApiResponseForPaginatedListExtendedGeofence geo_fencing_get_geofences(x_chronosheets_auth)

Get geofences belonging to your organisation  Requires the 'SubmitTimesheets' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import geo_fencing_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_extended_geofence import ApiResponseForPaginatedListExtendedGeofence
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_fencing_api.GeoFencingApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Number of records to skip (optional)
    take = 1 # int | Number of records to take (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get geofences belonging to your organisation  Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.geo_fencing_get_geofences(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_get_geofences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get geofences belonging to your organisation  Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.geo_fencing_get_geofences(x_chronosheets_auth, skip=skip, take=take)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_get_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Number of records to skip | [optional]
 **take** | **int**| Number of records to take | [optional]

### Return type

[**ApiResponseForPaginatedListExtendedGeofence**](ApiResponseForPaginatedListExtendedGeofence.md)

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

# **geo_fencing_get_geofences_basic_info**
> ApiResponseForPaginatedListBasicGeofence geo_fencing_get_geofences_basic_info(x_chronosheets_auth)

Gets a list of all geofences in your organisation, including just the name and ID.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import geo_fencing_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_basic_geofence import ApiResponseForPaginatedListBasicGeofence
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_fencing_api.GeoFencingApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of all geofences in your organisation, including just the name and ID.
        api_response = api_instance.geo_fencing_get_geofences_basic_info(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_get_geofences_basic_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseForPaginatedListBasicGeofence**](ApiResponseForPaginatedListBasicGeofence.md)

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

# **geo_fencing_update_geofence**
> ApiResponseInt32 geo_fencing_update_geofence(x_chronosheets_auth, request)

Updates a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import geo_fencing_api
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.update_geo_fence_request import UpdateGeoFenceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = geo_fencing_api.GeoFencingApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = UpdateGeoFenceRequest(
        geofence_id=1,
        name="name_example",
        fence_coordinates=[
            BasicCoordinate(
                latitude=3.14,
                longitude=3.14,
            ),
        ],
        trigger_job_code_id=1,
        trigger_task_id=1,
        send_alert_to_org_group_id=1,
        alert_settings="None",
        trigger_settings="None",
        start_time_hour=1,
        start_time_minute=1,
        end_time_hour=1,
        end_time_minute=1,
    ) # UpdateGeoFenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.
        api_response = api_instance.geo_fencing_update_geofence(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling GeoFencingApi->geo_fencing_update_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**UpdateGeoFenceRequest**](UpdateGeoFenceRequest.md)|  |

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

