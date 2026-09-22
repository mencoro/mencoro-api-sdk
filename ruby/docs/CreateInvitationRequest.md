# Mencoro::CreateInvitationRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **email** | **String** |  | [optional] |
| **role** | **String** |  | [optional][default to &#39;viewer&#39;] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateInvitationRequest.new(
  email: null,
  role: null
)
```

