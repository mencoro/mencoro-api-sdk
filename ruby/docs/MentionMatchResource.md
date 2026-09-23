# Mencoro::MentionMatchResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tracked_query_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **engine** | **String** |  |  |
| **ai_response_id** | **String** |  |  |
| **competitor_id** | **String** |  | [optional] |
| **mention_position** | **Integer** |  |  |
| **sentiment** | **String** |  |  |
| **mention_type** | **String** |  |  |
| **mention_type_condition** | **String** |  | [optional] |
| **response_context** | **String** |  |  |
| **detected_at** | **Time** |  |  |
| **mention_relation** | **String** |  | [optional] |
| **brand_name** | **String** |  | [optional] |
| **brand_name_as_mentioned** | **String** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::MentionMatchResource.new(
  tracked_query_id: null,
  project_id: null,
  engine: null,
  ai_response_id: null,
  competitor_id: null,
  mention_position: null,
  sentiment: null,
  mention_type: null,
  mention_type_condition: null,
  response_context: null,
  detected_at: null,
  mention_relation: null,
  brand_name: null,
  brand_name_as_mentioned: null
)
```

