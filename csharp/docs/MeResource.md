# Mencoro.Api.Model.MeResource
The authenticated user and the API key the request was made with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | **Guid** |  | 
**FullName** | **string** |  | 
**Email** | **string** |  | 
**Language** | **string** | IETF language tag the user reads the product in | 
**CreatedAt** | **DateTime** |  | 
**ApiKeyId** | **Guid** | The API key this request authenticated with | 
**Capabilities** | **List&lt;MeResource.CapabilitiesEnum&gt;** |  | 
**ScopeMode** | **string** |  | 
**OrganizationIds** | **List&lt;Guid&gt;** | Organizations the key names. Empty for a key scoped to all organizations, which instead follows the owner&#39;s membership. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

