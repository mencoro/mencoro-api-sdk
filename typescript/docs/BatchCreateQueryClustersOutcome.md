
# BatchCreateQueryClustersOutcome

Per-name results of creating clusters in bulk

## Properties

Name | Type
------------ | -------------
`successful` | [Array&lt;BatchCreateQueryClustersOutcomeSuccessfulInner&gt;](BatchCreateQueryClustersOutcomeSuccessfulInner.md)
`failed` | [Array&lt;BatchCreateQueryClustersOutcomeFailedInner&gt;](BatchCreateQueryClustersOutcomeFailedInner.md)

## Example

```typescript
import type { BatchCreateQueryClustersOutcome } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "successful": null,
  "failed": null,
} satisfies BatchCreateQueryClustersOutcome

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BatchCreateQueryClustersOutcome
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


