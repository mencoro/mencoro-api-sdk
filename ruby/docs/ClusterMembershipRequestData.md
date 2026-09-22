# Mencoro::ClusterMembershipRequestData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **query_cluster_ids** | **Array&lt;String&gt;** | Ids of the query clusters. Duplicates are collapsed. Every id must belong to the project in the path. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ClusterMembershipRequestData.new(
  query_cluster_ids: null
)
```

