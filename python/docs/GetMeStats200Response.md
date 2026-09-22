# GetMeStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**GetMeStats200ResponseOrganizations**](GetMeStats200ResponseOrganizations.md) |  | [optional] 
**projects** | [**GetMeStats200ResponseProjects**](GetMeStats200ResponseProjects.md) |  | [optional] 

## Example

```python
from mencoro.models.get_me_stats200_response import GetMeStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeStats200Response from a JSON string
get_me_stats200_response_instance = GetMeStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetMeStats200Response.to_json())

# convert the object into a dict
get_me_stats200_response_dict = get_me_stats200_response_instance.to_dict()
# create an instance of GetMeStats200Response from a dict
get_me_stats200_response_from_dict = GetMeStats200Response.from_dict(get_me_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


