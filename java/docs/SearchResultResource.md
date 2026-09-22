

# SearchResultResource

One organic result of a captured search page

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**position** | **Integer** | Rank on the captured page, starting at 1 |  |
|**url** | **String** | The result URL as captured, redirector included when unresolved is true |  |
|**title** | **String** | Result title, when the page showed one |  [optional] |
|**snippet** | **String** | Result snippet, when the page showed one |  [optional] |
|**domain** | **String** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true |  [optional] |
|**rating** | **Float** | Star rating shown in the rich result, when there was one |  [optional] |
|**ratingVotes** | **Integer** | Number of votes behind rating, when the rich result reported one |  [optional] |
|**unresolved** | **Boolean** | True when url still points at a redirector: count the result, do not attribute the domain |  |



