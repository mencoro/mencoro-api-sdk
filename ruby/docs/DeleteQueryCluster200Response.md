# Mencoro::DeleteQueryCluster200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The cluster that was deleted | [optional] |
| **name** | **String** | Its name at the moment it was deleted | [optional] |
| **deleted** | **Boolean** | Always true; present so the body is self-describing | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::DeleteQueryCluster200Response.new(
  id: null,
  name: null,
  deleted: null
)
```

