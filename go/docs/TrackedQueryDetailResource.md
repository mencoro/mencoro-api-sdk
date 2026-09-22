# TrackedQueryDetailResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**ProjectId** | **string** | The project this tracked query belongs to | 
**QueryText** | **string** | The prompt or keyword sent to the engine | 
**Engine** | **string** |  | 
**Locale** | Pointer to **NullableString** | Language tag the query is asked in. Null when the engine is asked without one. | [optional] 
**Country** | **string** | ISO-3166 alpha-2 country the query is asked from | 
**QueryClusterIds** | **[]string** | Clusters (groups) this query belongs to. Empty when it is ungrouped. | 
**Status** | **string** |  | 
**CheckFrequency** | **string** | How often the query is checked while active | 
**NPasses** | **int32** | Passes run per check. Greater than 1 only for AI engines. | 
**LastCheckedAt** | Pointer to **NullableTime** | When a check last completed. Null means no check has completed yet, which is not the same as a check that found nothing. | [optional] 

## Methods

### NewTrackedQueryDetailResource

`func NewTrackedQueryDetailResource(id string, projectId string, queryText string, engine string, country string, queryClusterIds []string, status string, checkFrequency string, nPasses int32, ) *TrackedQueryDetailResource`

NewTrackedQueryDetailResource instantiates a new TrackedQueryDetailResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryDetailResourceWithDefaults

`func NewTrackedQueryDetailResourceWithDefaults() *TrackedQueryDetailResource`

NewTrackedQueryDetailResourceWithDefaults instantiates a new TrackedQueryDetailResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TrackedQueryDetailResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TrackedQueryDetailResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TrackedQueryDetailResource) SetId(v string)`

SetId sets Id field to given value.


### GetProjectId

`func (o *TrackedQueryDetailResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *TrackedQueryDetailResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *TrackedQueryDetailResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetQueryText

`func (o *TrackedQueryDetailResource) GetQueryText() string`

GetQueryText returns the QueryText field if non-nil, zero value otherwise.

### GetQueryTextOk

`func (o *TrackedQueryDetailResource) GetQueryTextOk() (*string, bool)`

GetQueryTextOk returns a tuple with the QueryText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryText

`func (o *TrackedQueryDetailResource) SetQueryText(v string)`

SetQueryText sets QueryText field to given value.


### GetEngine

`func (o *TrackedQueryDetailResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *TrackedQueryDetailResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *TrackedQueryDetailResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetLocale

`func (o *TrackedQueryDetailResource) GetLocale() string`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *TrackedQueryDetailResource) GetLocaleOk() (*string, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocale

`func (o *TrackedQueryDetailResource) SetLocale(v string)`

SetLocale sets Locale field to given value.

### HasLocale

`func (o *TrackedQueryDetailResource) HasLocale() bool`

HasLocale returns a boolean if a field has been set.

### SetLocaleNil

`func (o *TrackedQueryDetailResource) SetLocaleNil(b bool)`

 SetLocaleNil sets the value for Locale to be an explicit nil

### UnsetLocale
`func (o *TrackedQueryDetailResource) UnsetLocale()`

UnsetLocale ensures that no value is present for Locale, not even an explicit nil
### GetCountry

`func (o *TrackedQueryDetailResource) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *TrackedQueryDetailResource) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *TrackedQueryDetailResource) SetCountry(v string)`

SetCountry sets Country field to given value.


### GetQueryClusterIds

`func (o *TrackedQueryDetailResource) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *TrackedQueryDetailResource) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *TrackedQueryDetailResource) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.


### GetStatus

`func (o *TrackedQueryDetailResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TrackedQueryDetailResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TrackedQueryDetailResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCheckFrequency

`func (o *TrackedQueryDetailResource) GetCheckFrequency() string`

GetCheckFrequency returns the CheckFrequency field if non-nil, zero value otherwise.

### GetCheckFrequencyOk

`func (o *TrackedQueryDetailResource) GetCheckFrequencyOk() (*string, bool)`

GetCheckFrequencyOk returns a tuple with the CheckFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckFrequency

`func (o *TrackedQueryDetailResource) SetCheckFrequency(v string)`

SetCheckFrequency sets CheckFrequency field to given value.


### GetNPasses

`func (o *TrackedQueryDetailResource) GetNPasses() int32`

GetNPasses returns the NPasses field if non-nil, zero value otherwise.

### GetNPassesOk

`func (o *TrackedQueryDetailResource) GetNPassesOk() (*int32, bool)`

GetNPassesOk returns a tuple with the NPasses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNPasses

`func (o *TrackedQueryDetailResource) SetNPasses(v int32)`

SetNPasses sets NPasses field to given value.


### GetLastCheckedAt

`func (o *TrackedQueryDetailResource) GetLastCheckedAt() time.Time`

GetLastCheckedAt returns the LastCheckedAt field if non-nil, zero value otherwise.

### GetLastCheckedAtOk

`func (o *TrackedQueryDetailResource) GetLastCheckedAtOk() (*time.Time, bool)`

GetLastCheckedAtOk returns a tuple with the LastCheckedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCheckedAt

`func (o *TrackedQueryDetailResource) SetLastCheckedAt(v time.Time)`

SetLastCheckedAt sets LastCheckedAt field to given value.

### HasLastCheckedAt

`func (o *TrackedQueryDetailResource) HasLastCheckedAt() bool`

HasLastCheckedAt returns a boolean if a field has been set.

### SetLastCheckedAtNil

`func (o *TrackedQueryDetailResource) SetLastCheckedAtNil(b bool)`

 SetLastCheckedAtNil sets the value for LastCheckedAt to be an explicit nil

### UnsetLastCheckedAt
`func (o *TrackedQueryDetailResource) UnsetLastCheckedAt()`

UnsetLastCheckedAt ensures that no value is present for LastCheckedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


