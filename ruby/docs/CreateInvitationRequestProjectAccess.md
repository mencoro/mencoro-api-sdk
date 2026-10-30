# Mencoro::CreateInvitationRequestProjectAccess

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **mode** | **String** |  |  |
| **project_ids** | **Array&lt;String&gt;** | For selected: at least one and at most 500 projects of the organization. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateInvitationRequestProjectAccess.new(
  mode: null,
  project_ids: null
)
```

