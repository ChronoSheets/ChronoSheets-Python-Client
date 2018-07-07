# CSInsertJobCodeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A short code for the Job.  This is referred to as a Job Code | [optional] 
**project_id** | **int** | The linked Project.  Time spent with this JobCode is on this Project | [optional] 
**client_id** | **int** | The linked Client.  Time spent with this JobCode is for this Client | [optional] 
**linked_task_ids** | **list[int]** | A list of Task Ids.  This are the Tasks that become available to the employee when they select this JobCode | [optional] 
**linked_org_group_ids** | **list[int]** | Optionally restrict access to the JobCode by specifying which Organisation Groups can use it | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


