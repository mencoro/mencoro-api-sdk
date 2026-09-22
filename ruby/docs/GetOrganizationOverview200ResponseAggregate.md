# Mencoro::GetOrganizationOverview200ResponseAggregate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_count** | **Integer** | Active projects in the organization, the length of &#x60;projects&#x60;. | [optional] |
| **projects_with_data** | **Integer** | How many of those have a share of voice; the averages below are means over the projects that report each metric, never over the ones still null. | [optional] |
| **total_tracked_queries** | **Integer** |  | [optional] |
| **avg_share_of_voice** | **Float** | Null when no project reports a share of voice. | [optional] |
| **avg_mention_rate** | **Integer** |  | [optional] |
| **avg_mention_position** | **Float** | 1-based rank; LOWER is better. | [optional] |
| **avg_positivity_index** | **Integer** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetOrganizationOverview200ResponseAggregate.new(
  project_count: null,
  projects_with_data: null,
  total_tracked_queries: null,
  avg_share_of_voice: null,
  avg_mention_rate: null,
  avg_mention_position: null,
  avg_positivity_index: null
)
```

