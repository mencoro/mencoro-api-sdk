
# ProjectMentionMixResponse


## Properties

Name | Type
------------ | -------------
`byType` | { [key: string]: number; }
`byTone` | { [key: string]: number; }
`byQualifier` | { [key: string]: number; }

## Example

```typescript
import type { ProjectMentionMixResponse } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "byType": null,
  "byTone": null,
  "byQualifier": null,
} satisfies ProjectMentionMixResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectMentionMixResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


