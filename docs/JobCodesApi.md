# ChronoSheetsAPI.JobCodesApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_codes_create_job_code**](JobCodesApi.md#job_codes_create_job_code) | **PUT** /api/JobCodes/CreateJobCode | Create a job code
[**job_codes_delete_job_code**](JobCodesApi.md#job_codes_delete_job_code) | **DELETE** /api/JobCodes/DeleteJobCode | Delete a job code
[**job_codes_get_job_code_by_id**](JobCodesApi.md#job_codes_get_job_code_by_id) | **GET** /api/JobCodes/GetJobCodeById | Get a particular job code by job code id
[**job_codes_get_job_codes**](JobCodesApi.md#job_codes_get_job_codes) | **GET** /api/JobCodes/GetJobCodes | Get job codes for your organisation
[**job_codes_update_job_code**](JobCodesApi.md#job_codes_update_job_code) | **POST** /api/JobCodes/UpdateJobCode | Update a job code


# **job_codes_create_job_code**
> CSApiResponseInt32 job_codes_create_job_code(request, x_chronosheets_auth)

Create a job code

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.JobCodesApi()
request = ChronoSheetsAPI.CSInsertJobCodeRequest() # CSInsertJobCodeRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a job code
    api_response = api_instance.job_codes_create_job_code(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobCodesApi->job_codes_create_job_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertJobCodeRequest**](CSInsertJobCodeRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_delete_job_code**
> CSApiResponseBoolean job_codes_delete_job_code(job_code_id, x_chronosheets_auth)

Delete a job code

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.JobCodesApi()
job_code_id = 56 # int | The ID of the job code your want to delete
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Delete a job code
    api_response = api_instance.job_codes_delete_job_code(job_code_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobCodesApi->job_codes_delete_job_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_code_id** | **int**| The ID of the job code your want to delete | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_get_job_code_by_id**
> CSApiResponseJobCode job_codes_get_job_code_by_id(job_code_id, x_chronosheets_auth)

Get a particular job code by job code id

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.JobCodesApi()
job_code_id = 56 # int | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a particular job code by job code id
    api_response = api_instance.job_codes_get_job_code_by_id(job_code_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobCodesApi->job_codes_get_job_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_code_id** | **int**|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseJobCode**](CSApiResponseJobCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_get_job_codes**
> CSApiResponseListJobCode job_codes_get_job_codes(x_chronosheets_auth)

Get job codes for your organisation

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.JobCodesApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get job codes for your organisation
    api_response = api_instance.job_codes_get_job_codes(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobCodesApi->job_codes_get_job_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListJobCode**](CSApiResponseListJobCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_codes_update_job_code**
> CSApiResponseBoolean job_codes_update_job_code(request, x_chronosheets_auth)

Update a job code

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.JobCodesApi()
request = ChronoSheetsAPI.CSUpdateJobCodeRequest() # CSUpdateJobCodeRequest | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a job code
    api_response = api_instance.job_codes_update_job_code(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobCodesApi->job_codes_update_job_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSUpdateJobCodeRequest**](CSUpdateJobCodeRequest.md)|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

