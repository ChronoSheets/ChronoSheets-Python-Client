# ChronoSheetsAPI.OrganisationApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_get_organisation**](OrganisationApi.md#organisation_get_organisation) | **GET** /Organisation/GetOrganisation | Get your organisation.    Requires &#39;OrganisationAdmin&#39; permission.
[**organisation_update_organisation**](OrganisationApi.md#organisation_update_organisation) | **PUT** /Organisation/UpdateOrganisation | Update an organisation.    Requires &#39;OrganisationAdmin&#39; permission.


# **organisation_get_organisation**
> ApiResponseOrganisation organisation_get_organisation(x_chronosheets_auth)

Get your organisation.    Requires 'OrganisationAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import organisation_api
from ChronoSheetsAPI.model.api_response_organisation import ApiResponseOrganisation
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get your organisation.    Requires 'OrganisationAdmin' permission.
        api_response = api_instance.organisation_get_organisation(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling OrganisationApi->organisation_get_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseOrganisation**](ApiResponseOrganisation.md)

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

# **organisation_update_organisation**
> ApiResponseUpdateOrganisationResponse organisation_update_organisation(x_chronosheets_auth, request)

Update an organisation.    Requires 'OrganisationAdmin' permission.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import organisation_api
from ChronoSheetsAPI.model.api_response_update_organisation_response import ApiResponseUpdateOrganisationResponse
from ChronoSheetsAPI.model.update_organisation_request import UpdateOrganisationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_api.OrganisationApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = UpdateOrganisationRequest(
        organsation_id=1,
        organisation_name="organisation_name_example",
        address_line01="address_line01_example",
        address_line02="address_line02_example",
        organisation_suburb="organisation_suburb_example",
        organisation_state="organisation_state_example",
        organisation_postcode="organisation_postcode_example",
        organisation_country="organisation_country_example",
        organisation_phone="organisation_phone_example",
        organisation_email_address="organisation_email_address_example",
    ) # UpdateOrganisationRequest | An Update Organsation Request object containing updated fields.  Make sure to specify the Organsation Id in the request object so that ChronoSheets knows which Organsation to update

    # example passing only required values which don't have defaults set
    try:
        # Update an organisation.    Requires 'OrganisationAdmin' permission.
        api_response = api_instance.organisation_update_organisation(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling OrganisationApi->organisation_update_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**UpdateOrganisationRequest**](UpdateOrganisationRequest.md)| An Update Organsation Request object containing updated fields.  Make sure to specify the Organsation Id in the request object so that ChronoSheets knows which Organsation to update |

### Return type

[**ApiResponseUpdateOrganisationResponse**](ApiResponseUpdateOrganisationResponse.md)

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

