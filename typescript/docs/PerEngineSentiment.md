
# PerEngineSentiment


## Properties

Name | Type
------------ | -------------
`engine` | string
`positive` | number
`neutral` | number
`negative` | number
`mentionCount` | number
`positivityIndex` | number

## Example

```typescript
import type { PerEngineSentiment } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "engine": null,
  "positive": null,
  "neutral": null,
  "negative": null,
  "mentionCount": null,
  "positivityIndex": null,
} satisfies PerEngineSentiment

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PerEngineSentiment
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


