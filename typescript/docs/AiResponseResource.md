
# AiResponseResource

One captured AI answer with its citations

## Properties

Name | Type
------------ | -------------
`id` | string
`projectId` | string
`trackedQueryId` | string
`engine` | string
`responseText` | string
`citations` | [Array&lt;CitationResource&gt;](CitationResource.md)
`capturedAt` | Date
`modelName` | string
`passIndex` | number
`passCount` | number

## Example

```typescript
import type { AiResponseResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "projectId": null,
  "trackedQueryId": null,
  "engine": null,
  "responseText": null,
  "citations": null,
  "capturedAt": null,
  "modelName": null,
  "passIndex": null,
  "passCount": null,
} satisfies AiResponseResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AiResponseResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


