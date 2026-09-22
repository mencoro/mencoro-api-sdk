# Mencoro.Api.Model.PreviewOrganizationOperation200ResponseOrganization
The organization the operation acts on. For createOrganization there is none yet, so `id` is null and `name` carries the name you proposed — the preview shows what you are about to create rather than hiding it. Branch on `organization.id`, never on `organization` itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid?** |  | [optional] 
**Name** | **string** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

