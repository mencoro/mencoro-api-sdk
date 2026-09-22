# Mencoro::CompetitorResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** | The competitor&#39;s display name |  |
| **website_domains** | **Array&lt;String&gt;** | Domains a result is matched against for this competitor |  |
| **brand_names** | **Array&lt;String&gt;** | Names a mention is matched against for this competitor |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CompetitorResource.new(
  id: null,
  name: null,
  website_domains: null,
  brand_names: null
)
```

