# ChronoSheetsAPI.GeoFencingApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geo_fencing_create_geofence**](GeoFencingApi.md#geo_fencing_create_geofence) | **POST** /GeoFencing/CreateGeofence | Create a geofencing with rules to be used for clock on/off automation.  Requires the &#39;ManageGeofencing&#39; permission.
[**geo_fencing_delete_geofence**](GeoFencingApi.md#geo_fencing_delete_geofence) | **DELETE** /GeoFencing/DeleteGeofence | Deletes a geofence.  Requires the &#39;ManageGeofencing&#39; permission.
[**geo_fencing_get_geofence_by_id**](GeoFencingApi.md#geo_fencing_get_geofence_by_id) | **GET** /GeoFencing/GetGeofenceById | Get a geofence by ID  Requires the &#39;SubmitTimesheets&#39; permission.
[**geo_fencing_get_geofences**](GeoFencingApi.md#geo_fencing_get_geofences) | **GET** /GeoFencing/GetGeofences | Get geofences belonging to your organisation  Requires the &#39;SubmitTimesheets&#39; permission.
[**geo_fencing_update_geofence**](GeoFencingApi.md#geo_fencing_update_geofence) | **PUT** /GeoFencing/UpdateGeofence | Updates a geofencing with rules to be used for clock on/off automation.  Requires the &#39;ManageGeofencing&#39; permission.


# **geo_fencing_create_geofence**
> CSApiResponseInt32 geo_fencing_create_geofence(request, x_chronosheets_auth)

Create a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.GeoFencingApi()
request = ChronoSheetsAPI.CSCreateGeoFenceRequest() # CSCreateGeoFenceRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.
    api_response = api_instance.geo_fencing_create_geofence(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoFencingApi->geo_fencing_create_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSCreateGeoFenceRequest**](CSCreateGeoFenceRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_fencing_delete_geofence**
> CSApiResponseGeofence geo_fencing_delete_geofence(geofence_id, x_chronosheets_auth)

Deletes a geofence.  Requires the 'ManageGeofencing' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.GeoFencingApi()
geofence_id = 56 # int | Specify the geofence you want to delete with the geofence ID.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Deletes a geofence.  Requires the 'ManageGeofencing' permission.
    api_response = api_instance.geo_fencing_delete_geofence(geofence_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoFencingApi->geo_fencing_delete_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **int**| Specify the geofence you want to delete with the geofence ID. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseGeofence**](CSApiResponseGeofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_fencing_get_geofence_by_id**
> CSApiResponseGeofence geo_fencing_get_geofence_by_id(geofence_id, x_chronosheets_auth)

Get a geofence by ID  Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.GeoFencingApi()
geofence_id = 56 # int | The ID of the geofence you want to obtain
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a geofence by ID  Requires the 'SubmitTimesheets' permission.
    api_response = api_instance.geo_fencing_get_geofence_by_id(geofence_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoFencingApi->geo_fencing_get_geofence_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **int**| The ID of the geofence you want to obtain | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseGeofence**](CSApiResponseGeofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_fencing_get_geofences**
> CSApiResponseForPaginatedListExtendedGeofence geo_fencing_get_geofences(x_chronosheets_auth, skip=skip, take=take)

Get geofences belonging to your organisation  Requires the 'SubmitTimesheets' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.GeoFencingApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
skip = 56 # int | Number of records to skip (optional)
take = 56 # int | Number of records to take (optional)

try:
    # Get geofences belonging to your organisation  Requires the 'SubmitTimesheets' permission.
    api_response = api_instance.geo_fencing_get_geofences(x_chronosheets_auth, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoFencingApi->geo_fencing_get_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **skip** | **int**| Number of records to skip | [optional] 
 **take** | **int**| Number of records to take | [optional] 

### Return type

[**CSApiResponseForPaginatedListExtendedGeofence**](CSApiResponseForPaginatedListExtendedGeofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_fencing_update_geofence**
> CSApiResponseInt32 geo_fencing_update_geofence(request, x_chronosheets_auth)

Updates a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.GeoFencingApi()
request = ChronoSheetsAPI.CSUpdateGeoFenceRequest() # CSUpdateGeoFenceRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Updates a geofencing with rules to be used for clock on/off automation.  Requires the 'ManageGeofencing' permission.
    api_response = api_instance.geo_fencing_update_geofence(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoFencingApi->geo_fencing_update_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSUpdateGeoFenceRequest**](CSUpdateGeoFenceRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

