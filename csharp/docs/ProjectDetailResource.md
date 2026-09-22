# Mencoro.Api.Model.ProjectDetailResource
A project and the brand monitoring configuration its checks run against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**OrganizationId** | **Guid** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**CreatedAt** | **DateTime** |  | 
**WebsiteDomains** | **List&lt;string&gt;** | Domains the project is monitored for. Empty when the project has no brand monitoring profile yet. | 
**BrandNames** | **List&lt;string&gt;** | Brand names matched in AI answers and search results. Empty when the project has no brand monitoring profile yet. | 
**Competitors** | [**List&lt;ProjectDetailResourceCompetitorsInner&gt;**](ProjectDetailResourceCompetitorsInner.md) | Competitors this project is measured against. Empty when none are configured. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

