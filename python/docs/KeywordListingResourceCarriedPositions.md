# KeywordListingResourceCarriedPositions

Per engine family, whether the position figure includes a measurement from before the window. An active variant with no check of its engine in the window contributes the brand's position in its latest earlier capture, and nothing when the brand was absent from that capture. An entry is null when no variant behind the figure carried. Every other metric stays window-only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serp** | [**KeywordListingResourceCarriedPositionsSerp**](KeywordListingResourceCarriedPositionsSerp.md) |  | 
**shopping** | [**KeywordListingResourceCarriedPositionsSerp**](KeywordListingResourceCarriedPositionsSerp.md) |  | 
**mention** | [**KeywordListingResourceCarriedPositionsSerp**](KeywordListingResourceCarriedPositionsSerp.md) |  | 
**link** | [**KeywordListingResourceCarriedPositionsSerp**](KeywordListingResourceCarriedPositionsSerp.md) |  | 

## Example

```python
from mencoro.models.keyword_listing_resource_carried_positions import KeywordListingResourceCarriedPositions

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordListingResourceCarriedPositions from a JSON string
keyword_listing_resource_carried_positions_instance = KeywordListingResourceCarriedPositions.from_json(json)
# print the JSON string representation of the object
print(KeywordListingResourceCarriedPositions.to_json())

# convert the object into a dict
keyword_listing_resource_carried_positions_dict = keyword_listing_resource_carried_positions_instance.to_dict()
# create an instance of KeywordListingResourceCarriedPositions from a dict
keyword_listing_resource_carried_positions_from_dict = KeywordListingResourceCarriedPositions.from_dict(keyword_listing_resource_carried_positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


