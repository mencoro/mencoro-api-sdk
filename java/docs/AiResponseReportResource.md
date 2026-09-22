

# AiResponseReportResource

Acknowledgement of a report about a captured AI answer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aiResponseId** | **UUID** | The captured AI answer the report is about |  |
|**trackedQueryId** | **UUID** | The tracked query that answer was captured for |  |
|**type** | [**TypeEnum**](#TypeEnum) | The kind of problem reported |  |
|**comment** | **String** | The note as stored. An empty or whitespace-only comment is stored as null. |  [optional] |
|**missedBrandNames** | **List&lt;String&gt;** | Brand names reported as missed, de-duplicated and trimmed. |  |
|**accepted** | **Boolean** | True once the report has been accepted for review. It is never false: a report that could not be delivered answers with an error instead. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MISSED_MENTION | &quot;missed_mention&quot; |
| OTHER | &quot;other&quot; |



