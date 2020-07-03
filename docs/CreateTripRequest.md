# CreateTripRequest

Contains fields for creating a Trip
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_id** | **int** | The associated Timesheet record Id.  The Trip will be linked to the Timesheet with this TimesheetId | [optional] 
**vehicle_id** | **int** | The associated Vehicle Id.  The Trip will show that this Vehicle was used | [optional] 
**path_coords_string_csv** | **str** | A CSV of GPS path co-ordinates.  Format example: -37.8433562,144.7226188;[Lat1],[Long1];........[LatN],[LongN] | [optional] 
**distance_meters** | **float** | The total distance of the Trip | [optional] 
**mobile_platform** | **str** | The Mobile platform that the Trip was recorded on | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


