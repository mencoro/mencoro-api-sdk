# Mencoro::GetOrganizationStats200ResponseProjects

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **total** | **Integer** | Every project of the organization the caller can access, archived ones included. | [optional] |
| **active** | **Integer** | Projects that are not archived; never greater than &#x60;total&#x60;. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetOrganizationStats200ResponseProjects.new(
  total: 25,
  active: 18
)
```

