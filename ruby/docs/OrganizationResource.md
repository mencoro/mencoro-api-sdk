# Mencoro::OrganizationResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** |  |  |
| **description** | **String** |  | [optional] |
| **status** | **String** |  |  |
| **image_url** | **String** |  | [optional] |
| **contact_email** | **String** |  | [optional] |
| **role** | **String** | The caller&#39;s current role in this organization |  |
| **created_at** | **Time** |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::OrganizationResource.new(
  id: null,
  name: null,
  description: null,
  status: null,
  image_url: null,
  contact_email: null,
  role: null,
  created_at: null
)
```

