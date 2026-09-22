# CitationResource

A source cited inside one AI answer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL exactly as the engine cited it, redirector included when unresolved is true | 
**position** | **int** | Place within this answer, starting at 1 | 
**anchor_text** | **str** | The visible link text, when the engine provided one | [optional] 
**title** | **str** | Title of the cited page, when the engine provided one | [optional] 
**snippet** | **str** | Excerpt the engine showed for this source, when it provided one | [optional] 
**publication_date** | **str** | Publication date the engine reported, when it provided one | [optional] 
**thumbnail_url** | **str** | Preview image the engine showed for this source, when it provided one | [optional] 
**domain** | **str** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] 
**source_name** | **str** | Publisher name the engine reported, when it provided one | [optional] 
**unresolved** | **bool** | True when url still points at a redirector: count the citation, do not attribute the domain | 

## Example

```python
from mencoro.models.citation_resource import CitationResource

# TODO update the JSON string below
json = "{}"
# create an instance of CitationResource from a JSON string
citation_resource_instance = CitationResource.from_json(json)
# print the JSON string representation of the object
print(CitationResource.to_json())

# convert the object into a dict
citation_resource_dict = citation_resource_instance.to_dict()
# create an instance of CitationResource from a dict
citation_resource_from_dict = CitationResource.from_dict(citation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


