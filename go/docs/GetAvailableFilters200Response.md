# GetAvailableFilters200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Engines** | Pointer to **[]string** | Engine codes, ready to pass as the engines filter | [optional] 
**Countries** | Pointer to **[]string** | ISO-3166 alpha-2 codes, ready to pass as the countries filter | [optional] 
**Clusters** | Pointer to [**[]GetAvailableFilters200ResponseClustersInner**](GetAvailableFilters200ResponseClustersInner.md) |  | [optional] 

## Methods

### NewGetAvailableFilters200Response

`func NewGetAvailableFilters200Response() *GetAvailableFilters200Response`

NewGetAvailableFilters200Response instantiates a new GetAvailableFilters200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetAvailableFilters200ResponseWithDefaults

`func NewGetAvailableFilters200ResponseWithDefaults() *GetAvailableFilters200Response`

NewGetAvailableFilters200ResponseWithDefaults instantiates a new GetAvailableFilters200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEngines

`func (o *GetAvailableFilters200Response) GetEngines() []string`

GetEngines returns the Engines field if non-nil, zero value otherwise.

### GetEnginesOk

`func (o *GetAvailableFilters200Response) GetEnginesOk() (*[]string, bool)`

GetEnginesOk returns a tuple with the Engines field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngines

`func (o *GetAvailableFilters200Response) SetEngines(v []string)`

SetEngines sets Engines field to given value.

### HasEngines

`func (o *GetAvailableFilters200Response) HasEngines() bool`

HasEngines returns a boolean if a field has been set.

### GetCountries

`func (o *GetAvailableFilters200Response) GetCountries() []string`

GetCountries returns the Countries field if non-nil, zero value otherwise.

### GetCountriesOk

`func (o *GetAvailableFilters200Response) GetCountriesOk() (*[]string, bool)`

GetCountriesOk returns a tuple with the Countries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountries

`func (o *GetAvailableFilters200Response) SetCountries(v []string)`

SetCountries sets Countries field to given value.

### HasCountries

`func (o *GetAvailableFilters200Response) HasCountries() bool`

HasCountries returns a boolean if a field has been set.

### GetClusters

`func (o *GetAvailableFilters200Response) GetClusters() []GetAvailableFilters200ResponseClustersInner`

GetClusters returns the Clusters field if non-nil, zero value otherwise.

### GetClustersOk

`func (o *GetAvailableFilters200Response) GetClustersOk() (*[]GetAvailableFilters200ResponseClustersInner, bool)`

GetClustersOk returns a tuple with the Clusters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusters

`func (o *GetAvailableFilters200Response) SetClusters(v []GetAvailableFilters200ResponseClustersInner)`

SetClusters sets Clusters field to given value.

### HasClusters

`func (o *GetAvailableFilters200Response) HasClusters() bool`

HasClusters returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


