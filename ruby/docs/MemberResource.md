# Mencoro::MemberResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **user_id** | **String** | The user this membership belongs to |  |
| **role** | **String** |  |  |
| **state** | **String** |  |  |
| **is_active** | **Boolean** |  |  |
| **joined_at** | **Time** |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::MemberResource.new(
  id: null,
  user_id: null,
  role: null,
  state: null,
  is_active: null,
  joined_at: null
)
```

