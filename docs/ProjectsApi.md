# ChronoSheetsAPI.ProjectsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_create_project**](ProjectsApi.md#projects_create_project) | **POST** /Projects/CreateProject | Create a project.    Requires the &#39;ManageClientsAndProjects&#39; permission.
[**projects_get_project_by_id**](ProjectsApi.md#projects_get_project_by_id) | **GET** /Projects/GetProjectById | Get a project by its Id.    Requires the &#39;ManageClientsAndProjects&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**projects_get_projects_for_client**](ProjectsApi.md#projects_get_projects_for_client) | **GET** /Projects/GetProjectsForClient | Get projects for a particular client.    Requires the &#39;ManageClientsAndProjects&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**projects_update_project**](ProjectsApi.md#projects_update_project) | **PUT** /Projects/UpdateProject | Update a project.    Requires the &#39;ManageClientsAndProjects&#39; permission.


# **projects_create_project**
> CSApiResponseInt32 projects_create_project(request, x_chronosheets_auth)

Create a project.    Requires the 'ManageClientsAndProjects' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ProjectsApi()
request = ChronoSheetsAPI.CSInsertProjectRequest() # CSInsertProjectRequest | An Insert Project Request object containing values for the new Project to create.  Make sure to specify a correct Client Id - this will be used to attach the new project under that client.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a project.    Requires the 'ManageClientsAndProjects' permission.
    api_response = api_instance.projects_create_project(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertProjectRequest**](CSInsertProjectRequest.md)| An Insert Project Request object containing values for the new Project to create.  Make sure to specify a correct Client Id - this will be used to attach the new project under that client. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_project_by_id**
> CSApiResponseProject projects_get_project_by_id(project_id, x_chronosheets_auth)

Get a project by its Id.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ProjectsApi()
project_id = 56 # int | The ID of the Project you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a project by its Id.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.
    api_response = api_instance.projects_get_project_by_id(project_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_project_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the Project you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseProject**](CSApiResponseProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_projects_for_client**
> CSApiResponseListProject projects_get_projects_for_client(client_id, x_chronosheets_auth)

Get projects for a particular client.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ProjectsApi()
client_id = 56 # int | The ID of the client
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get projects for a particular client.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.
    api_response = api_instance.projects_get_projects_for_client(client_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get_projects_for_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| The ID of the client | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListProject**](CSApiResponseListProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update_project**
> CSApiResponseBoolean projects_update_project(request, x_chronosheets_auth)

Update a project.    Requires the 'ManageClientsAndProjects' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ProjectsApi()
request = ChronoSheetsAPI.CSUpdateProjectRequest() # CSUpdateProjectRequest | An Update Project Request object containing updated fields.  Make sure to specify the Project Id in the request object so that ChronoSheets knows which Project to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a project.    Requires the 'ManageClientsAndProjects' permission.
    api_response = api_instance.projects_update_project(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSUpdateProjectRequest**](CSUpdateProjectRequest.md)| An Update Project Request object containing updated fields.  Make sure to specify the Project Id in the request object so that ChronoSheets knows which Project to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

