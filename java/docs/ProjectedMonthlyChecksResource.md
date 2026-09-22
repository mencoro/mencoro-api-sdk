

# ProjectedMonthlyChecksResource

What an organization's current tracking configuration would consume in a month

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectedMonthlyChecks** | **Integer** | Checks a month of the current configuration would consume: for each ACTIVE tracked query, its runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. Never null. |  |
|**activeTrackedQueryCount** | **Integer** | Active tracked queries the projection was summed over, across every project of the organization, archived projects included. Paused queries are excluded from both figures. Never null. |  |



