# ChronoSheetsAPI.FleetApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fleet_create_vehicle**](FleetApi.md#fleet_create_vehicle) | **PUT** /api/Fleet/CreateVehicle | Create a vehicle
[**fleet_get_vehicle_by_id**](FleetApi.md#fleet_get_vehicle_by_id) | **GET** /api/Fleet/GetVehicleById | Get a particular vehicle
[**fleet_get_vehicles**](FleetApi.md#fleet_get_vehicles) | **GET** /api/Fleet/GetVehicles | Get a collection of vehicles that are under your organisation
[**fleet_update_vehicle**](FleetApi.md#fleet_update_vehicle) | **POST** /api/Fleet/UpdateVehicle | Update a vehicle


# **fleet_create_vehicle**
> CSApiResponseInt32 fleet_create_vehicle(request, x_chronosheets_auth)

Create a vehicle

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
request = ChronoSheetsAPI.CSInsertVehicleRequest() # CSInsertVehicleRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a vehicle
    api_response = api_instance.fleet_create_vehicle(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_create_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertVehicleRequest**](CSInsertVehicleRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fleet_get_vehicle_by_id**
> CSApiResponseFleetVehicle fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth)

Get a particular vehicle

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
vehicle_id = 56 # int | The ID of the vehicle you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a particular vehicle
    api_response = api_instance.fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_get_vehicle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| The ID of the vehicle you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseFleetVehicle**](CSApiResponseFleetVehicle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fleet_get_vehicles**
> CSApiResponseListFleetVehicle fleet_get_vehicles(include_deleted, x_chronosheets_auth)

Get a collection of vehicles that are under your organisation

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
include_deleted = true # bool | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a collection of vehicles that are under your organisation
    api_response = api_instance.fleet_get_vehicles(include_deleted, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_get_vehicles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListFleetVehicle**](CSApiResponseListFleetVehicle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fleet_update_vehicle**
> CSApiResponseBoolean fleet_update_vehicle(request, x_chronosheets_auth)

Update a vehicle

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
request = ChronoSheetsAPI.CSSaveVehicleRequest() # CSSaveVehicleRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a vehicle
    api_response = api_instance.fleet_update_vehicle(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSSaveVehicleRequest**](CSSaveVehicleRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

