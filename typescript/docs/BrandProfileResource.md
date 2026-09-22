
# BrandProfileResource

The brand identity a project\'s checks are matched against

## Properties

Name | Type
------------ | -------------
`projectId` | string
`brandNames` | Array&lt;string&gt;
`websiteDomains` | Array&lt;string&gt;
`description` | string

## Example

```typescript
import type { BrandProfileResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "projectId": null,
  "brandNames": null,
  "websiteDomains": null,
  "description": null,
} satisfies BrandProfileResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrandProfileResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


