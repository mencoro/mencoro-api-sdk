# MeResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | **string** |  | 
**FullName** | **string** |  | 
**Email** | **string** |  | 
**Language** | **string** | IETF language tag the user reads the product in | 
**CreatedAt** | **time.Time** |  | 
**ApiKeyId** | **string** | The API key this request authenticated with | 
**Capabilities** | **[]string** |  | 
**ScopeMode** | **string** |  | 
**OrganizationIds** | **[]string** | Organizations the key names. Empty for a key scoped to all organizations, which instead follows the owner&#39;s membership. | 

## Methods

### NewMeResource

`func NewMeResource(userId string, fullName string, email string, language string, createdAt time.Time, apiKeyId string, capabilities []string, scopeMode string, organizationIds []string, ) *MeResource`

NewMeResource instantiates a new MeResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMeResourceWithDefaults

`func NewMeResourceWithDefaults() *MeResource`

NewMeResourceWithDefaults instantiates a new MeResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *MeResource) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *MeResource) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *MeResource) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetFullName

`func (o *MeResource) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *MeResource) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *MeResource) SetFullName(v string)`

SetFullName sets FullName field to given value.


### GetEmail

`func (o *MeResource) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *MeResource) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *MeResource) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetLanguage

`func (o *MeResource) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *MeResource) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *MeResource) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetCreatedAt

`func (o *MeResource) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *MeResource) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *MeResource) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetApiKeyId

`func (o *MeResource) GetApiKeyId() string`

GetApiKeyId returns the ApiKeyId field if non-nil, zero value otherwise.

### GetApiKeyIdOk

`func (o *MeResource) GetApiKeyIdOk() (*string, bool)`

GetApiKeyIdOk returns a tuple with the ApiKeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKeyId

`func (o *MeResource) SetApiKeyId(v string)`

SetApiKeyId sets ApiKeyId field to given value.


### GetCapabilities

`func (o *MeResource) GetCapabilities() []string`

GetCapabilities returns the Capabilities field if non-nil, zero value otherwise.

### GetCapabilitiesOk

`func (o *MeResource) GetCapabilitiesOk() (*[]string, bool)`

GetCapabilitiesOk returns a tuple with the Capabilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCapabilities

`func (o *MeResource) SetCapabilities(v []string)`

SetCapabilities sets Capabilities field to given value.


### GetScopeMode

`func (o *MeResource) GetScopeMode() string`

GetScopeMode returns the ScopeMode field if non-nil, zero value otherwise.

### GetScopeModeOk

`func (o *MeResource) GetScopeModeOk() (*string, bool)`

GetScopeModeOk returns a tuple with the ScopeMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopeMode

`func (o *MeResource) SetScopeMode(v string)`

SetScopeMode sets ScopeMode field to given value.


### GetOrganizationIds

`func (o *MeResource) GetOrganizationIds() []string`

GetOrganizationIds returns the OrganizationIds field if non-nil, zero value otherwise.

### GetOrganizationIdsOk

`func (o *MeResource) GetOrganizationIdsOk() (*[]string, bool)`

GetOrganizationIdsOk returns a tuple with the OrganizationIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationIds

`func (o *MeResource) SetOrganizationIds(v []string)`

SetOrganizationIds sets OrganizationIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


