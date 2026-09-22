# CitationResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **string** | The URL exactly as the engine cited it, redirector included when unresolved is true |
**position** | **int** | Place within this answer, starting at 1 |
**anchor_text** | **string** | The visible link text, when the engine provided one | [optional]
**title** | **string** | Title of the cited page, when the engine provided one | [optional]
**snippet** | **string** | Excerpt the engine showed for this source, when it provided one | [optional]
**publication_date** | **string** | Publication date the engine reported, when it provided one | [optional]
**thumbnail_url** | **string** | Preview image the engine showed for this source, when it provided one | [optional]
**domain** | **string** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional]
**source_name** | **string** | Publisher name the engine reported, when it provided one | [optional]
**unresolved** | **bool** | True when url still points at a redirector: count the citation, do not attribute the domain |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
