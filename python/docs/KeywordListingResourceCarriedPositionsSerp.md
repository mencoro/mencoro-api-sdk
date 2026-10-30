# KeywordListingResourceCarriedPositionsSerp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measured_at** | **date** | Date (YYYY-MM-DD) of the oldest carried measurement. | 
**all_carried** | **bool** | True when every variant behind the figure carried, so it holds no measurement from the window. | 

## Example

```python
from mencoro.models.keyword_listing_resource_carried_positions_serp import KeywordListingResourceCarriedPositionsSerp

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordListingResourceCarriedPositionsSerp from a JSON string
keyword_listing_resource_carried_positions_serp_instance = KeywordListingResourceCarriedPositionsSerp.from_json(json)
# print the JSON string representation of the object
print(KeywordListingResourceCarriedPositionsSerp.to_json())

# convert the object into a dict
keyword_listing_resource_carried_positions_serp_dict = keyword_listing_resource_carried_positions_serp_instance.to_dict()
# create an instance of KeywordListingResourceCarriedPositionsSerp from a dict
keyword_listing_resource_carried_positions_serp_from_dict = KeywordListingResourceCarriedPositionsSerp.from_dict(keyword_listing_resource_carried_positions_serp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


