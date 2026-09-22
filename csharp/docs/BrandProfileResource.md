# Mencoro.Api.Model.BrandProfileResource
The brand identity a project's checks are matched against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectId** | **Guid** | The project this profile belongs to | 
**BrandNames** | **List&lt;string&gt;** | The brand terms a mention in an AI answer is matched against. Empty when none has been configured yet. | 
**WebsiteDomains** | **List&lt;string&gt;** | The domains a cited link or a search result is matched against. Empty when none has been configured yet. | 
**Description** | **string** | What the brand does, as generated from its names and domains. Null means it has not been generated yet, which is not the same as an empty description. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

