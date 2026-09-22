
# EntitlementsResource

What an organization\'s plan allows and what it has consumed

## Properties

Name | Type
------------ | -------------
`status` | string
`isEntitled` | boolean
`checkBudget` | number
`checksConsumed` | number
`checksAvailable` | number
`billingCycleType` | string
`billingCycleAnchor` | Date
`nextResetAt` | Date
`cancelledAt` | Date
`scheduledToCancelAt` | Date
`gracePeriodEndsAt` | Date

## Example

```typescript
import type { EntitlementsResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "status": null,
  "isEntitled": null,
  "checkBudget": null,
  "checksConsumed": null,
  "checksAvailable": null,
  "billingCycleType": null,
  "billingCycleAnchor": null,
  "nextResetAt": null,
  "cancelledAt": null,
  "scheduledToCancelAt": null,
  "gracePeriodEndsAt": null,
} satisfies EntitlementsResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EntitlementsResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


