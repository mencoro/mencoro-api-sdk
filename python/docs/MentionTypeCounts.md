# MentionTypeCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation** | **int** |  | 
**comparison** | **int** |  | 
**listing** | **int** |  | 
**example** | **int** |  | 
**reference** | **int** |  | 

## Example

```python
from mencoro.models.mention_type_counts import MentionTypeCounts

# TODO update the JSON string below
json = "{}"
# create an instance of MentionTypeCounts from a JSON string
mention_type_counts_instance = MentionTypeCounts.from_json(json)
# print the JSON string representation of the object
print(MentionTypeCounts.to_json())

# convert the object into a dict
mention_type_counts_dict = mention_type_counts_instance.to_dict()
# create an instance of MentionTypeCounts from a dict
mention_type_counts_from_dict = MentionTypeCounts.from_dict(mention_type_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


