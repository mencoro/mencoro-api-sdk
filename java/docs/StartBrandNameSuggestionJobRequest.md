

# StartBrandNameSuggestionJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The display name of the entity to find aliases for. |  |
|**websiteDomains** | **List&lt;String&gt;** | The entity website domains. At least one is required: the web search is grounded on them, and without one the name alone is ambiguous. Duplicates are collapsed, after the entry count has been checked against maxItems. |  |
|**enteredBrandNames** | **List&lt;String&gt;** | Names already known, excluded from the suggestions. Duplicates are collapsed, after the entry count has been checked against maxItems. |  [optional] |
|**country** | **String** | ISO 3166-1 alpha-2 country used to localize the web search. |  [optional] |



