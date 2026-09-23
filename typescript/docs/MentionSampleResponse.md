
# MentionSampleResponse


## Properties

Name | Type
------------ | -------------
`id` | string
`trackedQueryId` | string
`aiResponseId` | string
`engine` | string
`competitorId` | string
`sentiment` | string
`mentionType` | string
`mentionPosition` | number
`text` | string
`detectedAt` | string
`queryText` | string
`country` | string
`mentionRelation` | string
`brandName` | string

## Example

```typescript
import type { MentionSampleResponse } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "trackedQueryId": null,
  "aiResponseId": null,
  "engine": null,
  "competitorId": null,
  "sentiment": null,
  "mentionType": null,
  "mentionPosition": null,
  "text": null,
  "detectedAt": null,
  "queryText": null,
  "country": null,
  "mentionRelation": null,
  "brandName": null,
} satisfies MentionSampleResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MentionSampleResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


