# UpdateGeoFenceRequest

A request object for updating a new geofence
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofence_id** | **int** | The ID of the geofence you want to update | [optional] 
**name** | **str** | The name of the geo fence | [optional] 
**fence_coordinates** | [**list[BasicCoordinate]**](BasicCoordinate.md) | A list of coordinates specifying the geofence region | [optional] 
**trigger_job_code_id** | **int** | The job code to be used when the person enters/leaves the geofence | [optional] 
**trigger_task_id** | **int** | The task to be used when the person enters/leaves the geofence | [optional] 
**send_alert_to_org_group_id** | **int** | Send an alert to a user, specified by their user ID | [optional] 
**alert_settings** | **str** | Define when you want the alerts to be setn | [optional] 
**trigger_settings** | **str** | Define how to you want to trigger the timesheet automation | [optional] 
**start_time_hour** | **int** | The start hour in which this geofence should apply.  After this time, the geofence will be active. | [optional] 
**start_time_minute** | **int** | The start minute in which this geofence should apply.  After this time, the geofence will be active. | [optional] 
**end_time_hour** | **int** | The end hour in which this geofence will stop applying.  After this time, the geofence will be inactive. | [optional] 
**end_time_minute** | **int** | The end minute in which this geofence will stop applying.  After this time, the geofence will be inactive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


