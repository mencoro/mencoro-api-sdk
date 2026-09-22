# Mencoro.Api.Model.ProjectedMonthlyChecksResource
What an organization's current tracking configuration would consume in a month

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectedMonthlyChecks** | **int** | Checks a month of the current configuration would consume: for each ACTIVE tracked query, its runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. Never null. | 
**ActiveTrackedQueryCount** | **int** | Active tracked queries the projection was summed over, across every project of the organization, archived projects included. Paused queries are excluded from both figures. Never null. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

