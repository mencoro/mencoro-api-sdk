# Mencoro::GetOrganizationOverview200ResponseProjectsInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |
| **tracked_query_count** | **Integer** |  | [optional] |
| **share_of_voice** | **Float** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. | [optional] |
| **mention_rate** | **Integer** | 0-100 percentage of tracked queries with a result; higher is better. Null when the project has no rank data yet. | [optional] |
| **avg_mention_position** | **Float** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. | [optional] |
| **positivity_index** | **Integer** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetOrganizationOverview200ResponseProjectsInner.new(
  project_id: null,
  name: null,
  status: null,
  tracked_query_count: null,
  share_of_voice: null,
  mention_rate: null,
  avg_mention_position: null,
  positivity_index: null
)
```

