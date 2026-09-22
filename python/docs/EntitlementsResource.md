# EntitlementsResource

What an organization's plan allows and what it has consumed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | \&quot;none\&quot; when the organization has never had a subscription contract. | 
**is_entitled** | **bool** | Whether the organization may use paid features right now: an active contract, or a cancelled one still inside its paid grace window. | 
**check_budget** | **int** | Checks the current cycle allows. Null when there is no plan on file, which is not the same as a budget of zero. | [optional] 
**checks_consumed** | **int** | Checks consumed so far in the current cycle. Null when there is no plan on file. | [optional] 
**checks_available** | **int** | Checks left in the current cycle. Null when there is no plan on file. | [optional] 
**billing_cycle_type** | **str** | How often the allowance renews. Null when there is no plan on file. | [optional] 
**billing_cycle_anchor** | **datetime** | Start of the current cycle. Null when there is no plan on file. | [optional] 
**next_reset_at** | **datetime** | When the check budget next resets. Null when there is no plan on file. | [optional] 
**cancelled_at** | **datetime** | When the subscription was terminally cancelled. Null while it has not been. | [optional] 
**scheduled_to_cancel_at** | **datetime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] 
**grace_period_ends_at** | **datetime** | When paid access ends after a cancellation. Null when the subscription has not been cancelled. | [optional] 

## Example

```python
from mencoro.models.entitlements_resource import EntitlementsResource

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementsResource from a JSON string
entitlements_resource_instance = EntitlementsResource.from_json(json)
# print the JSON string representation of the object
print(EntitlementsResource.to_json())

# convert the object into a dict
entitlements_resource_dict = entitlements_resource_instance.to_dict()
# create an instance of EntitlementsResource from a dict
entitlements_resource_from_dict = EntitlementsResource.from_dict(entitlements_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


