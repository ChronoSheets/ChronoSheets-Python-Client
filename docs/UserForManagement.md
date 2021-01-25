# UserForManagement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_account_active** | **bool** |  | [optional] 
**id** | **int** | The ID of the user | [optional] 
**organisation_id** | **int** | The ID of the organisation | [optional] 
**user_name** | **str** | The username of the user | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**email_address** | **str** | The email address of the user | [optional] 
**roles** | **int** | A BIT field designating which Roles/Permissions the employee will have when they sign in.  See the {timesheets.types.Enums.UserRoles} Enum for more details | [optional] 
**alert_settings** | **int** | A BIT field designating which Alerts the employee will receive.  See the {timesheets.types.Enums.AlertSettings} Enum for more details | [optional] 
**setup_wizard_required** | **bool** | Whether or not the setup wizard is required | [optional] 
**is_subscribed_to_newsletter** | **bool** | Whether or not the user is subscribed to the user | [optional] 
**organisation** | [**Organisation**](Organisation.md) |  | [optional] 
**is_primary_account** | **bool** | Whether or not this account is the organisation&#39;s primary account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


