# SubscriptionResource

The current subscription contract of an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Contract state. \&quot;none\&quot; when the organization has never held a subscription. | 
**tier_code** | **str** | Public tier identifier derived from the check budget. | [optional] 
**billing_cycle_type** | **str** | Billing interval of the contract. | [optional] 
**billing_cycle_anchor** | **datetime** | Instant the billing cycle is anchored to. | [optional] 
**check_budget** | **int** | Checks the current cycle grants. Null when there is no subscription, never a stand-in for zero. | [optional] 
**checks_consumed** | **int** | Checks consumed so far in the current cycle. Null when there is no subscription; zero means none consumed yet. | [optional] 
**checks_available** | **int** | Checks still available in the current cycle. Null when there is no subscription; zero means the budget is exhausted. | [optional] 
**next_reset_at** | **datetime** | When the check budget resets next. | [optional] 
**cancelled_at** | **datetime** | When the subscription was terminally cancelled. Null while it has not been. | [optional] 
**scheduled_to_cancel_at** | **datetime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] 
**grace_period_ends_at** | **datetime** | When paid access ends after a cancellation. Null when the subscription is not cancelled. | [optional] 
**deactivation_reason** | **str** | Why the subscription is currently inactive. Null for an active subscription, and meaningless once \&quot;cancelledAt\&quot; is set - the cancellation supersedes it. | [optional] 
**is_entitled** | **bool** | Whether the organization may use paid features right now: active, or cancelled but still inside its paid grace window. | 

## Example

```python
from mencoro.models.subscription_resource import SubscriptionResource

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResource from a JSON string
subscription_resource_instance = SubscriptionResource.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResource.to_json())

# convert the object into a dict
subscription_resource_dict = subscription_resource_instance.to_dict()
# create an instance of SubscriptionResource from a dict
subscription_resource_from_dict = SubscriptionResource.from_dict(subscription_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


