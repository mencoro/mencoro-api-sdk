
# BatchChangeTrackedQueryCheckFrequencyRequestData

Tracked queries to retune, and the check frequency to set on them

## Properties

Name | Type
------------ | -------------
`ids` | Array&lt;string&gt;
`checkFrequency` | string

## Example

```typescript
import type { BatchChangeTrackedQueryCheckFrequencyRequestData } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "ids": null,
  "checkFrequency": null,
} satisfies BatchChangeTrackedQueryCheckFrequencyRequestData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BatchChangeTrackedQueryCheckFrequencyRequestData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


