# Mencoro.Api.Model.CitationResource
A source cited inside one AI answer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | The URL exactly as the engine cited it, redirector included when unresolved is true | 
**Position** | **int** | Place within this answer, starting at 1 | 
**AnchorText** | **string** | The visible link text, when the engine provided one | [optional] 
**Title** | **string** | Title of the cited page, when the engine provided one | [optional] 
**Snippet** | **string** | Excerpt the engine showed for this source, when it provided one | [optional] 
**PublicationDate** | **string** | Publication date the engine reported, when it provided one | [optional] 
**ThumbnailUrl** | **string** | Preview image the engine showed for this source, when it provided one | [optional] 
**Domain** | **string** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] 
**SourceName** | **string** | Publisher name the engine reported, when it provided one | [optional] 
**Unresolved** | **bool** | True when url still points at a redirector: count the citation, do not attribute the domain | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

