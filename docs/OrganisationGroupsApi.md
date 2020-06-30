# ChronoSheetsAPI.OrganisationGroupsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisation_groups_create_organisation_group**](OrganisationGroupsApi.md#organisation_groups_create_organisation_group) | **POST** /OrganisationGroups/CreateOrganisationGroup | Create an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.
[**organisation_groups_delete_organisation_group**](OrganisationGroupsApi.md#organisation_groups_delete_organisation_group) | **DELETE** /OrganisationGroups/DeleteOrganisationGroup | 
[**organisation_groups_get_organisation_group**](OrganisationGroupsApi.md#organisation_groups_get_organisation_group) | **GET** /OrganisationGroups/GetOrganisationGroup | Get a particular organisation group.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.
[**organisation_groups_get_organisation_groups**](OrganisationGroupsApi.md#organisation_groups_get_organisation_groups) | **GET** /OrganisationGroups/GetOrganisationGroups | Get a collection of organisation groups that are under your organisation.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.
[**organisation_groups_get_organisation_groups_for_job**](OrganisationGroupsApi.md#organisation_groups_get_organisation_groups_for_job) | **GET** /OrganisationGroups/GetOrganisationGroupsForJob | Get org groups for a particular job.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageJobsAndTask&#39;, &#39;ManageClientsAndProjects&#39; or &#39;ManageOrganisationUsers&#39; permissions.
[**organisation_groups_get_organisation_groups_for_vehicle**](OrganisationGroupsApi.md#organisation_groups_get_organisation_groups_for_vehicle) | **GET** /OrganisationGroups/GetOrganisationGroupsForVehicle | Get org groups for a particular vehicle.    Requires the &#39;ManageOrganisationGroups&#39;, &#39;ManageFleet&#39; or &#39;ManageOrganisationUsers&#39; permissions.
[**organisation_groups_update_organisation_group**](OrganisationGroupsApi.md#organisation_groups_update_organisation_group) | **PUT** /OrganisationGroups/UpdateOrganisationGroup | Update an organisation group.    Requires the &#39;ManageOrganisationGroups&#39; permissions.


# **organisation_groups_create_organisation_group**
> CSApiResponseInt32 organisation_groups_create_organisation_group(request, x_chronosheets_auth)

Create an organisation group.    Requires the 'ManageOrganisationGroups' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
request = ChronoSheetsAPI.CSInsertOrganisationGroupRequest() # CSInsertOrganisationGroupRequest | An Insert OrganisationGroup Request object containing values for the new OrganisationGroup to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create an organisation group.    Requires the 'ManageOrganisationGroups' permissions.
    api_response = api_instance.organisation_groups_create_organisation_group(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_create_organisation_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertOrganisationGroupRequest**](CSInsertOrganisationGroupRequest.md)| An Insert OrganisationGroup Request object containing values for the new OrganisationGroup to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_groups_delete_organisation_group**
> CSApiResponseBoolean organisation_groups_delete_organisation_group(organisation_group_id, x_chronosheets_auth)



### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
organisation_group_id = 56 # int | 
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    api_response = api_instance.organisation_groups_delete_organisation_group(organisation_group_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_delete_organisation_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_group_id** | **int**|  | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_groups_get_organisation_group**
> CSApiResponseOrganisationGroup organisation_groups_get_organisation_group(organisation_group_id, x_chronosheets_auth)

Get a particular organisation group.    Requires the 'ManageOrganisationGroups', 'ManageJobsAndTask', 'ManageClientsAndProjects' or 'ManageOrganisationUsers' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
organisation_group_id = 56 # int | The ID of the OrganisationGroup you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a particular organisation group.    Requires the 'ManageOrganisationGroups', 'ManageJobsAndTask', 'ManageClientsAndProjects' or 'ManageOrganisationUsers' permissions.
    api_response = api_instance.organisation_groups_get_organisation_group(organisation_group_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_get_organisation_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_group_id** | **int**| The ID of the OrganisationGroup you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseOrganisationGroup**](CSApiResponseOrganisationGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_groups_get_organisation_groups**
> CSApiResponseListOrganisationGroup organisation_groups_get_organisation_groups(x_chronosheets_auth)

Get a collection of organisation groups that are under your organisation.    Requires the 'ManageOrganisationGroups', 'ManageJobsAndTask', 'ManageClientsAndProjects' or 'ManageOrganisationUsers' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a collection of organisation groups that are under your organisation.    Requires the 'ManageOrganisationGroups', 'ManageJobsAndTask', 'ManageClientsAndProjects' or 'ManageOrganisationUsers' permissions.
    api_response = api_instance.organisation_groups_get_organisation_groups(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_get_organisation_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListOrganisationGroup**](CSApiResponseListOrganisationGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_groups_get_organisation_groups_for_job**
> CSApiResponseListOrganisationGroup organisation_groups_get_organisation_groups_for_job(job_id, x_chronosheets_auth)

Get org groups for a particular job.    Requires the 'ManageOrganisationGroups', 'ManageJobsAndTask', 'ManageClientsAndProjects' or 'ManageOrganisationUsers' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
job_id = 56 # int | The ID of the job
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get org groups for a particular job.    Requires the 'ManageOrganisationGroups', 'ManageJobsAndTask', 'ManageClientsAndProjects' or 'ManageOrganisationUsers' permissions.
    api_response = api_instance.organisation_groups_get_organisation_groups_for_job(job_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_get_organisation_groups_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| The ID of the job | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListOrganisationGroup**](CSApiResponseListOrganisationGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_groups_get_organisation_groups_for_vehicle**
> CSApiResponseListOrganisationGroup organisation_groups_get_organisation_groups_for_vehicle(vehicle_id, x_chronosheets_auth)

Get org groups for a particular vehicle.    Requires the 'ManageOrganisationGroups', 'ManageFleet' or 'ManageOrganisationUsers' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
vehicle_id = 56 # int | The ID of the vehicle
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get org groups for a particular vehicle.    Requires the 'ManageOrganisationGroups', 'ManageFleet' or 'ManageOrganisationUsers' permissions.
    api_response = api_instance.organisation_groups_get_organisation_groups_for_vehicle(vehicle_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_get_organisation_groups_for_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| The ID of the vehicle | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListOrganisationGroup**](CSApiResponseListOrganisationGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisation_groups_update_organisation_group**
> CSApiResponseBoolean organisation_groups_update_organisation_group(request, x_chronosheets_auth)

Update an organisation group.    Requires the 'ManageOrganisationGroups' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.OrganisationGroupsApi()
request = ChronoSheetsAPI.CSSaveOrganisationGroupRequest() # CSSaveOrganisationGroupRequest | A Save OrganisationGroup Request object containing updated fields.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update an organisation group.    Requires the 'ManageOrganisationGroups' permissions.
    api_response = api_instance.organisation_groups_update_organisation_group(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationGroupsApi->organisation_groups_update_organisation_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSSaveOrganisationGroupRequest**](CSSaveOrganisationGroupRequest.md)| A Save OrganisationGroup Request object containing updated fields.  Make sure to specify the OrganisationGroup Id in the request object so that ChronoSheets knows which OrganisationGroup to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

