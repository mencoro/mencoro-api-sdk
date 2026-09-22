# Mencoro::InvitationResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **email** | **String** |  |  |
| **role** | **String** |  |  |
| **state** | **String** |  |  |
| **created_at** | **Time** |  |  |
| **expires_at** | **Time** |  |  |
| **accepted_at** | **Time** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::InvitationResource.new(
  id: null,
  email: null,
  role: null,
  state: null,
  created_at: null,
  expires_at: null,
  accepted_at: null
)
```

