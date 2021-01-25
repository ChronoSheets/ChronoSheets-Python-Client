# ChronoSheetsAPI.TranscriptsApi

All URIs are relative to *https://api.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcripts_get_my_transcript**](TranscriptsApi.md#transcripts_get_my_transcript) | **GET** /Transcripts/GetMyTranscript | Get an audio to text transcript for a particular audio file attachment
[**transcripts_get_my_transcripts**](TranscriptsApi.md#transcripts_get_my_transcripts) | **GET** /Transcripts/GetMyTranscripts | Get my file transcripts.  Get audio to text transcripts that you&#39;ve created.


# **transcripts_get_my_transcript**
> ApiResponseTranscription transcripts_get_my_transcript(file_attachment_id, x_chronosheets_auth)

Get an audio to text transcript for a particular audio file attachment

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import transcripts_api
from ChronoSheetsAPI.model.api_response_transcription import ApiResponseTranscription
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transcripts_api.TranscriptsApi(api_client)
    file_attachment_id = 1 # int | The ID of the file attachment that has a transcript.  It should be an audio file attachment.
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token

    # example passing only required values which don't have defaults set
    try:
        # Get an audio to text transcript for a particular audio file attachment
        api_response = api_instance.transcripts_get_my_transcript(file_attachment_id, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TranscriptsApi->transcripts_get_my_transcript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_attachment_id** | **int**| The ID of the file attachment that has a transcript.  It should be an audio file attachment. |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |

### Return type

[**ApiResponseTranscription**](ApiResponseTranscription.md)

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

# **transcripts_get_my_transcripts**
> ApiResponseForPaginatedListOrgReportTranscript transcripts_get_my_transcripts(start_date, end_date, x_chronosheets_auth)

Get my file transcripts.  Get audio to text transcripts that you've created.

### Example

```python
import time
import ChronoSheetsAPI
from ChronoSheetsClientLibApi import transcripts_api
from ChronoSheetsAPI.model.api_response_for_paginated_list_org_report_transcript import ApiResponseForPaginatedListOrgReportTranscript
from pprint import pprint
# Defining the host is optional and defaults to https://api.chronosheets.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ChronoSheetsAPI.Configuration(
    host = "https://api.chronosheets.com"
)


# Enter a context with an instance of the API client
with ChronoSheetsAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transcripts_api.TranscriptsApi(api_client)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The Start date of the date range.  Transcripts after this date will be obtained.
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The End date of the date range.  Transcripts before this date will be obtained.
    x_chronosheets_auth = "x-chronosheets-auth_example" # str | The ChronoSheets Auth Token
    skip = 1 # int | Skip this many transcripts (optional)
    take = 1 # int | Take this many transcripts (optional)
    keyword = "Keyword_example" # str | Search the text content of the transcript keywords (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get my file transcripts.  Get audio to text transcripts that you've created.
        api_response = api_instance.transcripts_get_my_transcripts(start_date, end_date, x_chronosheets_auth)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TranscriptsApi->transcripts_get_my_transcripts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get my file transcripts.  Get audio to text transcripts that you've created.
        api_response = api_instance.transcripts_get_my_transcripts(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, keyword=keyword)
        pprint(api_response)
    except ChronoSheetsAPI.ApiException as e:
        print("Exception when calling TranscriptsApi->transcripts_get_my_transcripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The Start date of the date range.  Transcripts after this date will be obtained. |
 **end_date** | **datetime**| The End date of the date range.  Transcripts before this date will be obtained. |
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token |
 **skip** | **int**| Skip this many transcripts | [optional]
 **take** | **int**| Take this many transcripts | [optional]
 **keyword** | **str**| Search the text content of the transcript keywords | [optional]

### Return type

[**ApiResponseForPaginatedListOrgReportTranscript**](ApiResponseForPaginatedListOrgReportTranscript.md)

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

