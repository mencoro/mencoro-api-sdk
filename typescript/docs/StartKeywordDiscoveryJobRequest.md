
# StartKeywordDiscoveryJobRequest


## Properties

Name | Type
------------ | -------------
`input` | string
`language` | string
`country` | string
`excludeQueries` | Array&lt;string&gt;

## Example

```typescript
import type { StartKeywordDiscoveryJobRequest } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "input": crm for plumbers, field service software,
  "language": es,
  "country": ES,
  "excludeQueries": null,
} satisfies StartKeywordDiscoveryJobRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StartKeywordDiscoveryJobRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


