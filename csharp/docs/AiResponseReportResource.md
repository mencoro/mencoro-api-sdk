# Mencoro.Api.Model.AiResponseReportResource
Acknowledgement of a report about a captured AI answer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AiResponseId** | **Guid** | The captured AI answer the report is about | 
**TrackedQueryId** | **Guid** | The tracked query that answer was captured for | 
**Type** | **string** | The kind of problem reported | 
**Comment** | **string** | The note as stored. An empty or whitespace-only comment is stored as null. | [optional] 
**MissedBrandNames** | **List&lt;string&gt;** | Brand names reported as missed, de-duplicated and trimmed. | 
**Accepted** | **bool** | True once the report has been accepted for review. It is never false: a report that could not be delivered answers with an error instead. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

