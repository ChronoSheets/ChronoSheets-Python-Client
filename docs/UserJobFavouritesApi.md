# ChronoSheetsAPI.UserJobFavouritesApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_job_favourites_create_job_favourite**](UserJobFavouritesApi.md#user_job_favourites_create_job_favourite) | **PUT** /api/UserJobFavourites/CreateJobFavourite | Create a job favourite
[**user_job_favourites_delete_job_favourite**](UserJobFavouritesApi.md#user_job_favourites_delete_job_favourite) | **DELETE** /api/UserJobFavourites/DeleteJobFavourite | Delete a job favourite
[**user_job_favourites_get_job_favourites**](UserJobFavouritesApi.md#user_job_favourites_get_job_favourites) | **GET** /api/UserJobFavourites/GetJobFavourites | Get your job favourites


# **user_job_favourites_create_job_favourite**
> CSApiResponseInt32 user_job_favourites_create_job_favourite(request, x_chronosheets_auth)

Create a job favourite

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UserJobFavouritesApi()
request = ChronoSheetsAPI.CSInsertUserJobFavouriteRequest() # CSInsertUserJobFavouriteRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a job favourite
    api_response = api_instance.user_job_favourites_create_job_favourite(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserJobFavouritesApi->user_job_favourites_create_job_favourite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertUserJobFavouriteRequest**](CSInsertUserJobFavouriteRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_job_favourites_delete_job_favourite**
> CSApiResponseBoolean user_job_favourites_delete_job_favourite(job_id, x_chronosheets_auth)

Delete a job favourite

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UserJobFavouritesApi()
job_id = 56 # int | The ID of the Job
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Delete a job favourite
    api_response = api_instance.user_job_favourites_delete_job_favourite(job_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserJobFavouritesApi->user_job_favourites_delete_job_favourite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| The ID of the Job | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_job_favourites_get_job_favourites**
> CSApiResponseListUserJobFavourite user_job_favourites_get_job_favourites(x_chronosheets_auth)

Get your job favourites

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UserJobFavouritesApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get your job favourites
    api_response = api_instance.user_job_favourites_get_job_favourites(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserJobFavouritesApi->user_job_favourites_get_job_favourites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListUserJobFavourite**](CSApiResponseListUserJobFavourite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

