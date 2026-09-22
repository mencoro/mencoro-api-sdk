# ListCompetitors200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CompetitorResource]**](CompetitorResource.md) |  | [optional] 
**total** | **int** | Number of competitors configured on the project | [optional] 

## Example

```python
from mencoro.models.list_competitors200_response import ListCompetitors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCompetitors200Response from a JSON string
list_competitors200_response_instance = ListCompetitors200Response.from_json(json)
# print the JSON string representation of the object
print(ListCompetitors200Response.to_json())

# convert the object into a dict
list_competitors200_response_dict = list_competitors200_response_instance.to_dict()
# create an instance of ListCompetitors200Response from a dict
list_competitors200_response_from_dict = ListCompetitors200Response.from_dict(list_competitors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


