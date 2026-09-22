# Mencoro.Api.Model.ReportAiResponseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | What is wrong with the capture. | 
**Comment** | **string** | Optional note for the reviewer, at most 1000 characters. An empty string is stored as no comment. | [optional] 
**MissedBrandNames** | **List&lt;string&gt;** | Brands the engine mentioned that the pipeline did not record. Most useful with type \&quot;missed_mention\&quot;; accepted with either. At most 50 distinct names of 255 characters each. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

