# ListKeywordListings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[KeywordListingResource]**](KeywordListingResource.md) |  | [optional] 
**total** | **int** | Keywords matching the filters, not the size of this page. | [optional] 
**total_variant_count** | **int** | Tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60;. With a text search applied this still counts the whole project, so it is not a budget figure for a searched page. | [optional] 
**data_dirty_since** | **datetime** | When a pending recalculation was triggered. Null when the metrics are up to date. | [optional] 

## Example

```python
from mencoro.models.list_keyword_listings200_response import ListKeywordListings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListKeywordListings200Response from a JSON string
list_keyword_listings200_response_instance = ListKeywordListings200Response.from_json(json)
# print the JSON string representation of the object
print(ListKeywordListings200Response.to_json())

# convert the object into a dict
list_keyword_listings200_response_dict = list_keyword_listings200_response_instance.to_dict()
# create an instance of ListKeywordListings200Response from a dict
list_keyword_listings200_response_from_dict = ListKeywordListings200Response.from_dict(list_keyword_listings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


