
# TrackedQueryCountResource

How many tracked queries a project has, and what checking them would cost in budget units

## Properties

Name | Type
------------ | -------------
`count` | number
`checkCost` | number

## Example

```typescript
import type { TrackedQueryCountResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "count": 42,
  "checkCost": 96,
} satisfies TrackedQueryCountResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrackedQueryCountResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


