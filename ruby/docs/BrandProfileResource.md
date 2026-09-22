# Mencoro::BrandProfileResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | The project this profile belongs to |  |
| **brand_names** | **Array&lt;String&gt;** | The brand terms a mention in an AI answer is matched against. Empty when none has been configured yet. |  |
| **website_domains** | **Array&lt;String&gt;** | The domains a cited link or a search result is matched against. Empty when none has been configured yet. |  |
| **description** | **String** | What the brand does, as generated from its names and domains. Null means it has not been generated yet, which is not the same as an empty description. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BrandProfileResource.new(
  project_id: null,
  brand_names: null,
  website_domains: null,
  description: null
)
```

