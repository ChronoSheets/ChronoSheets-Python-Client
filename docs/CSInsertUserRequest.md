# CSInsertUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | The Email Address of the employee | [optional] 
**first_name** | **str** | The First Name of the employee | [optional] 
**last_name** | **str** | The Last Name of the employee | [optional] 
**is_subscribed_to_newsletter** | **bool** | Whether or not the employee is subscribed to ChronoSheets newsletters | [optional] 
**roles** | **int** | A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details | [optional] 
**alert_settings** | **int** | A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details | [optional] 
**user_name** | **str** | The UserName of the employee.  This can be used when logging into ChronoSheets | [optional] 
**hourly_pay_rate** | **float** | Set the starting usual Hourly Pay Rate with this value.  This is the Pay Rate the employee receives for working during Rostered Hours | [optional] 
**hourly_overtime_pay_rate** | **float** | Set the starting usual Overtime Hourly Pay Rate with this value.  This is the Pay Rate the employee receives for working outside of Rostered Hours | [optional] 
**current_date** | **datetime** | The Current date time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


