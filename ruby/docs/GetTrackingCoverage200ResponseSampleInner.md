# Mencoro::GetTrackingCoverage200ResponseSampleInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tracked_query_id** | **String** |  | [optional] |
| **query_text** | **String** |  | [optional] |
| **engine** | **String** |  | [optional] |
| **country** | **String** | ISO-3166 alpha-2 code | [optional] |
| **check_frequency** | **String** |  | [optional] |
| **last_checked_at** | **Time** | RFC 3339 timestamp of the last check. Null means never checked, which this sample never contains. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetTrackingCoverage200ResponseSampleInner.new(
  tracked_query_id: null,
  query_text: null,
  engine: null,
  country: null,
  check_frequency: null,
  last_checked_at: null
)
```

