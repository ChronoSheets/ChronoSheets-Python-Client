# ChronoSheetsAPI.UserJobFavouritesApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_job_favourites_create_job_favourite**](UserJobFavouritesApi.md#user_job_favourites_create_job_favourite) | **POST** /UserJobFavourites/CreateJobFavourite | Create a job favourite.    Requires the &#39;SubmitTimesheets&#39; permission.
[**user_job_favourites_delete_job_favourite**](UserJobFavouritesApi.md#user_job_favourites_delete_job_favourite) | **DELETE** /UserJobFavourites/DeleteJobFavourite | Delete a job favourite.    Requires the &#39;SubmitTimesheets&#39; permission.
[**user_job_favourites_get_job_favourites**](UserJobFavouritesApi.md#user_job_favourites_get_job_favourites) | **GET** /UserJobFavourites/GetJobFavourites | Get your job favourites.    Requires the &#39;SubmitTimesheets&#39; permission.


# **user_job_favourites_create_job_favourite**
> ApiResponseInt32 user_job_favourites_create_job_favourite(x_chronosheets_auth, request)

Create a job favourite.    Requires the 'SubmitTimesheets' permission.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.UserJobFavouritesApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.InsertUserJobFavouriteRequest() # InsertUserJobFavouriteRequest | An Insert UserJobFavourite Request object containing values for the new UserJobFavourite to create

    try:
        # Create a job favourite.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.user_job_favourites_create_job_favourite(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserJobFavouritesApi->user_job_favourites_create_job_favourite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **request** | [**InsertUserJobFavouriteRequest**](InsertUserJobFavouriteRequest.md)| An Insert UserJobFavourite Request object containing values for the new UserJobFavourite to create | 

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

# **user_job_favourites_delete_job_favourite**
> ApiResponseBoolean user_job_favourites_delete_job_favourite(job_id, x_chronosheets_auth)

Delete a job favourite.    Requires the 'SubmitTimesheets' permission.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.UserJobFavouritesApi(api_client)
    job_id = 56 # int | The ID of the Job for the Job Favourite you want to delete.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Delete a job favourite.    Requires the 'SubmitTimesheets' permission.
        api_response = api_instance.user_job_favourites_delete_job_favourite(job_id, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserJobFavouritesApi->user_job_favourites_delete_job_favourite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| The ID of the Job for the Job Favourite you want to delete. | 
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

# **user_job_favourites_get_job_favourites**
> ApiResponseListUserJobFavourite user_job_favourites_get_job_favourites(x_chronosheets_auth)

Get your job favourites.    Requires the 'SubmitTimesheets' permission.

### Example

```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ChronoSheetsAPI.UserJobFavouritesApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get your job favourites.    Requires the 'SubmitTimesheets' permission.
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

[**ApiResponseListUserJobFavourite**](ApiResponseListUserJobFavourite.md)

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

