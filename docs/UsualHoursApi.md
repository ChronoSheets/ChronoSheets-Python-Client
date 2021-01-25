# ChronoSheetsAPI.UsualHoursApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usual_hours_get_usual_hours**](UsualHoursApi.md#usual_hours_get_usual_hours) | **GET** /UsualHours/GetUsualHours | Get usual hours (rostered hours) for an employee.  Requires the &#39;ManageOrganisationUsers&#39; permission.
[**usual_hours_set_usual_hours**](UsualHoursApi.md#usual_hours_set_usual_hours) | **PUT** /UsualHours/SetUsualHours | Set usual hours (rostered hours) for an employee.  Requires the &#39;ManageOrganisationUsers&#39; permission.


# **usual_hours_get_usual_hours**
> ApiResponseListUsualHoursDay usual_hours_get_usual_hours(user_id, x_chronosheets_auth)

Get usual hours (rostered hours) for an employee.  Requires the 'ManageOrganisationUsers' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import usual_hours_api
from ChronoSheetsAPI.model.api_response_list_usual_hours_day import ApiResponseListUsualHoursDay
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = usual_hours_api.UsualHoursApi(api_client)
    user_id = 1 # int | The ID of the User for which you want to get UsualHours for
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get usual hours (rostered hours) for an employee.  Requires the 'ManageOrganisationUsers' permission.
        api_response = api_instance.usual_hours_get_usual_hours(user_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling UsualHoursApi->usual_hours_get_usual_hours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the User for which you want to get UsualHours for |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseListUsualHoursDay**](ApiResponseListUsualHoursDay.md)

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

# **usual_hours_set_usual_hours**
> ApiResponseBoolean usual_hours_set_usual_hours(x_chronosheets_auth, request)

Set usual hours (rostered hours) for an employee.  Requires the 'ManageOrganisationUsers' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import usual_hours_api
from ChronoSheetsAPI.model.api_response_boolean import ApiResponseBoolean
from ChronoSheetsAPI.model.set_usual_hours_request import SetUsualHoursRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = usual_hours_api.UsualHoursApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = SetUsualHoursRequest(
        usual_hours_data=[
            UsualHoursDay(
                day_type="Monday",
                time_slots=[
                    TimeSlot(
                        day_type="Monday",
                        usual_hour_id=1,
                        start_hour=1,
                        start_minute=1,
                        end_hour=1,
                        end_minute=1,
                        is_valid=True,
                    ),
                ],
                delete_usual_hours=[
                    1,
                ],
            ),
        ],
        user_id=1,
    ) # SetUsualHoursRequest | A Set UsualHours Request object containing updated data.  Make sure to specify the Day types in the request object so that ChronoSheets knows which Days to update

    # example passing only required values which don't have defaults set
    try:
        # Set usual hours (rostered hours) for an employee.  Requires the 'ManageOrganisationUsers' permission.
        api_response = api_instance.usual_hours_set_usual_hours(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling UsualHoursApi->usual_hours_set_usual_hours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**SetUsualHoursRequest**](SetUsualHoursRequest.md)| A Set UsualHours Request object containing updated data.  Make sure to specify the Day types in the request object so that ChronoSheets knows which Days to update |

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

