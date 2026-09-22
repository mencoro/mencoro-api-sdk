
# BatchChangeTrackedQueryPassesRequestData

Tracked queries to retune, and the passes per check to set on them

## Properties

Name | Type
------------ | -------------
`ids` | Array&lt;string&gt;
`nPasses` | number

## Example

```typescript
import type { BatchChangeTrackedQueryPassesRequestData } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "ids": null,
  "nPasses": null,
} satisfies BatchChangeTrackedQueryPassesRequestData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BatchChangeTrackedQueryPassesRequestData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


