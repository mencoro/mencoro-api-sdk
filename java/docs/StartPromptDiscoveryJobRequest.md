

# StartPromptDiscoveryJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**input** | **String** | Free text describing the topics to turn into prompts. |  |
|**country** | **String** | ISO 3166-1 alpha-2 country the prompts are asked from. |  |
|**language** | **String** | Language code. Omit to let the provider detect it from the input. |  [optional] |
|**excludeQueries** | **List&lt;String&gt;** | Extra queries to keep out of the suggestions for this run. Duplicates are collapsed, after the entry count has been checked against maxItems. The project tracked queries are excluded whether or not this is sent. |  [optional] |



