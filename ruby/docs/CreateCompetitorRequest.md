# Mencoro::CreateCompetitorRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | The competitor&#39;s display name | [optional] |
| **website_domains** | **Array&lt;String&gt;** | Domains a result is matched against for this competitor. A full URL or a bare host. | [optional] |
| **brand_names** | **Array&lt;String&gt;** | Names a mention is matched against for this competitor | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateCompetitorRequest.new(
  name: null,
  website_domains: null,
  brand_names: null
)
```

