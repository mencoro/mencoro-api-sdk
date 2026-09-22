# GetMeStats200ResponseOrganizations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Organizations the caller is an active member of, within the key&#39;s scope. | [optional] 

## Example

```python
from mencoro.models.get_me_stats200_response_organizations import GetMeStats200ResponseOrganizations

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeStats200ResponseOrganizations from a JSON string
get_me_stats200_response_organizations_instance = GetMeStats200ResponseOrganizations.from_json(json)
# print the JSON string representation of the object
print(GetMeStats200ResponseOrganizations.to_json())

# convert the object into a dict
get_me_stats200_response_organizations_dict = get_me_stats200_response_organizations_instance.to_dict()
# create an instance of GetMeStats200ResponseOrganizations from a dict
get_me_stats200_response_organizations_from_dict = GetMeStats200ResponseOrganizations.from_dict(get_me_stats200_response_organizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


