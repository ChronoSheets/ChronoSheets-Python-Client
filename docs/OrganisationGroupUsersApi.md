# ChronoSheetsAPI.OrganisationGroupUsersApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_group_users_get_organisation_group_users**](OrganisationGroupUsersApi.md#organisation_group_users_get_organisation_group_users) | **GET** /api/OrganisationGroupUsers/GetOrganisationGroupUsers | Get a collection of organisation group users that belong to an organisation group.  Requires the &#39;ManageOrganisationGroups&#39; or &#39;ManageOrganisationUsers&#39; permissions.
[**organisation_group_users_update_organisation_group_users**](OrganisationGroupUsersApi.md#organisation_group_users_update_organisation_group_users) | **POST** /api/OrganisationGroupUsers/UpdateOrganisationGroupUsers | Set the users who belong to an organisation group


# **organisation_group_users_get_organisation_group_users**
> CSApiResponseListUserForManagement organisation_group_users_get_organisation_group_users(org_group_id, x_chronosheets_auth)

Get a collection of organisation group users that belong to an organisation group.  Requires the 'ManageOrganisationGroups' or 'ManageOrganisationUsers' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupUsersApi()
org_group_id = 56 # int | An OrganisatioGroup Id
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a collection of organisation group users that belong to an organisation group.  Requires the 'ManageOrganisationGroups' or 'ManageOrganisationUsers' permissions.
    api_response = api_instance.organisation_group_users_get_organisation_group_users(org_group_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupUsersApi->organisation_group_users_get_organisation_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_group_id** | **int**| An OrganisatioGroup Id | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListUserForManagement**](CSApiResponseListUserForManagement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_group_users_update_organisation_group_users**
> CSApiResponseBoolean organisation_group_users_update_organisation_group_users(request, x_chronosheets_auth)

Set the users who belong to an organisation group

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupUsersApi()
request = ChronoSheetsAPI.CSSetOrganisationGroupUsersRequest() # CSSetOrganisationGroupUsersRequest | A request object specifying which users belong to an organisation group.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Set the users who belong to an organisation group
    api_response = api_instance.organisation_group_users_update_organisation_group_users(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupUsersApi->organisation_group_users_update_organisation_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSSetOrganisationGroupUsersRequest**](CSSetOrganisationGroupUsersRequest.md)| A request object specifying which users belong to an organisation group.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

