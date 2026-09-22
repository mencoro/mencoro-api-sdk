

# SubmittedChecksResource

The tracked queries submitted for an immediate check

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**submitted** | **Integer** | How many tracked queries were submitted. Zero is a valid answer: it means nothing in the project was eligible. |  |
|**trackedQueryIds** | **List&lt;UUID&gt;** | The tracked queries submitted, in the order they were submitted (least recently checked first). Poll these to follow progress. |  |



