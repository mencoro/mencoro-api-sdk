# Mencoro::BulkAddClustersToTrackedQueriesRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | **Array&lt;String&gt;** | Tracked queries to add. At most 100 distinct ids; duplicates are collapsed. | [optional] |
| **query_cluster_ids** | **Array&lt;String&gt;** | Clusters every named tracked query is added to. All must belong to the project in the path. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BulkAddClustersToTrackedQueriesRequest.new(
  ids: null,
  query_cluster_ids: null
)
```

