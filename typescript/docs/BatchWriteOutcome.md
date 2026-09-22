
# BatchWriteOutcome

Per-item results of a batch write

## Properties

Name | Type
------------ | -------------
`successful` | [Array&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;](BatchPauseTrackedQueries200ResponseSuccessfulInner.md)
`failed` | [Array&lt;BatchWriteOutcomeFailedInner&gt;](BatchWriteOutcomeFailedInner.md)

## Example

```typescript
import type { BatchWriteOutcome } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "successful": null,
  "failed": null,
} satisfies BatchWriteOutcome

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BatchWriteOutcome
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


