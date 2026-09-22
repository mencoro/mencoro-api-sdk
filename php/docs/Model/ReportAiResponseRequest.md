# ReportAiResponseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **string** | What is wrong with the capture. |
**comment** | **string** | Optional note for the reviewer, at most 1000 characters. An empty string is stored as no comment. | [optional]
**missed_brand_names** | **string[]** | Brands the engine mentioned that the pipeline did not record. Most useful with type \&quot;missed_mention\&quot;; accepted with either. At most 50 distinct names of 255 characters each. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
