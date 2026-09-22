# Mencoro::ProjectDetailResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **organization_id** | **String** |  |  |
| **name** | **String** |  |  |
| **status** | **String** |  |  |
| **created_at** | **Time** |  |  |
| **website_domains** | **Array&lt;String&gt;** | Domains the project is monitored for. Empty when the project has no brand monitoring profile yet. |  |
| **brand_names** | **Array&lt;String&gt;** | Brand names matched in AI answers and search results. Empty when the project has no brand monitoring profile yet. |  |
| **competitors** | [**Array&lt;ProjectDetailResourceCompetitorsInner&gt;**](ProjectDetailResourceCompetitorsInner.md) | Competitors this project is measured against. Empty when none are configured. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ProjectDetailResource.new(
  id: null,
  organization_id: null,
  name: null,
  status: null,
  created_at: null,
  website_domains: null,
  brand_names: null,
  competitors: null
)
```

