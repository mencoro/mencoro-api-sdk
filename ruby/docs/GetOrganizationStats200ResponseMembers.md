# Mencoro::GetOrganizationStats200ResponseMembers

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **total** | **Integer** | Active memberships. Suspended members are excluded. Null for a member restricted to selected projects. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetOrganizationStats200ResponseMembers.new(
  total: 12
)
```

