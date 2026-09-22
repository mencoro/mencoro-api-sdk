
# AsyncJobResource

An asynchronous job and, once it has completed, its result

## Properties

Name | Type
------------ | -------------
`jobId` | string
`type` | string
`status` | string
`result` | object

## Example

```typescript
import type { AsyncJobResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "jobId": null,
  "type": null,
  "status": null,
  "result": null,
} satisfies AsyncJobResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AsyncJobResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


