

# ShoppingSnapshotResource

One captured shopping-results page

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**projectId** | **UUID** | The project this capture belongs to |  |
|**trackedQueryId** | **UUID** | The tracked query that was searched |  |
|**engine** | **String** | The shopping surface that was captured |  |
|**offers** | [**List&lt;ShoppingOfferResource&gt;**](ShoppingOfferResource.md) | Offers in rank order |  |
|**capturedAt** | **OffsetDateTime** | When the page was captured, UTC |  |



