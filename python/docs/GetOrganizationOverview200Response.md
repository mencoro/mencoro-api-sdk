# GetOrganizationOverview200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[GetOrganizationOverview200ResponseProjectsInner]**](GetOrganizationOverview200ResponseProjectsInner.md) |  | [optional] 
**aggregate** | [**GetOrganizationOverview200ResponseAggregate**](GetOrganizationOverview200ResponseAggregate.md) |  | [optional] 

## Example

```python
from mencoro.models.get_organization_overview200_response import GetOrganizationOverview200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationOverview200Response from a JSON string
get_organization_overview200_response_instance = GetOrganizationOverview200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationOverview200Response.to_json())

# convert the object into a dict
get_organization_overview200_response_dict = get_organization_overview200_response_instance.to_dict()
# create an instance of GetOrganizationOverview200Response from a dict
get_organization_overview200_response_from_dict = GetOrganizationOverview200Response.from_dict(get_organization_overview200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


