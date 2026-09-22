# Mencoro::CreateProjectRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** |  |  |
| **website_domains** | **Array&lt;String&gt;** | At least one website URL or domain to monitor. |  |
| **brand_names** | **Array&lt;String&gt;** | At least one brand name to match in AI answers and search results. |  |
| **competitors** | [**Array&lt;CreateProjectRequestCompetitorsInner&gt;**](CreateProjectRequestCompetitorsInner.md) | Competitors to create with the project. Optional; they can also be added later through the competitor endpoints. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateProjectRequest.new(
  name: null,
  website_domains: null,
  brand_names: null,
  competitors: null
)
```

