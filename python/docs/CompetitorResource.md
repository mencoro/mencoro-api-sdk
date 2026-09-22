# CompetitorResource

A competitor tracked by a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** | The competitor&#39;s display name | 
**website_domains** | **List[str]** | Domains a result is matched against for this competitor | 
**brand_names** | **List[str]** | Names a mention is matched against for this competitor | 

## Example

```python
from mencoro.models.competitor_resource import CompetitorResource

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitorResource from a JSON string
competitor_resource_instance = CompetitorResource.from_json(json)
# print the JSON string representation of the object
print(CompetitorResource.to_json())

# convert the object into a dict
competitor_resource_dict = competitor_resource_instance.to_dict()
# create an instance of CompetitorResource from a dict
competitor_resource_from_dict = CompetitorResource.from_dict(competitor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


