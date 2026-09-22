# ShoppingOfferResource

One offer of a captured shopping page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Rank on the captured page, starting at 1 | 
**title** | **str** | Product title as the marketplace showed it | 
**product_url** | **str** | Link to the offer | 
**seller_name** | **str** | Seller name as the marketplace showed it | 
**seller_domain** | **str** | Seller host, when the marketplace reported one | [optional] 
**product_id** | **str** | The marketplace&#39;s own identifier for this listing, not a Mencoro id | 
**thumbnail_url** | **str** | Product image the marketplace showed, when it showed one | [optional] 
**price** | **float** | Price as shown at capture time: no tax normalisation, no shipping, no conversion | 
**currency** | **str** | ISO-4217 currency of price. May differ between offers in one snapshot | 
**rating** | **float** | Star rating shown for the offer, when there was one | [optional] 
**rating_votes** | **int** | Number of votes behind rating, when the marketplace reported one | [optional] 

## Example

```python
from mencoro.models.shopping_offer_resource import ShoppingOfferResource

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingOfferResource from a JSON string
shopping_offer_resource_instance = ShoppingOfferResource.from_json(json)
# print the JSON string representation of the object
print(ShoppingOfferResource.to_json())

# convert the object into a dict
shopping_offer_resource_dict = shopping_offer_resource_instance.to_dict()
# create an instance of ShoppingOfferResource from a dict
shopping_offer_resource_from_dict = ShoppingOfferResource.from_dict(shopping_offer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


