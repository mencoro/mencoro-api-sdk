

# ListKeywordListings200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;KeywordListingResource&gt;**](KeywordListingResource.md) |  |  [optional] |
|**total** | **Integer** | Keywords matching the filters, not the size of this page. |  [optional] |
|**totalVariantCount** | **Integer** | Tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60;. With a text search applied this still counts the whole project, so it is not a budget figure for a searched page. |  [optional] |
|**dataDirtySince** | **OffsetDateTime** | When a pending recalculation was triggered. Null when the metrics are up to date. |  [optional] |



