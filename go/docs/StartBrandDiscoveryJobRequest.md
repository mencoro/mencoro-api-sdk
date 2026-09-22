# StartBrandDiscoveryJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShoppingEnabled** | Pointer to **bool** | Adds a shopping discovery pass. Set it only for a project that tracks a shopping engine: on any other project the pass spends provider budget on results nothing will use. | [optional] [default to false]
**Country** | Pointer to **NullableString** | ISO 3166-1 alpha-2 country used to localize the discovery. | [optional] 

## Methods

### NewStartBrandDiscoveryJobRequest

`func NewStartBrandDiscoveryJobRequest() *StartBrandDiscoveryJobRequest`

NewStartBrandDiscoveryJobRequest instantiates a new StartBrandDiscoveryJobRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStartBrandDiscoveryJobRequestWithDefaults

`func NewStartBrandDiscoveryJobRequestWithDefaults() *StartBrandDiscoveryJobRequest`

NewStartBrandDiscoveryJobRequestWithDefaults instantiates a new StartBrandDiscoveryJobRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShoppingEnabled

`func (o *StartBrandDiscoveryJobRequest) GetShoppingEnabled() bool`

GetShoppingEnabled returns the ShoppingEnabled field if non-nil, zero value otherwise.

### GetShoppingEnabledOk

`func (o *StartBrandDiscoveryJobRequest) GetShoppingEnabledOk() (*bool, bool)`

GetShoppingEnabledOk returns a tuple with the ShoppingEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingEnabled

`func (o *StartBrandDiscoveryJobRequest) SetShoppingEnabled(v bool)`

SetShoppingEnabled sets ShoppingEnabled field to given value.

### HasShoppingEnabled

`func (o *StartBrandDiscoveryJobRequest) HasShoppingEnabled() bool`

HasShoppingEnabled returns a boolean if a field has been set.

### GetCountry

`func (o *StartBrandDiscoveryJobRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *StartBrandDiscoveryJobRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *StartBrandDiscoveryJobRequest) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *StartBrandDiscoveryJobRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *StartBrandDiscoveryJobRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *StartBrandDiscoveryJobRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


