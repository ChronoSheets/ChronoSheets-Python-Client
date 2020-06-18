# ChronoSheetsAPI.TranscriptsApi

All URIs are relative to *https://www.chronosheets.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcripts_get_my_transcript**](TranscriptsApi.md#transcripts_get_my_transcript) | **GET** /api/Transcripts/GetMyTranscript | Get an audio to text transcript for a particular audio file attachment
[**transcripts_get_my_transcripts**](TranscriptsApi.md#transcripts_get_my_transcripts) | **GET** /api/Transcripts/GetMyTranscripts | Get my file transcripts.  Get audio to text transcripts that you&#39;ve created.


# **transcripts_get_my_transcript**
> CSApiResponseTranscription transcripts_get_my_transcript(file_attachment_id, x_chronosheets_auth)

Get an audio to text transcript for a particular audio file attachment

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TranscriptsApi()
file_attachment_id = 56 # int | The ID of the file attachment that has a transcript.  It should be an audio file attachment.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token

try:
    # Get an audio to text transcript for a particular audio file attachment
    api_response = api_instance.transcripts_get_my_transcript(file_attachment_id, x_chronosheets_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranscriptsApi->transcripts_get_my_transcript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_attachment_id** | **int**| The ID of the file attachment that has a transcript.  It should be an audio file attachment. | 
 **x_chronosheets_auth** | **str**| The ChronoSheets Auth Token | 

### Return type

[**CSApiResponseTranscription**](CSApiResponseTranscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcripts_get_my_transcripts**
> CSApiResponseForPaginatedListOrgReportTranscript transcripts_get_my_transcripts(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, keyword=keyword)

Get my file transcripts.  Get audio to text transcripts that you've created.

### Example
```python
from __future__ import print_function
import time
import ChronoSheetsAPI
from ChronoSheetsAPI.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ChronoSheetsAPI.TranscriptsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | The Start date of the date range.  Transcripts after this date will be obtained.
end_date = '2013-10-20T19:20:30+01:00' # datetime | The End date of the date range.  Transcripts before this date will be obtained.
x_chronosheets_auth = 'x_chronosheets_auth_example' # str | The ChronoSheets Auth Token
skip = 56 # int | Skip this many transcripts (optional)
take = 56 # int | Take this many transcripts (optional)
keyword = 'keyword_example' # str | Search the text content of the transcript keywords (optional)

try:
    # Get my file transcripts.  Get audio to text transcripts that you've created.
    api_response = api_instance.transcripts_get_my_transcripts(start_date, end_date, x_chronosheets_auth, skip=skip, take=take, keyword=keyword)
    pprint(api_response)
except ApiException as e:
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

[**CSApiResponseForPaginatedListOrgReportTranscript**](CSApiResponseForPaginatedListOrgReportTranscript.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

