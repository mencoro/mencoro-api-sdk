# Mencoro.Api.Model.SearchResultResource
One organic result of a captured search page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Position** | **int** | Rank on the captured page, starting at 1 | 
**Url** | **string** | The result URL as captured, redirector included when unresolved is true | 
**Title** | **string** | Result title, when the page showed one | [optional] 
**Snippet** | **string** | Result snippet, when the page showed one | [optional] 
**Domain** | **string** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] 
**Rating** | **float?** | Star rating shown in the rich result, when there was one | [optional] 
**RatingVotes** | **int?** | Number of votes behind rating, when the rich result reported one | [optional] 
**Unresolved** | **bool** | True when url still points at a redirector: count the result, do not attribute the domain | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

