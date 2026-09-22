# Mencoro::UpdateProjectBrandProfileRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **website_domains** | **Array&lt;String&gt;** | Domains a cited link or a search result is matched against. A full URL or a bare host. | [optional] |
| **brand_names** | **Array&lt;String&gt;** | Terms a mention in an AI answer is matched against. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::UpdateProjectBrandProfileRequest.new(
  website_domains: null,
  brand_names: null
)
```

