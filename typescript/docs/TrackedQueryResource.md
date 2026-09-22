
# TrackedQueryResource

A tracked query and the metrics of its most recent check

## Properties

Name | Type
------------ | -------------
`id` | string
`queryText` | string
`engine` | string
`country` | string
`status` | string
`queryClusterIds` | Array&lt;string&gt;
`checkFrequency` | string
`nPasses` | number
`lastSerpPosition` | number
`lastMentionPosition` | number
`lastLinkPosition` | number
`lastShoppingPosition` | number
`lastShareOfVoice` | number
`lastPositivityIndex` | number
`lastPositiveMentionCount` | number
`lastNeutralMentionCount` | number
`lastNegativeMentionCount` | number
`lastCheckedAt` | Date

## Example

```typescript
import type { TrackedQueryResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "queryText": null,
  "engine": null,
  "country": null,
  "status": null,
  "queryClusterIds": null,
  "checkFrequency": null,
  "nPasses": null,
  "lastSerpPosition": null,
  "lastMentionPosition": null,
  "lastLinkPosition": null,
  "lastShoppingPosition": null,
  "lastShareOfVoice": null,
  "lastPositivityIndex": null,
  "lastPositiveMentionCount": null,
  "lastNeutralMentionCount": null,
  "lastNegativeMentionCount": null,
  "lastCheckedAt": null,
} satisfies TrackedQueryResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrackedQueryResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


