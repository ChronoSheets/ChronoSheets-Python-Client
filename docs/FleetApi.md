# ChronoSheetsAPI.FleetApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fleet_create_vehicle**](FleetApi.md#fleet_create_vehicle) | **POST** /api/Fleet/CreateVehicle | Create a vehicle.    Requires the &#39;ManageFleet&#39; permission.
[**fleet_delete_vehicle**](FleetApi.md#fleet_delete_vehicle) | **DELETE** /api/Fleet/DeleteVehicle | Delete a vehicle from the fleet.  Requires the &#39;ManageFleet&#39; permission.
[**fleet_get_vehicle_by_id**](FleetApi.md#fleet_get_vehicle_by_id) | **GET** /api/Fleet/GetVehicleById | Get a particular vehicle.  Does not require any special permission.
[**fleet_get_vehicles**](FleetApi.md#fleet_get_vehicles) | **GET** /api/Fleet/GetVehicles | Get a collection of vehicles that are under your organisation.    Does not require any special permission.
[**fleet_update_vehicle**](FleetApi.md#fleet_update_vehicle) | **PUT** /api/Fleet/UpdateVehicle | Update a vehicle.    Requires the &#39;ManageFleet&#39; permission.


# **fleet_create_vehicle**
> CSApiResponseInt32 fleet_create_vehicle(request, x_chronosheets_auth)

Create a vehicle.    Requires the 'ManageFleet' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
request = ChronoSheetsAPI.CSInsertVehicleRequest() # CSInsertVehicleRequest | An Insert Vehicle Request object containing values for the new Vehicle to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a vehicle.    Requires the 'ManageFleet' permission.
    api_response = api_instance.fleet_create_vehicle(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_create_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertVehicleRequest**](CSInsertVehicleRequest.md)| An Insert Vehicle Request object containing values for the new Vehicle to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fleet_delete_vehicle**
> CSApiResponseBoolean fleet_delete_vehicle(vehicle_id, x_chronosheets_auth)

Delete a vehicle from the fleet.  Requires the 'ManageFleet' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
vehicle_id = 56 # int | The unique ID of the vehicle you wish to delete
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Delete a vehicle from the fleet.  Requires the 'ManageFleet' permission.
    api_response = api_instance.fleet_delete_vehicle(vehicle_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_delete_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| The unique ID of the vehicle you wish to delete | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fleet_get_vehicle_by_id**
> CSApiResponseFleetVehicle fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth)

Get a particular vehicle.  Does not require any special permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
vehicle_id = 56 # int | The ID of the Vehicle you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a particular vehicle.  Does not require any special permission.
    api_response = api_instance.fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_get_vehicle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| The ID of the Vehicle you want to get | 
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
> CSApiResponseListFleetVehicle fleet_get_vehicles(x_chronosheets_auth, include_deleted=include_deleted)

Get a collection of vehicles that are under your organisation.    Does not require any special permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
include_deleted = true # bool | Whether or not to include deleted vehicles (optional)

try:
    # Get a collection of vehicles that are under your organisation.    Does not require any special permission.
    api_response = api_instance.fleet_get_vehicles(x_chronosheets_auth, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_get_vehicles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **include_deleted** | **bool**| Whether or not to include deleted vehicles | [optional] 

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

Update a vehicle.    Requires the 'ManageFleet' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.FleetApi()
request = ChronoSheetsAPI.CSSaveVehicleRequest() # CSSaveVehicleRequest | A Save Vehicle Request object containing updated fields.  Make sure to specify the Vehicle Id in the request object so that ChronoSheets knows which Vehicle to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a vehicle.    Requires the 'ManageFleet' permission.
    api_response = api_instance.fleet_update_vehicle(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FleetApi->fleet_update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSSaveVehicleRequest**](CSSaveVehicleRequest.md)| A Save Vehicle Request object containing updated fields.  Make sure to specify the Vehicle Id in the request object so that ChronoSheets knows which Vehicle to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

