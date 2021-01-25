# OrgReportTimesheetFileAttachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**timesheet_id** | **int** | The ID of the timesheet this attachment is attached to. | [optional] 
**document_s3_signed_url** | **str** | The limited use signed URL for the document (if it&#39;s not an image).  This URL is unique and will eventually expire.  If the attachment is an image, then this won&#39;t be set. | [optional] 
**image_large_s3_signed_url** | **str** | The limited use signed URL for the large version of the image.  This URL is unique and will eventually expire.  Only set when the attachment is actually an image. | [optional] 
**image_medium_s3_signed_url** | **str** | The limited use signed URL for the medium version of the image.  This URL is unique and will eventually expire.  Only set when the attachment is actually an image. | [optional] 
**image_small_s3_signed_url** | **str** | The limited use signed URL for the small version of the image.  This URL is unique and will eventually expire.  Only set when the attachment is actually an image. | [optional] 
**timesheet_start** | **datetime** | The start date and time of the timesheet that this attachment is attached to | [optional] 
**timesheet_end** | **datetime** | The end date and time of the timesheet that this attachment is attached to | [optional] 
**file_attachment_id** | **int** | The ID of the file attachment | [optional] 
**user_id** | **int** | The ID of the user who attached the file | [optional] 
**org_id** | **int** | The ID of the organisation that owns the file and employs the employee | [optional] 
**mobile_platform** | **str** | The mobile platform that was used to attach the file | [optional] 
**attachment_type** | **str** | The type of file attachment | [optional] 
**notes** | **str** | Any notes regarding the file attachment | [optional] 
**non_image_file_path** | **str** | The path to the file attachment as hosted by ChronoSheets storage, if it&#39;s not an image.  If the attachment is an image then this won&#39;t be set. | [optional] 
**image_large_file_path** | **str** | The path to the file attachment as hosted by ChronoSheets storage, only set if it&#39;s an image.  This is regarding the large version of the image. | [optional] 
**image_medium_file_path** | **str** | The path to the file attachment as hosted by ChronoSheets storage, only set if it&#39;s an image.  This is regarding the medium version of the image. | [optional] 
**image_small_file_path** | **str** | The path to the file attachment as hosted by ChronoSheets storage, only set if it&#39;s an image.  This is regarding the small version of the image. | [optional] 
**original_file_name** | **str** | The original file name of the attachment | [optional] 
**latitude** | **float** | Meta-data indicating the latitude of the file attachment.  If the attachment is an image, this data originates from the meta data inside the image file. | [optional] 
**longitude** | **float** | Meta-data indicating the longitude of the file attachment.  If the attachment is an image, this data originates from the meta data inside the image file. | [optional] 
**date_uploaded** | **datetime** | The date and time the attachment was uploaded.  Time is in UTC. | [optional] 
**date_image_captured** | **datetime** | The original date and time the image was captured, if it was an image.  This data originates from the meta data inside the image file. | [optional] 
**storage_allocation_bytes** | **int** | The number of bytes allocated for storing the file attachment. | [optional] 
**audio_duration_seconds** | **int** | If the attachment was an audio file, this field indicates the duration of the audio file in seconds.  This data originates from the meta data inside the audio file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


