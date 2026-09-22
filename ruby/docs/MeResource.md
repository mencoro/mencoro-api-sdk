# Mencoro::MeResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **user_id** | **String** |  |  |
| **full_name** | **String** |  |  |
| **email** | **String** |  |  |
| **language** | **String** | IETF language tag the user reads the product in |  |
| **created_at** | **Time** |  |  |
| **api_key_id** | **String** | The API key this request authenticated with |  |
| **capabilities** | **Array&lt;String&gt;** |  |  |
| **scope_mode** | **String** |  |  |
| **organization_ids** | **Array&lt;String&gt;** | Organizations the key names. Empty for a key scoped to all organizations, which instead follows the owner&#39;s membership. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::MeResource.new(
  user_id: null,
  full_name: null,
  email: null,
  language: en,
  created_at: null,
  api_key_id: null,
  capabilities: null,
  scope_mode: null,
  organization_ids: null
)
```

