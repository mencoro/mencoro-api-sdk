# CitedSourcesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[CitedSourceRow]**](CitedSourceRow.md) |  | 
**total** | **int** |  | 

## Example

```python
from mencoro.models.cited_sources_response import CitedSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CitedSourcesResponse from a JSON string
cited_sources_response_instance = CitedSourcesResponse.from_json(json)
# print the JSON string representation of the object
print(CitedSourcesResponse.to_json())

# convert the object into a dict
cited_sources_response_dict = cited_sources_response_instance.to_dict()
# create an instance of CitedSourcesResponse from a dict
cited_sources_response_from_dict = CitedSourcesResponse.from_dict(cited_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


