
# BatchForceCheckTrackedQueries200Response


## Properties

Name | Type
------------ | -------------
`successful` | [Array&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;](BatchPauseTrackedQueries200ResponseSuccessfulInner.md)
`failed` | [Array&lt;BatchForceCheckTrackedQueries200ResponseFailedInner&gt;](BatchForceCheckTrackedQueries200ResponseFailedInner.md)

## Example

```typescript
import type { BatchForceCheckTrackedQueries200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "successful": null,
  "failed": null,
} satisfies BatchForceCheckTrackedQueries200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BatchForceCheckTrackedQueries200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


