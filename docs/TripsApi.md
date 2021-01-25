# ChronoSheetsAPI.TripsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trips_create_trip**](TripsApi.md#trips_create_trip) | **POST** /Trips/CreateTrip | Create a new trip.  Important: create a timesheet record before calling this, passing in the new timesheet record id as a reference.    Requires the &#39;SubmitTimesheets&#39; permission.
[**trips_get_my_trip_by_id**](TripsApi.md#trips_get_my_trip_by_id) | **GET** /Trips/GetMyTripById | Get trip by Id.    Requires the &#39;ViewMyTrips&#39; permission.
[**trips_get_my_trips**](TripsApi.md#trips_get_my_trips) | **GET** /Trips/GetMyTrips | Get my trips.  Get the GPS trips you&#39;ve recorded and submitted.    Requires the &#39;ViewMyTrips&#39; permission.


# **trips_create_trip**
> ApiResponseInt32 trips_create_trip(x_chronosheets_auth, request)

Create a new trip.  Important: create a timesheet record before calling this, passing in the new timesheet record id as a reference.    Requires the 'SubmitTimesheets' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import trips_api
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.create_trip_request import CreateTripRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = trips_api.TripsApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = CreateTripRequest(
        timesheet_id=1,
        vehicle_id=1,
        path_coords_string_csv="path_coords_string_csv_example",
        distance_meters=3.14,
        mobile_platform="Unknown",
    ) # CreateTripRequest | A Create Trip Request object containing values for the new Trip to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new trip.  Important: create a timesheet record before calling this, passing in the new timesheet record id as a reference.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.trips_create_trip(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TripsApi->trips_create_trip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**CreateTripRequest**](CreateTripRequest.md)| A Create Trip Request object containing values for the new Trip to create |

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

# **trips_get_my_trip_by_id**
> ApiResponseTrip trips_get_my_trip_by_id(trip_id, x_chronosheets_auth)

Get trip by Id.    Requires the 'ViewMyTrips' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import trips_api
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
    api_instance = trips_api.TripsApi(api_client)
    trip_id = 1 # int | The ID of the Trip you want to get
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get trip by Id.    Requires the 'ViewMyTrips' permission.
        api_response = api_instance.trips_get_my_trip_by_id(trip_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TripsApi->trips_get_my_trip_by_id: %s\n" % e)
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

# **trips_get_my_trips**
> ApiResponseForPaginatedListTrip trips_get_my_trips(start_date, end_date, x_chronosheets_auth)

Get my trips.  Get the GPS trips you've recorded and submitted.    Requires the 'ViewMyTrips' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import trips_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_trip import ApiResponseForPaginatedListTrip
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = trips_api.TripsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The Start date of the date range.  Trips after this date will be obtained.
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The End date of the date range.  Trips before this date will be obtained.
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many Trips (optional)
    take = 1 # int | Take this many Trips (optional)
    vehicle_id = 1 # int | Filter by a particular Vehicle (get trips made with a particular vehicle), specified by VehicleId (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get my trips.  Get the GPS trips you've recorded and submitted.    Requires the 'ViewMyTrips' permission.
        api_response = api_instance.trips_get_my_trips(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TripsApi->trips_get_my_trips: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get my trips.  Get the GPS trips you've recorded and submitted.    Requires the 'ViewMyTrips' permission.
        api_response = api_instance.trips_get_my_trips(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, vehicle_id=vehicle_id)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TripsApi->trips_get_my_trips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The Start date of the date range.  Trips after this date will be obtained. |
 **end_date** | **datetime**| The End date of the date range.  Trips before this date will be obtained. |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many Trips | [optional]
 **take** | **int**| Take this many Trips | [optional]
 **vehicle_id** | **int**| Filter by a particular Vehicle (get trips made with a particular vehicle), specified by VehicleId | [optional]

### Return type

[**ApiResponseForPaginatedListTrip**](ApiResponseForPaginatedListTrip.md)

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

