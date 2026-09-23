# Mencoro::PerEntityMetrics

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **serp** | **Float** |  | [optional] |
| **shopping** | **Float** |  | [optional] |
| **mention** | **Float** |  | [optional] |
| **link** | **Float** |  | [optional] |
| **positivity** | **Integer** |  | [optional] |
| **share_of_voice** | **Float** |  | [optional] |
| **mention_rate** | **Integer** |  | [optional] |
| **serp_rate** | **Integer** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::PerEntityMetrics.new(
  serp: null,
  shopping: null,
  mention: null,
  link: null,
  positivity: null,
  share_of_voice: null,
  mention_rate: null,
  serp_rate: null
)
```

