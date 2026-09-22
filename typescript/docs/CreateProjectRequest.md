
# CreateProjectRequest


## Properties

Name | Type
------------ | -------------
`name` | string
`websiteDomains` | Array&lt;string&gt;
`brandNames` | Array&lt;string&gt;
`competitors` | [Array&lt;CreateProjectRequestCompetitorsInner&gt;](CreateProjectRequestCompetitorsInner.md)

## Example

```typescript
import type { CreateProjectRequest } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "websiteDomains": null,
  "brandNames": null,
  "competitors": null,
} satisfies CreateProjectRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateProjectRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


