# Mencoro.Api.Model.AcceptedJobResource
Background work accepted for processing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobId** | **Guid** | The job to poll. May name a job started by an earlier, equivalent request. | 
**Deduplicated** | **bool** | Whether this call started the job, or joined one that was already running | 
**TrackingUrl** | **string** | Poll this until the job reaches a terminal status | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

