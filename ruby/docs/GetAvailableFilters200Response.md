# Mencoro::GetAvailableFilters200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **engines** | **Array&lt;String&gt;** | Engine codes, ready to pass as the engines filter | [optional] |
| **countries** | **Array&lt;String&gt;** | ISO-3166 alpha-2 codes, ready to pass as the countries filter | [optional] |
| **clusters** | [**Array&lt;GetAvailableFilters200ResponseClustersInner&gt;**](GetAvailableFilters200ResponseClustersInner.md) |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetAvailableFilters200Response.new(
  engines: null,
  countries: null,
  clusters: null
)
```

