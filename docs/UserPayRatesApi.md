# ChronoSheetsAPI.UserPayRatesApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_pay_rates_create_pay_rate**](UserPayRatesApi.md#user_pay_rates_create_pay_rate) | **POST** /UserPayRates/CreatePayRate | Create a new pay rate for a particular user, archiving the previous pay rate.    Requires the &#39;ManageOrganisationUsers&#39; permission.
[**user_pay_rates_get_pay_rates**](UserPayRatesApi.md#user_pay_rates_get_pay_rates) | **GET** /UserPayRates/GetPayRates | Get a collection of pay rates for a particular user, specified by user id.    Requires the &#39;ManageOrganisationUsers&#39; permission.


# **user_pay_rates_create_pay_rate**
> CSApiResponseInt32 user_pay_rates_create_pay_rate(request, x_chronosheets_auth)

Create a new pay rate for a particular user, archiving the previous pay rate.    Requires the 'ManageOrganisationUsers' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UserPayRatesApi()
request = ChronoSheetsAPI.CSInsertUserHourlyRateRequest() # CSInsertUserHourlyRateRequest | An Insert UserHourlyRate Request object containing values for the new UserHourlyRate to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a new pay rate for a particular user, archiving the previous pay rate.    Requires the 'ManageOrganisationUsers' permission.
    api_response = api_instance.user_pay_rates_create_pay_rate(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPayRatesApi->user_pay_rates_create_pay_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertUserHourlyRateRequest**](CSInsertUserHourlyRateRequest.md)| An Insert UserHourlyRate Request object containing values for the new UserHourlyRate to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_pay_rates_get_pay_rates**
> CSApiResponseListUserHourlyRate user_pay_rates_get_pay_rates(user_id, x_chronosheets_auth)

Get a collection of pay rates for a particular user, specified by user id.    Requires the 'ManageOrganisationUsers' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UserPayRatesApi()
user_id = 56 # int | The ID of the User for which you want to get UserHourlyRate objects
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a collection of pay rates for a particular user, specified by user id.    Requires the 'ManageOrganisationUsers' permission.
    api_response = api_instance.user_pay_rates_get_pay_rates(user_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPayRatesApi->user_pay_rates_get_pay_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the User for which you want to get UserHourlyRate objects | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListUserHourlyRate**](CSApiResponseListUserHourlyRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

