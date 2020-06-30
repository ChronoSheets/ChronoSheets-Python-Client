# ChronoSheetsAPI.OrganisationApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_get_organisation**](OrganisationApi.md#organisation_get_organisation) | **GET** /Organisation/GetOrganisation | Get your organisation.    Requires &#39;OrganisationAdmin&#39; permission.
[**organisation_update_organisation**](OrganisationApi.md#organisation_update_organisation) | **PUT** /Organisation/UpdateOrganisation | Update an organisation.    Requires &#39;OrganisationAdmin&#39; permission.


# **organisation_get_organisation**
> CSApiResponseOrganisation organisation_get_organisation(x_chronosheets_auth)

Get your organisation.    Requires 'OrganisationAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get your organisation.    Requires 'OrganisationAdmin' permission.
    api_response = api_instance.organisation_get_organisation(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationApi->organisation_get_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseOrganisation**](CSApiResponseOrganisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_update_organisation**
> CSApiResponseUpdateOrganisationResponse organisation_update_organisation(request, x_chronosheets_auth)

Update an organisation.    Requires 'OrganisationAdmin' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationApi()
request = ChronoSheetsAPI.CSUpdateOrganisationRequest() # CSUpdateOrganisationRequest | An Update Organsation Request object containing updated fields.  Make sure to specify the Organsation Id in the request object so that ChronoSheets knows which Organsation to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update an organisation.    Requires 'OrganisationAdmin' permission.
    api_response = api_instance.organisation_update_organisation(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationApi->organisation_update_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSUpdateOrganisationRequest**](CSUpdateOrganisationRequest.md)| An Update Organsation Request object containing updated fields.  Make sure to specify the Organsation Id in the request object so that ChronoSheets knows which Organsation to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseUpdateOrganisationResponse**](CSApiResponseUpdateOrganisationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

