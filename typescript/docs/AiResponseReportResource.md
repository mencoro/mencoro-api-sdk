
# AiResponseReportResource

Acknowledgement of a report about a captured AI answer

## Properties

Name | Type
------------ | -------------
`aiResponseId` | string
`trackedQueryId` | string
`type` | string
`comment` | string
`missedBrandNames` | Array&lt;string&gt;
`accepted` | boolean

## Example

```typescript
import type { AiResponseReportResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "aiResponseId": null,
  "trackedQueryId": null,
  "type": null,
  "comment": null,
  "missedBrandNames": null,
  "accepted": null,
} satisfies AiResponseReportResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AiResponseReportResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


