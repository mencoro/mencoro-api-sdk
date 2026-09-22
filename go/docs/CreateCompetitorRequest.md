# CreateCompetitorRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | The competitor&#39;s display name | [optional] 
**WebsiteDomains** | Pointer to **[]string** | Domains a result is matched against for this competitor. A full URL or a bare host. | [optional] 
**BrandNames** | Pointer to **[]string** | Names a mention is matched against for this competitor | [optional] 

## Methods

### NewCreateCompetitorRequest

`func NewCreateCompetitorRequest() *CreateCompetitorRequest`

NewCreateCompetitorRequest instantiates a new CreateCompetitorRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCompetitorRequestWithDefaults

`func NewCreateCompetitorRequestWithDefaults() *CreateCompetitorRequest`

NewCreateCompetitorRequestWithDefaults instantiates a new CreateCompetitorRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateCompetitorRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateCompetitorRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateCompetitorRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CreateCompetitorRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetWebsiteDomains

`func (o *CreateCompetitorRequest) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *CreateCompetitorRequest) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *CreateCompetitorRequest) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.

### HasWebsiteDomains

`func (o *CreateCompetitorRequest) HasWebsiteDomains() bool`

HasWebsiteDomains returns a boolean if a field has been set.

### GetBrandNames

`func (o *CreateCompetitorRequest) GetBrandNames() []string`

GetBrandNames returns the BrandNames field if non-nil, zero value otherwise.

### GetBrandNamesOk

`func (o *CreateCompetitorRequest) GetBrandNamesOk() (*[]string, bool)`

GetBrandNamesOk returns a tuple with the BrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNames

`func (o *CreateCompetitorRequest) SetBrandNames(v []string)`

SetBrandNames sets BrandNames field to given value.

### HasBrandNames

`func (o *CreateCompetitorRequest) HasBrandNames() bool`

HasBrandNames returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


