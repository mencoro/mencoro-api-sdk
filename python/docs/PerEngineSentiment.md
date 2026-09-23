# PerEngineSentiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** |  | 
**positive** | **int** |  | 
**neutral** | **int** |  | 
**negative** | **int** |  | 
**mention_count** | **int** |  | 
**positivity_index** | **int** |  | [optional] 

## Example

```python
from mencoro.models.per_engine_sentiment import PerEngineSentiment

# TODO update the JSON string below
json = "{}"
# create an instance of PerEngineSentiment from a JSON string
per_engine_sentiment_instance = PerEngineSentiment.from_json(json)
# print the JSON string representation of the object
print(PerEngineSentiment.to_json())

# convert the object into a dict
per_engine_sentiment_dict = per_engine_sentiment_instance.to_dict()
# create an instance of PerEngineSentiment from a dict
per_engine_sentiment_from_dict = PerEngineSentiment.from_dict(per_engine_sentiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


