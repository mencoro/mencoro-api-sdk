# Mencoro::StartClusteringJobRequestData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tracked_query_ids** | **Array&lt;String&gt;** | The tracked queries to cluster. Duplicates are collapsed. |  |
| **mode** | **String** | fill_gaps groups only tracked queries that belong to no cluster; add_on_top adds the new clusters to whatever each query already has; full_regroup replaces the current clusters with the job&#39;s. |  |
| **restrict_to_existing_clusters** | **Boolean** | When true the job may only use clusters the project already has, and leaves a query ungrouped rather than inventing a name for it. | [optional][default to false] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::StartClusteringJobRequestData.new(
  tracked_query_ids: null,
  mode: null,
  restrict_to_existing_clusters: null
)
```

