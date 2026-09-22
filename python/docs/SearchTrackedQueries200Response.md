# SearchTrackedQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TrackedQueryResource]**](TrackedQueryResource.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mencoro.models.search_tracked_queries200_response import SearchTrackedQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTrackedQueries200Response from a JSON string
search_tracked_queries200_response_instance = SearchTrackedQueries200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTrackedQueries200Response.to_json())

# convert the object into a dict
search_tracked_queries200_response_dict = search_tracked_queries200_response_instance.to_dict()
# create an instance of SearchTrackedQueries200Response from a dict
search_tracked_queries200_response_from_dict = SearchTrackedQueries200Response.from_dict(search_tracked_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


