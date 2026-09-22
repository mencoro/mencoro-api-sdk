# UpdateProjectBrandProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WebsiteDomains** | Pointer to **[]string** | Domains a cited link or a search result is matched against. A full URL or a bare host. | [optional] 
**BrandNames** | Pointer to **[]string** | Terms a mention in an AI answer is matched against. | [optional] 

## Methods

### NewUpdateProjectBrandProfileRequest

`func NewUpdateProjectBrandProfileRequest() *UpdateProjectBrandProfileRequest`

NewUpdateProjectBrandProfileRequest instantiates a new UpdateProjectBrandProfileRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateProjectBrandProfileRequestWithDefaults

`func NewUpdateProjectBrandProfileRequestWithDefaults() *UpdateProjectBrandProfileRequest`

NewUpdateProjectBrandProfileRequestWithDefaults instantiates a new UpdateProjectBrandProfileRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWebsiteDomains

`func (o *UpdateProjectBrandProfileRequest) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *UpdateProjectBrandProfileRequest) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *UpdateProjectBrandProfileRequest) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.

### HasWebsiteDomains

`func (o *UpdateProjectBrandProfileRequest) HasWebsiteDomains() bool`

HasWebsiteDomains returns a boolean if a field has been set.

### GetBrandNames

`func (o *UpdateProjectBrandProfileRequest) GetBrandNames() []string`

GetBrandNames returns the BrandNames field if non-nil, zero value otherwise.

### GetBrandNamesOk

`func (o *UpdateProjectBrandProfileRequest) GetBrandNamesOk() (*[]string, bool)`

GetBrandNamesOk returns a tuple with the BrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNames

`func (o *UpdateProjectBrandProfileRequest) SetBrandNames(v []string)`

SetBrandNames sets BrandNames field to given value.

### HasBrandNames

`func (o *UpdateProjectBrandProfileRequest) HasBrandNames() bool`

HasBrandNames returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


