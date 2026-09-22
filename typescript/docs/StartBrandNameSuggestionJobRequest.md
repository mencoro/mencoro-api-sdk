
# StartBrandNameSuggestionJobRequest


## Properties

Name | Type
------------ | -------------
`name` | string
`websiteDomains` | Array&lt;string&gt;
`enteredBrandNames` | Array&lt;string&gt;
`country` | string

## Example

```typescript
import type { StartBrandNameSuggestionJobRequest } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "name": Acme,
  "websiteDomains": ["https://acme.com"],
  "enteredBrandNames": ["Acme","Acme Inc"],
  "country": ES,
} satisfies StartBrandNameSuggestionJobRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StartBrandNameSuggestionJobRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


