
# SubscriptionResource

The current subscription contract of an organization

## Properties

Name | Type
------------ | -------------
`status` | string
`tierCode` | string
`billingCycleType` | string
`billingCycleAnchor` | Date
`checkBudget` | number
`checksConsumed` | number
`checksAvailable` | number
`nextResetAt` | Date
`cancelledAt` | Date
`scheduledToCancelAt` | Date
`gracePeriodEndsAt` | Date
`deactivationReason` | string
`isEntitled` | boolean

## Example

```typescript
import type { SubscriptionResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "status": null,
  "tierCode": tier_2000,
  "billingCycleType": null,
  "billingCycleAnchor": null,
  "checkBudget": null,
  "checksConsumed": null,
  "checksAvailable": null,
  "nextResetAt": null,
  "cancelledAt": null,
  "scheduledToCancelAt": null,
  "gracePeriodEndsAt": null,
  "deactivationReason": null,
  "isEntitled": null,
} satisfies SubscriptionResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SubscriptionResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


