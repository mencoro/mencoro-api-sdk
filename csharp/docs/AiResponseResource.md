# Mencoro.Api.Model.AiResponseResource
One captured AI answer with its citations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**ProjectId** | **Guid** | The project this capture belongs to | 
**TrackedQueryId** | **Guid** | The tracked query that was asked | 
**Engine** | **string** | The AI engine that answered | 
**ResponseText** | **string** | The full answer text as the engine produced it | 
**Citations** | [**List&lt;CitationResource&gt;**](CitationResource.md) | Sources the engine cited, in the order it cited them | 
**CapturedAt** | **DateTime** | When the answer was captured, UTC | 
**ModelName** | **string** | Engine-reported model, when it reported one. Absent on captures taken before engines exposed it | [optional] 
**PassIndex** | **int** | Which sampling pass of the run this answer is, starting at 0 | 
**PassCount** | **int** | How many passes that run took. Rows of one run share trackedQueryId and capturedAt | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

