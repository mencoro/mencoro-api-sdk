
# GetOrganizationOverview200Response


## Properties

Name | Type
------------ | -------------
`projects` | [Array&lt;GetOrganizationOverview200ResponseProjectsInner&gt;](GetOrganizationOverview200ResponseProjectsInner.md)
`aggregate` | [GetOrganizationOverview200ResponseAggregate](GetOrganizationOverview200ResponseAggregate.md)

## Example

```typescript
import type { GetOrganizationOverview200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "projects": null,
  "aggregate": null,
} satisfies GetOrganizationOverview200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetOrganizationOverview200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


