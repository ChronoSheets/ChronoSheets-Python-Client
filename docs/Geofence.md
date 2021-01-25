# Geofence

A geofence
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_fencing_id** | **int** | The ID of the geofence | [optional] 
**org_id** | **int** | The ID of the organisation owning the geofence record | [optional] 
**created_by_user_id** | **int** | The ID of the user/employee who created the geofence | [optional] 
**last_updated_by_user_id** | **int** | The ID of the user/employee who last updated the geofence | [optional] 
**name** | **str** | A descriptive name of the geofence | [optional] 
**location_name** | **str** | The name of the approx. location of the geofence | [optional] 
**coordinates** | [**[BasicCoordinate]**](BasicCoordinate.md) | A list of co-ordinates specifying the geofence | [optional] 
**created_at** | **datetime** | The date and time the geofence was created.  Time is in UTC. | [optional] 
**updated_at** | **datetime** | The date and time the geofence was updated last.  Time is in UTC. | [optional] 
**trigger_job_code_id** | **int** | The ID of the job code used when the employee enters/exits the geofence | [optional] 
**trigger_task_id** | **int** | The ID of the task used when the employee enters/exits the geofence | [optional] 
**trigger_settings** | **str** | The settings for triggering actions | [optional] 
**alert_to_org_group_id** | **int** | The organisation group that will be notified when the geofence is triggered | [optional] 
**alert_settings** | **str** | The settings for trigger alerts | [optional] 
**start_time_hour** | **int** | The hour start time. E.g. 13 would be 1pm.  Time is in 24hr format. | [optional] 
**start_time_minute** | **int** | The minute start time.  E.g. 46 would be the 46th minute of the hour. | [optional] 
**end_time_hour** | **int** | The hour end time. E.g. 21 would be 9pm.  Time is in 24hr format. | [optional] 
**end_time_minute** | **int** | The minute end time.  E.g. 13 would be the 13th minute of the hour. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


