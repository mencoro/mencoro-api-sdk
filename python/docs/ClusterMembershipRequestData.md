# ClusterMembershipRequestData

The clusters a tracked query is added to or removed from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_cluster_ids** | **List[UUID]** | Ids of the query clusters. Duplicates are collapsed. Every id must belong to the project in the path. | 

## Example

```python
from mencoro.models.cluster_membership_request_data import ClusterMembershipRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMembershipRequestData from a JSON string
cluster_membership_request_data_instance = ClusterMembershipRequestData.from_json(json)
# print the JSON string representation of the object
print(ClusterMembershipRequestData.to_json())

# convert the object into a dict
cluster_membership_request_data_dict = cluster_membership_request_data_instance.to_dict()
# create an instance of ClusterMembershipRequestData from a dict
cluster_membership_request_data_from_dict = ClusterMembershipRequestData.from_dict(cluster_membership_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


