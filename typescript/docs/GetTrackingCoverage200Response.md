
# GetTrackingCoverage200Response


## Properties

Name | Type
------------ | -------------
`projectId` | string
`total` | number
`active` | number
`paused` | number
`neverChecked` | number
`overdue` | number
`sample` | [Array&lt;GetTrackingCoverage200ResponseSampleInner&gt;](GetTrackingCoverage200ResponseSampleInner.md)

## Example

```typescript
import type { GetTrackingCoverage200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "projectId": null,
  "total": null,
  "active": null,
  "paused": null,
  "neverChecked": null,
  "overdue": null,
  "sample": null,
} satisfies GetTrackingCoverage200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetTrackingCoverage200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


