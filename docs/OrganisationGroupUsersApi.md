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
    api_instance = ChronoSheetsAPI.OrganisationGroupUsersApi(api_client)
    org_group_id = 56 # int | An OrganisationGroup Id
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get a collection of organisation group users that belong to an organisation group.    Requires the 'ManageOrganisationGroups' or 'ManageOrganisationUsers' permissions.
        api_response = api_instance.organisation_group_users_get_organisation_group_users(org_group_id, x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = ChronoSheetsAPI.OrganisationGroupUsersApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.SetOrganisationGroupUsersRequest() # SetOrganisationGroupUsersRequest | A request object specifying which users belong to an organisation group.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update. CsvUserIds is a comma separated list of User Ids, e.g. 1,2,3,4

    try:
        # Set the users who belong to an organisation group.    Requires the 'ManageOrganisationGroups' permissions.
        api_response = api_instance.organisation_group_users_update_organisation_group_users(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
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

