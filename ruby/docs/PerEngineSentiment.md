# Mencoro::PerEngineSentiment

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **engine** | **String** |  |  |
| **positive** | **Integer** |  |  |
| **neutral** | **Integer** |  |  |
| **negative** | **Integer** |  |  |
| **mention_count** | **Integer** |  |  |
| **positivity_index** | **Integer** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::PerEngineSentiment.new(
  engine: null,
  positive: null,
  neutral: null,
  negative: null,
  mention_count: null,
  positivity_index: null
)
```

