# DoLoginResponse

A Response object containing important information that can be used after the user has logged in
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cs_auth_token** | **str** | The ChronoSheets Auth Token.  Use this token for all subsequent requests to the API.  The Auth Token does these things: holds your session and gives you appropraite authorisation to access API endpoints based on your UserRoles | [optional] 
**logged_in_user** | [**ClientSideUser**](ClientSideUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


