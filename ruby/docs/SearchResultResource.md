# Mencoro::SearchResultResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **position** | **Integer** | Rank on the captured page, starting at 1 |  |
| **url** | **String** | The result URL as captured, redirector included when unresolved is true |  |
| **title** | **String** | Result title, when the page showed one | [optional] |
| **snippet** | **String** | Result snippet, when the page showed one | [optional] |
| **domain** | **String** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] |
| **rating** | **Float** | Star rating shown in the rich result, when there was one | [optional] |
| **rating_votes** | **Integer** | Number of votes behind rating, when the rich result reported one | [optional] |
| **unresolved** | **Boolean** | True when url still points at a redirector: count the result, do not attribute the domain |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::SearchResultResource.new(
  position: null,
  url: null,
  title: null,
  snippet: null,
  domain: null,
  rating: null,
  rating_votes: null,
  unresolved: null
)
```

