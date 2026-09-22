# CreateCompetitorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The competitor&#39;s display name | [optional] 
**website_domains** | **List[str]** | Domains a result is matched against for this competitor. A full URL or a bare host. | [optional] 
**brand_names** | **List[str]** | Names a mention is matched against for this competitor | [optional] 

## Example

```python
from mencoro.models.create_competitor_request import CreateCompetitorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompetitorRequest from a JSON string
create_competitor_request_instance = CreateCompetitorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompetitorRequest.to_json())

# convert the object into a dict
create_competitor_request_dict = create_competitor_request_instance.to_dict()
# create an instance of CreateCompetitorRequest from a dict
create_competitor_request_from_dict = CreateCompetitorRequest.from_dict(create_competitor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


