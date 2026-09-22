# Mencoro.Api.Model.SearchSnapshotResource
One captured search-results page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**ProjectId** | **Guid** | The project this capture belongs to | 
**TrackedQueryId** | **Guid** | The tracked query that was searched | 
**Engine** | **string** | The search engine that was captured | 
**Results** | [**List&lt;SearchResultResource&gt;**](SearchResultResource.md) | Organic results in rank order | 
**CapturedAt** | **DateTime** | When the page was captured, UTC | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

