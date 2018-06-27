# ChronoSheetsAPI.TripsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trips_create_trip**](TripsApi.md#trips_create_trip) | **POST** /api/Trips/CreateTrip | Create a new trip.  Important: create a timesheet record before calling this, passing in the new timesheet record id as a reference.
[**trips_get_my_trip_by_id**](TripsApi.md#trips_get_my_trip_by_id) | **GET** /api/Trips/GetMyTripById | Get trip by Id
[**trips_get_my_trips**](TripsApi.md#trips_get_my_trips) | **GET** /api/Trips/GetMyTrips | Get my trips


# **trips_create_trip**
> CSApiResponseInt32 trips_create_trip(request, x_chronosheets_auth)

Create a new trip.  Important: create a timesheet record before calling this, passing in the new timesheet record id as a reference.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TripsApi()
request = ChronoSheetsAPI.CSCreateTripRequest() # CSCreateTripRequest | The create trip request
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a new trip.  Important: create a timesheet record before calling this, passing in the new timesheet record id as a reference.
    api_response = api_instance.trips_create_trip(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripsApi->trips_create_trip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSCreateTripRequest**](CSCreateTripRequest.md)| The create trip request | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trips_get_my_trip_by_id**
> CSApiResponseTrip trips_get_my_trip_by_id(trip_id, x_chronosheets_auth)

Get trip by Id

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TripsApi()
trip_id = 56 # int | The ID of the trip
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get trip by Id
    api_response = api_instance.trips_get_my_trip_by_id(trip_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripsApi->trips_get_my_trip_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_id** | **int**| The ID of the trip | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseTrip**](CSApiResponseTrip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trips_get_my_trips**
> CSApiResponseForPaginatedListTrip trips_get_my_trips(start_date, end_date, skip, take, vehicle_id, x_chronosheets_auth)

Get my trips

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TripsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
skip = 56 # int | 
take = 56 # int | 
vehicle_id = 56 # int | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get my trips
    api_response = api_instance.trips_get_my_trips(start_date, end_date, skip, take, vehicle_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripsApi->trips_get_my_trips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 
 **skip** | **int**|  | 
 **take** | **int**|  | 
 **vehicle_id** | **int**|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseForPaginatedListTrip**](CSApiResponseForPaginatedListTrip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

