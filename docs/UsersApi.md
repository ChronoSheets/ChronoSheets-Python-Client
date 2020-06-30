# ChronoSheetsAPI.UsersApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create_timesheet_user**](UsersApi.md#users_create_timesheet_user) | **POST** /Users/CreateTimesheetUser | Create a user account in your organisation.  Requires the &#39;ManageOrganisationUsers&#39; permission.
[**users_get_timesheet_user**](UsersApi.md#users_get_timesheet_user) | **GET** /Users/GetTimesheetUser | Get a particular user in your organisation.  Requires the &#39;ManageOrganisationUsers&#39; or &#39;ManageOrganisationGroups&#39; permissions.
[**users_get_timesheet_users**](UsersApi.md#users_get_timesheet_users) | **GET** /Users/GetTimesheetUsers | Get users accounts in your organisation.  Requires the &#39;ManageOrganisationUsers&#39; or &#39;ManageOrganisationGroups&#39; permissions.
[**users_update_timesheet_user**](UsersApi.md#users_update_timesheet_user) | **PUT** /Users/UpdateTimesheetUser | Update a user account.  Requires the &#39;ManageOrganisationUsers&#39; permission.


# **users_create_timesheet_user**
> CSApiResponseInsertUserResponse users_create_timesheet_user(request, x_chronosheets_auth)

Create a user account in your organisation.  Requires the 'ManageOrganisationUsers' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UsersApi()
request = ChronoSheetsAPI.CSInsertUserRequest() # CSInsertUserRequest | An Insert User Request object containing values for the new User to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a user account in your organisation.  Requires the 'ManageOrganisationUsers' permission.
    api_response = api_instance.users_create_timesheet_user(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_create_timesheet_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertUserRequest**](CSInsertUserRequest.md)| An Insert User Request object containing values for the new User to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInsertUserResponse**](CSApiResponseInsertUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_timesheet_user**
> CSApiResponseUserForManagement users_get_timesheet_user(user_id, x_chronosheets_auth)

Get a particular user in your organisation.  Requires the 'ManageOrganisationUsers' or 'ManageOrganisationGroups' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UsersApi()
user_id = 56 # int | The User ID of the UserForManagement you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a particular user in your organisation.  Requires the 'ManageOrganisationUsers' or 'ManageOrganisationGroups' permissions.
    api_response = api_instance.users_get_timesheet_user(user_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_timesheet_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The User ID of the UserForManagement you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseUserForManagement**](CSApiResponseUserForManagement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_timesheet_users**
> CSApiResponseListUserForManagement users_get_timesheet_users(x_chronosheets_auth)

Get users accounts in your organisation.  Requires the 'ManageOrganisationUsers' or 'ManageOrganisationGroups' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UsersApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get users accounts in your organisation.  Requires the 'ManageOrganisationUsers' or 'ManageOrganisationGroups' permissions.
    api_response = api_instance.users_get_timesheet_users(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_timesheet_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListUserForManagement**](CSApiResponseListUserForManagement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_timesheet_user**
> CSApiResponseUpdateUserResponse users_update_timesheet_user(request, x_chronosheets_auth)

Update a user account.  Requires the 'ManageOrganisationUsers' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.UsersApi()
request = ChronoSheetsAPI.CSUpdateUserRequest() # CSUpdateUserRequest | A Update User Request object containing updated fields.  Make sure to specify the User Id in the request object so that ChronoSheets knows which User to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a user account.  Requires the 'ManageOrganisationUsers' permission.
    api_response = api_instance.users_update_timesheet_user(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update_timesheet_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSUpdateUserRequest**](CSUpdateUserRequest.md)| A Update User Request object containing updated fields.  Make sure to specify the User Id in the request object so that ChronoSheets knows which User to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseUpdateUserResponse**](CSApiResponseUpdateUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

