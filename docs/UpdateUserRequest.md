# UpdateUserRequest

Fields for updating an employee User Account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The Id of the User that is to be updated | [optional] 
**email_address** | **str** | The Email Address of the employee | [optional] 
**first_name** | **str** | The First Name of the employee | [optional] 
**last_name** | **str** | The Last Name of the employee | [optional] 
**is_subscribed_to_newsletter** | **bool** | Whether or not the employee is subscribed to ChronoSheets newsletters | [optional] 
**is_account_active** | **bool** | Whether or not the employee account is active | [optional] 
**roles** | **int** | A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details | [optional] 
**alert_settings** | **int** | A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


