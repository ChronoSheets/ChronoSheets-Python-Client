# ChronoSheetsAPI.FleetApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fleet_create_vehicle**](FleetApi.md#fleet_create_vehicle) | **POST** /Fleet/CreateVehicle | Create a vehicle.    Requires the &#39;ManageFleet&#39; permission.
[**fleet_delete_vehicle**](FleetApi.md#fleet_delete_vehicle) | **DELETE** /Fleet/DeleteVehicle | Delete a vehicle from the fleet.  Requires the &#39;ManageFleet&#39; permission.
[**fleet_get_vehicle_by_id**](FleetApi.md#fleet_get_vehicle_by_id) | **GET** /Fleet/GetVehicleById | Get a particular vehicle.  Does not require any special permission.
[**fleet_get_vehicles**](FleetApi.md#fleet_get_vehicles) | **GET** /Fleet/GetVehicles | Get a collection of vehicles that are under your organisation.    Does not require any special permission.
[**fleet_update_vehicle**](FleetApi.md#fleet_update_vehicle) | **PUT** /Fleet/UpdateVehicle | Update a vehicle.    Requires the &#39;ManageFleet&#39; permission.


# **fleet_create_vehicle**
> ApiResponseInt32 fleet_create_vehicle(x_chronosheets_auth, request)

Create a vehicle.    Requires the 'ManageFleet' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import fleet_api
from ChronoSheetsAPI.model.insert_vehicle_request import InsertVehicleRequest
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fleet_api.FleetApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = InsertVehicleRequest(
        name="name_example",
        cost_per_kilometer=3.14,
        make="make_example",
        model="model_example",
        year="year_example",
        licence_plate_number="licence_plate_number_example",
        linked_org_group_ids=[
            1,
        ],
    ) # InsertVehicleRequest | An Insert Vehicle Request object containing values for the new Vehicle to create

    # example passing only required values which don't have defaults set
    try:
        # Create a vehicle.    Requires the 'ManageFleet' permission.
        api_response = api_instance.fleet_create_vehicle(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FleetApi->fleet_create_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**InsertVehicleRequest**](InsertVehicleRequest.md)| An Insert Vehicle Request object containing values for the new Vehicle to create |

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

# **fleet_delete_vehicle**
> ApiResponseBoolean fleet_delete_vehicle(vehicle_id, x_chronosheets_auth)

Delete a vehicle from the fleet.  Requires the 'ManageFleet' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import fleet_api
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
    api_instance = fleet_api.FleetApi(api_client)
    vehicle_id = 1 # int | The unique ID of the vehicle you wish to delete
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Delete a vehicle from the fleet.  Requires the 'ManageFleet' permission.
        api_response = api_instance.fleet_delete_vehicle(vehicle_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FleetApi->fleet_delete_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| The unique ID of the vehicle you wish to delete |
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

# **fleet_get_vehicle_by_id**
> ApiResponseFleetVehicle fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth)

Get a particular vehicle.  Does not require any special permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import fleet_api
from ChronoSheetsAPI.model.api_response_fleet_vehicle import ApiResponseFleetVehicle
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fleet_api.FleetApi(api_client)
    vehicle_id = 1 # int | The ID of the Vehicle you want to get
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get a particular vehicle.  Does not require any special permission.
        api_response = api_instance.fleet_get_vehicle_by_id(vehicle_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FleetApi->fleet_get_vehicle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| The ID of the Vehicle you want to get |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseFleetVehicle**](ApiResponseFleetVehicle.md)

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

# **fleet_get_vehicles**
> ApiResponseListFleetVehicle fleet_get_vehicles(x_chronosheets_auth)

Get a collection of vehicles that are under your organisation.    Does not require any special permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import fleet_api
from ChronoSheetsAPI.model.api_response_list_fleet_vehicle import ApiResponseListFleetVehicle
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fleet_api.FleetApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    include_deleted = True # bool | Whether or not to include deleted vehicles (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a collection of vehicles that are under your organisation.    Does not require any special permission.
        api_response = api_instance.fleet_get_vehicles(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FleetApi->fleet_get_vehicles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a collection of vehicles that are under your organisation.    Does not require any special permission.
        api_response = api_instance.fleet_get_vehicles(x_chronosheets_auth, include_deleted=include_deleted)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FleetApi->fleet_get_vehicles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **include_deleted** | **bool**| Whether or not to include deleted vehicles | [optional]

### Return type

[**ApiResponseListFleetVehicle**](ApiResponseListFleetVehicle.md)

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

# **fleet_update_vehicle**
> ApiResponseBoolean fleet_update_vehicle(x_chronosheets_auth, request)

Update a vehicle.    Requires the 'ManageFleet' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import fleet_api
from ChronoSheetsAPI.model.api_response_boolean import ApiResponseBoolean
from ChronoSheetsAPI.model.save_vehicle_request import SaveVehicleRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fleet_api.FleetApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = SaveVehicleRequest(
        id=1,
        name="name_example",
        cost_per_kilometer=3.14,
        make="make_example",
        model="model_example",
        year="year_example",
        licence_plate_number="licence_plate_number_example",
        linked_org_group_ids=[
            1,
        ],
        is_deleted=True,
    ) # SaveVehicleRequest | A Save Vehicle Request object containing updated fields.  Make sure to specify the Vehicle Id in the request object so that ChronoSheets knows which Vehicle to update

    # example passing only required values which don't have defaults set
    try:
        # Update a vehicle.    Requires the 'ManageFleet' permission.
        api_response = api_instance.fleet_update_vehicle(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling FleetApi->fleet_update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**SaveVehicleRequest**](SaveVehicleRequest.md)| A Save Vehicle Request object containing updated fields.  Make sure to specify the Vehicle Id in the request object so that ChronoSheets knows which Vehicle to update |

### Return type

[**ApiResponseBoolean**](ApiResponseBoolean.md)

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

