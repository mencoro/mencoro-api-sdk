
# StartClusteringJobRequestData

What a clustering job should group, and how

## Properties

Name | Type
------------ | -------------
`trackedQueryIds` | Array&lt;string&gt;
`mode` | string
`restrictToExistingClusters` | boolean

## Example

```typescript
import type { StartClusteringJobRequestData } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "trackedQueryIds": null,
  "mode": null,
  "restrictToExistingClusters": null,
} satisfies StartClusteringJobRequestData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StartClusteringJobRequestData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


