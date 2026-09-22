

# BatchChangeTrackedQueryPassesRequestData

Tracked queries to retune, and the passes per check to set on them

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ids** | **List&lt;UUID&gt;** | Ids of the tracked queries to change. Duplicates are collapsed. |  |
|**nPasses** | **Integer** | Passes run per check. Only an AI engine accepts more than one; a non-AI target is reported under \&quot;failed\&quot;. |  |



