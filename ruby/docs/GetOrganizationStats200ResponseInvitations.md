# Mencoro::GetOrganizationStats200ResponseInvitations

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **pending** | **Integer** | Invitations still awaiting an answer. Accepted, cancelled and expired ones are excluded. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetOrganizationStats200ResponseInvitations.new(
  pending: 3
)
```

