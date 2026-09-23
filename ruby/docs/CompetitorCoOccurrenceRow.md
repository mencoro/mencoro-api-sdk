# Mencoro::CompetitorCoOccurrenceRow

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **competitor_id** | **String** |  |  |
| **shared_response_count** | **Integer** |  |  |
| **brand_wins** | **Integer** |  |  |
| **competitor_wins** | **Integer** |  |  |
| **ties** | **Integer** |  |  |
| **win_rate** | **Integer** |  | [optional] |
| **avg_own_position** | **Float** |  | [optional] |
| **avg_competitor_position** | **Float** |  | [optional] |
| **example_query_text** | **String** |  | [optional] |
| **example_ai_response_id** | **String** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CompetitorCoOccurrenceRow.new(
  competitor_id: null,
  shared_response_count: null,
  brand_wins: null,
  competitor_wins: null,
  ties: null,
  win_rate: null,
  avg_own_position: null,
  avg_competitor_position: null,
  example_query_text: null,
  example_ai_response_id: null
)
```

