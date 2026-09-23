# PositionDistributionBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from mencoro.models.position_distribution_bucket import PositionDistributionBucket

# TODO update the JSON string below
json = "{}"
# create an instance of PositionDistributionBucket from a JSON string
position_distribution_bucket_instance = PositionDistributionBucket.from_json(json)
# print the JSON string representation of the object
print(PositionDistributionBucket.to_json())

# convert the object into a dict
position_distribution_bucket_dict = position_distribution_bucket_instance.to_dict()
# create an instance of PositionDistributionBucket from a dict
position_distribution_bucket_from_dict = PositionDistributionBucket.from_dict(position_distribution_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


