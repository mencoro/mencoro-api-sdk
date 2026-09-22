# ShoppingSnapshotResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**ProjectId** | **string** | The project this capture belongs to | 
**TrackedQueryId** | **string** | The tracked query that was searched | 
**Engine** | **string** | The shopping surface that was captured | 
**Offers** | [**[]ShoppingOfferResource**](ShoppingOfferResource.md) | Offers in rank order | 
**CapturedAt** | **time.Time** | When the page was captured, UTC | 

## Methods

### NewShoppingSnapshotResource

`func NewShoppingSnapshotResource(id string, projectId string, trackedQueryId string, engine string, offers []ShoppingOfferResource, capturedAt time.Time, ) *ShoppingSnapshotResource`

NewShoppingSnapshotResource instantiates a new ShoppingSnapshotResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShoppingSnapshotResourceWithDefaults

`func NewShoppingSnapshotResourceWithDefaults() *ShoppingSnapshotResource`

NewShoppingSnapshotResourceWithDefaults instantiates a new ShoppingSnapshotResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ShoppingSnapshotResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ShoppingSnapshotResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ShoppingSnapshotResource) SetId(v string)`

SetId sets Id field to given value.


### GetProjectId

`func (o *ShoppingSnapshotResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *ShoppingSnapshotResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *ShoppingSnapshotResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetTrackedQueryId

`func (o *ShoppingSnapshotResource) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *ShoppingSnapshotResource) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *ShoppingSnapshotResource) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetEngine

`func (o *ShoppingSnapshotResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *ShoppingSnapshotResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *ShoppingSnapshotResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetOffers

`func (o *ShoppingSnapshotResource) GetOffers() []ShoppingOfferResource`

GetOffers returns the Offers field if non-nil, zero value otherwise.

### GetOffersOk

`func (o *ShoppingSnapshotResource) GetOffersOk() (*[]ShoppingOfferResource, bool)`

GetOffersOk returns a tuple with the Offers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffers

`func (o *ShoppingSnapshotResource) SetOffers(v []ShoppingOfferResource)`

SetOffers sets Offers field to given value.


### GetCapturedAt

`func (o *ShoppingSnapshotResource) GetCapturedAt() time.Time`

GetCapturedAt returns the CapturedAt field if non-nil, zero value otherwise.

### GetCapturedAtOk

`func (o *ShoppingSnapshotResource) GetCapturedAtOk() (*time.Time, bool)`

GetCapturedAtOk returns a tuple with the CapturedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCapturedAt

`func (o *ShoppingSnapshotResource) SetCapturedAt(v time.Time)`

SetCapturedAt sets CapturedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


