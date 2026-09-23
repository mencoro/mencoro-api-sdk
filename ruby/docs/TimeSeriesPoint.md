# Mencoro::TimeSeriesPoint

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **raw_date** | **String** |  |  |
| **brand** | [**PerEntityMetrics**](PerEntityMetrics.md) |  |  |
| **competitors** | [**Hash&lt;String, PerEntityMetrics&gt;**](PerEntityMetrics.md) |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::TimeSeriesPoint.new(
  raw_date: null,
  brand: null,
  competitors: null
)
```

