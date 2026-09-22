
# OperationEffect

A single declared change, side effect, warning or condition

## Properties

Name | Type
------------ | -------------
`code` | string
`summary` | string
`targets` | Array&lt;string&gt;

## Example

```typescript
import type { OperationEffect } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "code": projects_will_be_archived,
  "summary": null,
  "targets": null,
} satisfies OperationEffect

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OperationEffect
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


