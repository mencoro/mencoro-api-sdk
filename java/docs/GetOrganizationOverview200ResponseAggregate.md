

# GetOrganizationOverview200ResponseAggregate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectCount** | **Integer** | Active projects in the organization, the length of &#x60;projects&#x60;. |  [optional] |
|**projectsWithData** | **Integer** | How many of those have a share of voice; the averages below are means over the projects that report each metric, never over the ones still null. |  [optional] |
|**totalTrackedQueries** | **Integer** |  |  [optional] |
|**avgShareOfVoice** | **Float** | Null when no project reports a share of voice. |  [optional] |
|**avgMentionRate** | **Integer** |  |  [optional] |
|**avgMentionPosition** | **Float** | 1-based rank; LOWER is better. |  [optional] |
|**avgPositivityIndex** | **Integer** |  |  [optional] |



