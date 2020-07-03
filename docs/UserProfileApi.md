# ChronoSheetsAPI.UserProfileApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_profile_do_login**](UserProfileApi.md#user_profile_do_login) | **PUT** /UserProfile/DoLogin | Login to your ChronoSheets account and obtain an Auth Token which you can use for other ChronoSheets API methods.    Does not require any special permissions.
[**user_profile_do_logout**](UserProfileApi.md#user_profile_do_logout) | **DELETE** /UserProfile/DoLogout | Logout of your ChronoSheets account.  This method ends and deletes your active session.    Does not require any special permissions.
[**user_profile_get_my_profile**](UserProfileApi.md#user_profile_get_my_profile) | **GET** /UserProfile/GetMyProfile | Get your own profile.  Use this method to obtain detailed information about your ChronoSheets user profile.    Does not require any special permissions.
[**user_profile_keep_session_alive**](UserProfileApi.md#user_profile_keep_session_alive) | **GET** /UserProfile/KeepSessionAlive | Keep a session alive.  Use this method to keep a session active.  You could use this to &#39;ping&#39; ChronoSheets every &#39;x&#39; minutes to make sure your Auth Token will keep working.    Does not require any special permissions.
[**user_profile_update_my_profile**](UserProfileApi.md#user_profile_update_my_profile) | **PUT** /UserProfile/UpdateMyProfile | Update your own profile.  Use this method to update your profile information or update/change your password.    Does not require any special permissions.


# **user_profile_do_login**
> ApiResponseDoLoginResponse user_profile_do_login(request)

Login to your ChronoSheets account and obtain an Auth Token which you can use for other ChronoSheets API methods.    Does not require any special permissions.

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
    api_instance = ChronoSheetsAPI.UserProfileApi(api_client)
    request = ChronoSheetsAPI.DoLoginRequest() # DoLoginRequest | A request object containing your username/email and password.

    try:
        # Login to your ChronoSheets account and obtain an Auth Token which you can use for other ChronoSheets API methods.    Does not require any special permissions.
        api_response = api_instance.user_profile_do_login(request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileApi->user_profile_do_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DoLoginRequest**](DoLoginRequest.md)| A request object containing your username/email and password. | 

### Return type

[**ApiResponseDoLoginResponse**](ApiResponseDoLoginResponse.md)

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

# **user_profile_do_logout**
> ApiResponseBoolean user_profile_do_logout(x_chronosheets_auth)

Logout of your ChronoSheets account.  This method ends and deletes your active session.    Does not require any special permissions.

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
    api_instance = ChronoSheetsAPI.UserProfileApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Logout of your ChronoSheets account.  This method ends and deletes your active session.    Does not require any special permissions.
        api_response = api_instance.user_profile_do_logout(x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileApi->user_profile_do_logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **user_profile_get_my_profile**
> ApiResponseUserProfile user_profile_get_my_profile(x_chronosheets_auth)

Get your own profile.  Use this method to obtain detailed information about your ChronoSheets user profile.    Does not require any special permissions.

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
    api_instance = ChronoSheetsAPI.UserProfileApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Get your own profile.  Use this method to obtain detailed information about your ChronoSheets user profile.    Does not require any special permissions.
        api_response = api_instance.user_profile_get_my_profile(x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileApi->user_profile_get_my_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**ApiResponseUserProfile**](ApiResponseUserProfile.md)

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

# **user_profile_keep_session_alive**
> ApiResponseBoolean user_profile_keep_session_alive(x_chronosheets_auth)

Keep a session alive.  Use this method to keep a session active.  You could use this to 'ping' ChronoSheets every 'x' minutes to make sure your Auth Token will keep working.    Does not require any special permissions.

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
    api_instance = ChronoSheetsAPI.UserProfileApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

    try:
        # Keep a session alive.  Use this method to keep a session active.  You could use this to 'ping' ChronoSheets every 'x' minutes to make sure your Auth Token will keep working.    Does not require any special permissions.
        api_response = api_instance.user_profile_keep_session_alive(x_chronosheets_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileApi->user_profile_keep_session_alive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **user_profile_update_my_profile**
> ApiResponseUpdateProfileResponse user_profile_update_my_profile(x_chronosheets_auth, request)

Update your own profile.  Use this method to update your profile information or update/change your password.    Does not require any special permissions.

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
    api_instance = ChronoSheetsAPI.UserProfileApi(api_client)
    x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
request = ChronoSheetsAPI.UpdateMyProfileRequest() # UpdateMyProfileRequest | An Update MyProfile Request object containing updated fields.

    try:
        # Update your own profile.  Use this method to update your profile information or update/change your password.    Does not require any special permissions.
        api_response = api_instance.user_profile_update_my_profile(x_chronosheets_auth, request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileApi->user_profile_update_my_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 
 **request** | [**UpdateMyProfileRequest**](UpdateMyProfileRequest.md)| An Update MyProfile Request object containing updated fields. | 

### Return type

[**ApiResponseUpdateProfileResponse**](ApiResponseUpdateProfileResponse.md)

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

