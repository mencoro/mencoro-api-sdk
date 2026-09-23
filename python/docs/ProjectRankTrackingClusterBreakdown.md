# ProjectRankTrackingClusterBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[ClusterBreakdownRow]**](ClusterBreakdownRow.md) |  | 
**data_dirty_since** | **str** |  | [optional] 

## Example

```python
from mencoro.models.project_rank_tracking_cluster_breakdown import ProjectRankTrackingClusterBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRankTrackingClusterBreakdown from a JSON string
project_rank_tracking_cluster_breakdown_instance = ProjectRankTrackingClusterBreakdown.from_json(json)
# print the JSON string representation of the object
print(ProjectRankTrackingClusterBreakdown.to_json())

# convert the object into a dict
project_rank_tracking_cluster_breakdown_dict = project_rank_tracking_cluster_breakdown_instance.to_dict()
# create an instance of ProjectRankTrackingClusterBreakdown from a dict
project_rank_tracking_cluster_breakdown_from_dict = ProjectRankTrackingClusterBreakdown.from_dict(project_rank_tracking_cluster_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


