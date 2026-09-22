# Mencoro::CreateInvitation200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **created** | **Boolean** | Always false on a 200. | [optional] |
| **reason** | **String** | Why nothing was created. | [optional] |
| **email** | **String** | The address as it was normalised. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateInvitation200Response.new(
  created: null,
  reason: null,
  email: null
)
```

