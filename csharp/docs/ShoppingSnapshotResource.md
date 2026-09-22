# Mencoro.Api.Model.ShoppingSnapshotResource
One captured shopping-results page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**ProjectId** | **Guid** | The project this capture belongs to | 
**TrackedQueryId** | **Guid** | The tracked query that was searched | 
**Engine** | **string** | The shopping surface that was captured | 
**Offers** | [**List&lt;ShoppingOfferResource&gt;**](ShoppingOfferResource.md) | Offers in rank order | 
**CapturedAt** | **DateTime** | When the page was captured, UTC | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

