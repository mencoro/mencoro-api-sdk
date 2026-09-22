
# TrackedQueryUsageResource

How many tracked queries an organization has configured

## Properties

Name | Type
------------ | -------------
`trackedQueryCount` | number

## Example

```typescript
import type { TrackedQueryUsageResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "trackedQueryCount": 124,
} satisfies TrackedQueryUsageResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrackedQueryUsageResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


