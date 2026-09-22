# ListKeywordListings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**\Mencoro\Api\Model\KeywordListingResource[]**](KeywordListingResource.md) |  | [optional]
**total** | **int** | Keywords matching the filters, not the size of this page. | [optional]
**total_variant_count** | **int** | Tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60;. With a text search applied this still counts the whole project, so it is not a budget figure for a searched page. | [optional]
**data_dirty_since** | **\DateTime** | When a pending recalculation was triggered. Null when the metrics are up to date. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
