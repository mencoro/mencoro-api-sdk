
# ClusterMembershipRequestData

The clusters a tracked query is added to or removed from

## Properties

Name | Type
------------ | -------------
`queryClusterIds` | Array&lt;string&gt;

## Example

```typescript
import type { ClusterMembershipRequestData } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "queryClusterIds": null,
} satisfies ClusterMembershipRequestData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClusterMembershipRequestData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


