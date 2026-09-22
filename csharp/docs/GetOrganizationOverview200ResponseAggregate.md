# Mencoro.Api.Model.GetOrganizationOverview200ResponseAggregate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectCount** | **int** | Active projects in the organization, the length of &#x60;projects&#x60;. | [optional] 
**ProjectsWithData** | **int** | How many of those have a share of voice; the averages below are means over the projects that report each metric, never over the ones still null. | [optional] 
**TotalTrackedQueries** | **int** |  | [optional] 
**AvgShareOfVoice** | **float?** | Null when no project reports a share of voice. | [optional] 
**AvgMentionRate** | **int?** |  | [optional] 
**AvgMentionPosition** | **float?** | 1-based rank; LOWER is better. | [optional] 
**AvgPositivityIndex** | **int?** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

