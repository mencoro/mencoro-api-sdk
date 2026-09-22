# Mencoro::TrackedQueryDetailResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **project_id** | **String** | The project this tracked query belongs to |  |
| **query_text** | **String** | The prompt or keyword sent to the engine |  |
| **engine** | **String** |  |  |
| **locale** | **String** | Language tag the query is asked in. Null when the engine is asked without one. | [optional] |
| **country** | **String** | ISO-3166 alpha-2 country the query is asked from |  |
| **query_cluster_ids** | **Array&lt;String&gt;** | Clusters (groups) this query belongs to. Empty when it is ungrouped. |  |
| **status** | **String** |  |  |
| **check_frequency** | **String** | How often the query is checked while active |  |
| **n_passes** | **Integer** | Passes run per check. Greater than 1 only for AI engines. |  |
| **last_checked_at** | **Time** | When a check last completed. Null means no check has completed yet, which is not the same as a check that found nothing. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::TrackedQueryDetailResource.new(
  id: null,
  project_id: null,
  query_text: null,
  engine: null,
  locale: null,
  country: null,
  query_cluster_ids: null,
  status: null,
  check_frequency: null,
  n_passes: null,
  last_checked_at: null
)
```

