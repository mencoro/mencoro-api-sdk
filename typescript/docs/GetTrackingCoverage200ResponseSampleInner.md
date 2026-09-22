
# GetTrackingCoverage200ResponseSampleInner


## Properties

Name | Type
------------ | -------------
`trackedQueryId` | string
`queryText` | string
`engine` | string
`country` | string
`checkFrequency` | string
`lastCheckedAt` | Date

## Example

```typescript
import type { GetTrackingCoverage200ResponseSampleInner } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "trackedQueryId": null,
  "queryText": null,
  "engine": null,
  "country": null,
  "checkFrequency": null,
  "lastCheckedAt": null,
} satisfies GetTrackingCoverage200ResponseSampleInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetTrackingCoverage200ResponseSampleInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


