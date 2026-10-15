

# TrackedQueryCountResource

How many tracked queries a project has, and what checking them would consume in checks

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Tracked queries in the project matching the status filter. Every status when none was sent. |  |
|**checkCost** | **Integer** | Budget cost of force-checking exactly those tracked queries, in checks: the sum of each one&#39;s configured passes multiplied by its engine weight. Five checks per Claude pass and one check per pass for every other engine, the same currency as the plan allowance. Reserves nothing and debits nothing. |  |



