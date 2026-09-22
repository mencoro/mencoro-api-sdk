# GetAvailableFilters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engines** | **List[str]** | Engine codes, ready to pass as the engines filter | [optional] 
**countries** | **List[str]** | ISO-3166 alpha-2 codes, ready to pass as the countries filter | [optional] 
**clusters** | [**List[GetAvailableFilters200ResponseClustersInner]**](GetAvailableFilters200ResponseClustersInner.md) |  | [optional] 

## Example

```python
from mencoro.models.get_available_filters200_response import GetAvailableFilters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableFilters200Response from a JSON string
get_available_filters200_response_instance = GetAvailableFilters200Response.from_json(json)
# print the JSON string representation of the object
print(GetAvailableFilters200Response.to_json())

# convert the object into a dict
get_available_filters200_response_dict = get_available_filters200_response_instance.to_dict()
# create an instance of GetAvailableFilters200Response from a dict
get_available_filters200_response_from_dict = GetAvailableFilters200Response.from_dict(get_available_filters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


