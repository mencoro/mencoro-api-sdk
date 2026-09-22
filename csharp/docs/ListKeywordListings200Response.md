# Mencoro.Api.Model.ListKeywordListings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**List&lt;KeywordListingResource&gt;**](KeywordListingResource.md) |  | [optional] 
**Total** | **int** | Keywords matching the filters, not the size of this page. | [optional] 
**TotalVariantCount** | **int** | Tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60;. With a text search applied this still counts the whole project, so it is not a budget figure for a searched page. | [optional] 
**DataDirtySince** | **DateTime?** | When a pending recalculation was triggered. Null when the metrics are up to date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

