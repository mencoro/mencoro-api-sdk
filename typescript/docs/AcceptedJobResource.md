
# AcceptedJobResource

Background work accepted for processing

## Properties

Name | Type
------------ | -------------
`jobId` | string
`deduplicated` | boolean
`trackingUrl` | string

## Example

```typescript
import type { AcceptedJobResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "jobId": null,
  "deduplicated": null,
  "trackingUrl": null,
} satisfies AcceptedJobResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AcceptedJobResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


