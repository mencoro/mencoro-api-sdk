
# ProjectedMonthlyChecksResource

What an organization\'s current tracking configuration would consume in a month

## Properties

Name | Type
------------ | -------------
`projectedMonthlyChecks` | number
`activeTrackedQueryCount` | number

## Example

```typescript
import type { ProjectedMonthlyChecksResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "projectedMonthlyChecks": 720,
  "activeTrackedQueryCount": 24,
} satisfies ProjectedMonthlyChecksResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectedMonthlyChecksResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


