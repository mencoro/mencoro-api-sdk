# AiResponseReportResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_response_id** | **string** | The captured AI answer the report is about |
**tracked_query_id** | **string** | The tracked query that answer was captured for |
**type** | **string** | The kind of problem reported |
**comment** | **string** | The note as stored. An empty or whitespace-only comment is stored as null. | [optional]
**missed_brand_names** | **string[]** | Brand names reported as missed, de-duplicated and trimmed. |
**accepted** | **bool** | True once the report has been accepted for review. It is never false: a report that could not be delivered answers with an error instead. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
