# Mencoro::CreateInvitationRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **email** | **String** |  | [optional] |
| **role** | **String** |  | [optional][default to &#39;viewer&#39;] |
| **project_access** | [**CreateInvitationRequestProjectAccess**](CreateInvitationRequestProjectAccess.md) |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateInvitationRequest.new(
  email: null,
  role: null,
  project_access: null
)
```

