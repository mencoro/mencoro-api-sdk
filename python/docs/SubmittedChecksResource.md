# SubmittedChecksResource

The tracked queries submitted for an immediate check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted** | **int** | How many tracked queries were submitted. Zero is a valid answer: it means nothing in the project was eligible. | 
**tracked_query_ids** | **List[UUID]** | The tracked queries submitted, in the order they were submitted (least recently checked first). Poll these to follow progress. | 

## Example

```python
from mencoro.models.submitted_checks_resource import SubmittedChecksResource

# TODO update the JSON string below
json = "{}"
# create an instance of SubmittedChecksResource from a JSON string
submitted_checks_resource_instance = SubmittedChecksResource.from_json(json)
# print the JSON string representation of the object
print(SubmittedChecksResource.to_json())

# convert the object into a dict
submitted_checks_resource_dict = submitted_checks_resource_instance.to_dict()
# create an instance of SubmittedChecksResource from a dict
submitted_checks_resource_from_dict = SubmittedChecksResource.from_dict(submitted_checks_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


