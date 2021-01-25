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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import user_profile_api
from ChronoSheetsAPI.model.api_response_do_login_response import ApiResponseDoLoginResponse
from ChronoSheetsAPI.model.do_login_request import DoLoginRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_profile_api.UserProfileApi(api_client)
    request = DoLoginRequest(
        username_or_email="username_or_email_example",
        password="password_example",
        remember_me=True,
    ) # DoLoginRequest | A request object containing your username/email and password.

    # example passing only required values which don't have defaults set
    try:
        # Login to your ChronoSheets account and obtain an Auth Token which you can use for other ChronoSheets API methods.    Does not require any special permissions.
        api_response = api_instance.user_profile_do_login(request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import user_profile_api
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
    api_instance = user_profile_api.UserProfileApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Logout of your ChronoSheets account.  This method ends and deletes your active session.    Does not require any special permissions.
        api_response = api_instance.user_profile_do_logout(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import user_profile_api
from ChronoSheetsAPI.model.api_response_user_profile import ApiResponseUserProfile
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_profile_api.UserProfileApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get your own profile.  Use this method to obtain detailed information about your ChronoSheets user profile.    Does not require any special permissions.
        api_response = api_instance.user_profile_get_my_profile(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import user_profile_api
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
    api_instance = user_profile_api.UserProfileApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Keep a session alive.  Use this method to keep a session active.  You could use this to 'ping' ChronoSheets every 'x' minutes to make sure your Auth Token will keep working.    Does not require any special permissions.
        api_response = api_instance.user_profile_keep_session_alive(x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import user_profile_api
from ChronoSheetsAPI.model.update_my_profile_request import UpdateMyProfileRequest
from ChronoSheetsAPI.model.api_response_update_profile_response import ApiResponseUpdateProfileResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_profile_api.UserProfileApi(api_client)
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    request = UpdateMyProfileRequest(
        email_address="email_address_example",
        first_name="first_name_example",
        last_name="last_name_example",
        old_password="old_password_example",
        new_password="new_password_example",
        confirm_new_password="confirm_new_password_example",
        is_subscribed_to_newsletter=True,
        wants_to_change_password=True,
    ) # UpdateMyProfileRequest | An Update MyProfile Request object containing updated fields.

    # example passing only required values which don't have defaults set
    try:
        # Update your own profile.  Use this method to update your profile information or update/change your password.    Does not require any special permissions.
        api_response = api_instance.user_profile_update_my_profile(x_chronosheets_auth, request)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
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

