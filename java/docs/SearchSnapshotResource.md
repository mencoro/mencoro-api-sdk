

# SearchSnapshotResource

One captured search-results page

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**projectId** | **UUID** | The project this capture belongs to |  |
|**trackedQueryId** | **UUID** | The tracked query that was searched |  |
|**engine** | **String** | The search engine that was captured |  |
|**results** | [**List&lt;SearchResultResource&gt;**](SearchResultResource.md) | Organic results in rank order |  |
|**capturedAt** | **OffsetDateTime** | When the page was captured, UTC |  |



