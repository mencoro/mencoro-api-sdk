
# PreviewOrganizationOperation200Response


## Properties

Name | Type
------------ | -------------
`action` | string
`organization` | [PreviewOrganizationOperation200ResponseOrganization](PreviewOrganizationOperation200ResponseOrganization.md)
`resourceId` | string
`changes` | [Array&lt;OperationEffect&gt;](OperationEffect.md)
`sideEffects` | [Array&lt;OperationEffect&gt;](OperationEffect.md)
`warnings` | [Array&lt;OperationEffect&gt;](OperationEffect.md)
`conditions` | [Array&lt;OperationEffect&gt;](OperationEffect.md)
`actor` | object
`confirmation` | object

## Example

```typescript
import type { PreviewOrganizationOperation200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "action": null,
  "organization": null,
  "resourceId": null,
  "changes": null,
  "sideEffects": null,
  "warnings": null,
  "conditions": null,
  "actor": null,
  "confirmation": null,
} satisfies PreviewOrganizationOperation200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PreviewOrganizationOperation200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


