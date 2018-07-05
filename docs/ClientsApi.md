# ChronoSheetsAPI.ClientsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_create_client**](ClientsApi.md#clients_create_client) | **PUT** /api/Clients/CreateClient | Create a client.  Requires the &#39;ManageClientsAndProjects&#39; permission.
[**clients_get_client**](ClientsApi.md#clients_get_client) | **GET** /api/Clients/GetClient | Get a particular client.  Requires the &#39;ManageClientsAndProjects&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**clients_get_clients**](ClientsApi.md#clients_get_clients) | **GET** /api/Clients/GetClients | Get a collection of clients that are under your organisation.  Requires the &#39;ManageClientsAndProjects&#39; or &#39;ManageJobsAndTask&#39; permissions.
[**clients_update_client**](ClientsApi.md#clients_update_client) | **POST** /api/Clients/UpdateClient | Update a client.  Requires the &#39;ManageClientsAndProjects&#39; permission.


# **clients_create_client**
> CSApiResponseInt32 clients_create_client(request, x_chronosheets_auth)

Create a client.  Requires the 'ManageClientsAndProjects' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ClientsApi()
request = ChronoSheetsAPI.CSInsertClientRequest() # CSInsertClientRequest | An Insert Client Request object containing values for the new Client to create
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Create a client.  Requires the 'ManageClientsAndProjects' permission.
    api_response = api_instance.clients_create_client(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSInsertClientRequest**](CSInsertClientRequest.md)| An Insert Client Request object containing values for the new Client to create | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseInt32**](CSApiResponseInt32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get_client**
> CSApiResponseClient clients_get_client(client_id, x_chronosheets_auth)

Get a particular client.  Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ClientsApi()
client_id = 56 # int | The ID of the Client you want to get
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a particular client.  Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.
    api_response = api_instance.clients_get_client(client_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| The ID of the Client you want to get | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseClient**](CSApiResponseClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get_clients**
> CSApiResponseListClient clients_get_clients(x_chronosheets_auth)

Get a collection of clients that are under your organisation.  Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ClientsApi()
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get a collection of clients that are under your organisation.  Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.
    api_response = api_instance.clients_get_clients(x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_get_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseListClient**](CSApiResponseListClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_update_client**
> CSApiResponseBoolean clients_update_client(request, x_chronosheets_auth)

Update a client.  Requires the 'ManageClientsAndProjects' permission.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.ClientsApi()
request = ChronoSheetsAPI.CSSaveClientRequest() # CSSaveClientRequest | A Save Client Request object containing updated fields.  Make sure to specify the Client Id in the request object so that ChronoSheets knows which Client to update
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Update a client.  Requires the 'ManageClientsAndProjects' permission.
    api_response = api_instance.clients_update_client(request, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_update_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CSSaveClientRequest**](CSSaveClientRequest.md)| A Save Client Request object containing updated fields.  Make sure to specify the Client Id in the request object so that ChronoSheets knows which Client to update | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseBoolean**](CSApiResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

