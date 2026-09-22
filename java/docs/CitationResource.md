

# CitationResource

A source cited inside one AI answer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **String** | The URL exactly as the engine cited it, redirector included when unresolved is true |  |
|**position** | **Integer** | Place within this answer, starting at 1 |  |
|**anchorText** | **String** | The visible link text, when the engine provided one |  [optional] |
|**title** | **String** | Title of the cited page, when the engine provided one |  [optional] |
|**snippet** | **String** | Excerpt the engine showed for this source, when it provided one |  [optional] |
|**publicationDate** | **String** | Publication date the engine reported, when it provided one |  [optional] |
|**thumbnailUrl** | **String** | Preview image the engine showed for this source, when it provided one |  [optional] |
|**domain** | **String** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true |  [optional] |
|**sourceName** | **String** | Publisher name the engine reported, when it provided one |  [optional] |
|**unresolved** | **Boolean** | True when url still points at a redirector: count the citation, do not attribute the domain |  |



