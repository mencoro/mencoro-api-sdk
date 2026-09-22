# Mencoro::GetShareOfVoiceFormula200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **mention_type_weights** | **Hash&lt;String, Float&gt;** | Base weight per mention type; higher means a structurally stronger brand association. | [optional] |
| **sentiment_multipliers** | **Hash&lt;String, Float&gt;** | Multiplier per tone, applied on top of the base weight. | [optional] |
| **direct_multiplier** | **Float** | Applied when the mention carries no condition. | [optional] |
| **conditional_multiplier** | **Float** | Applied instead when the answer hedged the mention with a condition. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetShareOfVoiceFormula200Response.new(
  mention_type_weights: null,
  sentiment_multipliers: null,
  direct_multiplier: null,
  conditional_multiplier: null
)
```

