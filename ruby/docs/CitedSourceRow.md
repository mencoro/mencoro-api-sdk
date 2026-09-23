# Mencoro::CitedSourceRow

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **group_key** | **String** |  |  |
| **domain** | **String** |  | [optional] |
| **citation_count** | **Integer** |  |  |
| **distinct_query_count** | **Integer** |  |  |
| **distinct_response_count** | **Integer** |  |  |
| **avg_position** | **Float** |  | [optional] |
| **sample_title** | **String** |  | [optional] |
| **sample_url** | **String** |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CitedSourceRow.new(
  group_key: null,
  domain: null,
  citation_count: null,
  distinct_query_count: null,
  distinct_response_count: null,
  avg_position: null,
  sample_title: null,
  sample_url: null
)
```

