

# TrackedQueryCountResource

How many tracked queries a project has, and what checking them would cost in budget units

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Tracked queries in the project matching the status filter. Every status when none was sent. |  |
|**checkCost** | **Integer** | Budget cost of force-checking exactly those tracked queries, in check budget units: the sum of each one&#39;s configured passes. One unit per pass, the same unit the plan allowance is counted in. Reserves nothing and debits nothing. |  |



