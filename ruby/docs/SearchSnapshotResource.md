# Mencoro::SearchSnapshotResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **project_id** | **String** | The project this capture belongs to |  |
| **tracked_query_id** | **String** | The tracked query that was searched |  |
| **engine** | **String** | The search engine that was captured |  |
| **results** | [**Array&lt;SearchResultResource&gt;**](SearchResultResource.md) | Organic results in rank order |  |
| **captured_at** | **Time** | When the page was captured, UTC |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::SearchSnapshotResource.new(
  id: null,
  project_id: null,
  tracked_query_id: null,
  engine: null,
  results: null,
  captured_at: null
)
```

