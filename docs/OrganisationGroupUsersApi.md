# ChronoSheetsAPI.OrganisationGroupUsersApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_group_users_get_organisation_group_users**](OrganisationGroupUsersApi.md#organisation_group_users_get_organisation_group_users) | **GET** /OrganisationGroupUsers/GetOrganisationGroupUsers | Get a collection of organisation group users that belong to an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; or &#39;ManageOrganisationUsers&#39; permissions.
[**organisation_group_users_update_organisation_group_users**](OrganisationGroupUsersApi.md#organisation_group_users_update_organisation_group_users) | **PUT** /OrganisationGroupUsers/UpdateOrganisationGroupUsers | Set the users who belong to an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.


# **organisation_group_users_get_organisation_group_users**
> ApiResponseListUserForManagement organisation_group_users_get_organisation_group_users(org_group_id, x_chronosheets_auth)

Get a collection of organisation group users that belong to an organisation group.    Requires the 'ManageOrganisationGroups' or 'ManageOrganisationUsers' permissions.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import organisation_group_users_api
from ChronoSheetsAPI.model.api_response_list_user_for_management import ApiResponseListUserForManagement
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organisation_group_users_api.OrganisationGroupUsersApi(api_client)
    org_group_id = 1 # int | An OrganisationGroup Id
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get a collection of organisation group users that belong to an organisation group.    Requires the 'ManageOrganisationGroups' or 'ManageOrganisationUsers' permissions.
        api_response = api_instance.organisation_group_users_get_organisation_group_users(org_group_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling OrganisationGroupUsersApi->organisation_group_users_get_organisation_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_group_id** | **int**| An OrganisationGroup Id |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseListUserForManagement**](ApiResponseListUserForManagement.md)

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

# **organisation_group_users_update_organisation_group_users**
> ApiResponseBoolean organisation_group_users_update_organisation_group_users(x_chronosheets_auth, request)

Set the users who belong to an organisation group.    Requires the 'ManageOrganisationGroups' permissions.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import organisation_group_users_api
from ChronoSheetsAPI.model.set_organisation_group_users_request import SetOrganisationGroupUsersRequest
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
    api_instance = organisation_group_users_api.OrganisationGroupUsersApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = SetOrganisationGroupUsersRequest(
        organisation_group_id=1,
        csv_user_ids="csv_user_ids_example",
    ) # SetOrganisationGroupUsersRequest | A request object specifying which users belong to an organisation group.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update. CsvUserIds is a comma separated list of User Ids, e.g. 1,2,3,4

    # example passing only required values which don't have defaults set
    try:
        # Set the users who belong to an organisation group.    Requires the 'ManageOrganisationGroups' permissions.
        api_response = api_instance.organisation_group_users_update_organisation_group_users(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling OrganisationGroupUsersApi->organisation_group_users_update_organisation_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **request** | [**SetOrganisationGroupUsersRequest**](SetOrganisationGroupUsersRequest.md)| A request object specifying which users belong to an organisation group.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update. CsvUserIds is a comma separated list of User Ids, e.g. 1,2,3,4 |

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

