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
| **project_access_mode** | **String** | Which projects of the organization the member reaches: every project, or only projectIds |  |
| **project_ids** | **Array&lt;String&gt;** | The projects a selected access reaches; empty when the mode is all |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::MemberResource.new(
  id: null,
  user_id: null,
  role: null,
  state: null,
  is_active: null,
  joined_at: null,
  project_access_mode: null,
  project_ids: null
)
```

