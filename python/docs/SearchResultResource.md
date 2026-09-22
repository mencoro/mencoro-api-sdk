# SearchResultResource

One organic result of a captured search page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | Rank on the captured page, starting at 1 | 
**url** | **str** | The result URL as captured, redirector included when unresolved is true | 
**title** | **str** | Result title, when the page showed one | [optional] 
**snippet** | **str** | Result snippet, when the page showed one | [optional] 
**domain** | **str** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] 
**rating** | **float** | Star rating shown in the rich result, when there was one | [optional] 
**rating_votes** | **int** | Number of votes behind rating, when the rich result reported one | [optional] 
**unresolved** | **bool** | True when url still points at a redirector: count the result, do not attribute the domain | 

## Example

```python
from mencoro.models.search_result_resource import SearchResultResource

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultResource from a JSON string
search_result_resource_instance = SearchResultResource.from_json(json)
# print the JSON string representation of the object
print(SearchResultResource.to_json())

# convert the object into a dict
search_result_resource_dict = search_result_resource_instance.to_dict()
# create an instance of SearchResultResource from a dict
search_result_resource_from_dict = SearchResultResource.from_dict(search_result_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


