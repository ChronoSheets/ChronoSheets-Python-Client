# AggregateJobCode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_tasks** | [**[AggregateJobTask]**](AggregateJobTask.md) | The list of available tasks under this job code | [optional] 
**permitted_employees** | **[int]** | The list of employee IDs that are permitted to record timesheets with this job code (empty means everyone) | [optional] 
**id** | **int** | The ID of the job code (not the code itself) | [optional] 
**code** | **str** | The job code itself | [optional] 
**client** | **str** | The name of the client | [optional] 
**client_id** | **int** | The ID of the client | [optional] 
**project** | **str** | The name of the project | [optional] 
**project_id** | **int** | The ID of the project | [optional] 
**organisation_id** | **int** | Your organisation ID | [optional] 
**is_deleted** | **bool** | A flag indicating whether or not the job code has been marked as deleted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


