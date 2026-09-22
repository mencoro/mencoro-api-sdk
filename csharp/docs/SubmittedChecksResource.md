# Mencoro.Api.Model.SubmittedChecksResource
The tracked queries submitted for an immediate check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Submitted** | **int** | How many tracked queries were submitted. Zero is a valid answer: it means nothing in the project was eligible. | 
**TrackedQueryIds** | **List&lt;Guid&gt;** | The tracked queries submitted, in the order they were submitted (least recently checked first). Poll these to follow progress. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

