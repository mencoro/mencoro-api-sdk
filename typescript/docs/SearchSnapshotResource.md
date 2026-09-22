
# SearchSnapshotResource

One captured search-results page

## Properties

Name | Type
------------ | -------------
`id` | string
`projectId` | string
`trackedQueryId` | string
`engine` | string
`results` | [Array&lt;SearchResultResource&gt;](SearchResultResource.md)
`capturedAt` | Date

## Example

```typescript
import type { SearchSnapshotResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "projectId": null,
  "trackedQueryId": null,
  "engine": null,
  "results": null,
  "capturedAt": null,
} satisfies SearchSnapshotResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SearchSnapshotResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


