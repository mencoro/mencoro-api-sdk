# SearchResultResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | Rank on the captured page, starting at 1 |
**url** | **string** | The result URL as captured, redirector included when unresolved is true |
**title** | **string** | Result title, when the page showed one | [optional]
**snippet** | **string** | Result snippet, when the page showed one | [optional]
**domain** | **string** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional]
**rating** | **float** | Star rating shown in the rich result, when there was one | [optional]
**rating_votes** | **int** | Number of votes behind rating, when the rich result reported one | [optional]
**unresolved** | **bool** | True when url still points at a redirector: count the result, do not attribute the domain |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
