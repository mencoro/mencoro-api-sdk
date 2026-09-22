
# TrackedQueryDetailResource

A tracked query and how it is checked

## Properties

Name | Type
------------ | -------------
`id` | string
`projectId` | string
`queryText` | string
`engine` | string
`locale` | string
`country` | string
`queryClusterIds` | Array&lt;string&gt;
`status` | string
`checkFrequency` | string
`nPasses` | number
`lastCheckedAt` | Date

## Example

```typescript
import type { TrackedQueryDetailResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "projectId": null,
  "queryText": null,
  "engine": null,
  "locale": null,
  "country": null,
  "queryClusterIds": null,
  "status": null,
  "checkFrequency": null,
  "nPasses": null,
  "lastCheckedAt": null,
} satisfies TrackedQueryDetailResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrackedQueryDetailResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


