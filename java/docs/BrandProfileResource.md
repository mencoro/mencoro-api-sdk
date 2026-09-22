

# BrandProfileResource

The brand identity a project's checks are matched against

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **UUID** | The project this profile belongs to |  |
|**brandNames** | **List&lt;String&gt;** | The brand terms a mention in an AI answer is matched against. Empty when none has been configured yet. |  |
|**websiteDomains** | **List&lt;String&gt;** | The domains a cited link or a search result is matched against. Empty when none has been configured yet. |  |
|**description** | **String** | What the brand does, as generated from its names and domains. Null means it has not been generated yet, which is not the same as an empty description. |  [optional] |



