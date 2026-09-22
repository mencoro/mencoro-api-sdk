
# StartPromptDiscoveryJobRequest


## Properties

Name | Type
------------ | -------------
`input` | string
`country` | string
`language` | string
`excludeQueries` | Array&lt;string&gt;

## Example

```typescript
import type { StartPromptDiscoveryJobRequest } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "input": crm for plumbers, field service software,
  "country": ES,
  "language": es,
  "excludeQueries": null,
} satisfies StartPromptDiscoveryJobRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StartPromptDiscoveryJobRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


