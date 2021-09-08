# osis_admission_sdk.PropositionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proposition**](PropositionsApi.md#create_proposition) | **POST** /propositions | 
[**list_proposition**](PropositionsApi.md#list_proposition) | **GET** /propositions | 
[**retrieve_proposition**](PropositionsApi.md#retrieve_proposition) | **GET** /propositions/{uuid} | 
[**update_proposition**](PropositionsApi.md#update_proposition) | **PUT** /propositions/{uuid} | 


# **create_proposition**
> PropositionIdentityDTO create_proposition(initier_proposition_command=initier_proposition_command)



### Example
```python
from __future__ import print_function
import time
import osis_admission_sdk
from osis_admission_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = osis_admission_sdk.PropositionsApi()
initier_proposition_command = osis_admission_sdk.InitierPropositionCommand() # InitierPropositionCommand |  (optional)

try:
    api_response = api_instance.create_proposition(initier_proposition_command=initier_proposition_command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropositionsApi->create_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initier_proposition_command** | [**InitierPropositionCommand**](InitierPropositionCommand.md)|  | [optional] 

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_proposition**
> list[PropositionDTO] list_proposition()



### Example
```python
from __future__ import print_function
import time
import osis_admission_sdk
from osis_admission_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = osis_admission_sdk.PropositionsApi()

try:
    api_response = api_instance.list_proposition()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropositionsApi->list_proposition: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PropositionDTO]**](PropositionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_proposition**
> PropositionDTO retrieve_proposition(uuid)



### Example
```python
from __future__ import print_function
import time
import osis_admission_sdk
from osis_admission_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = osis_admission_sdk.PropositionsApi()
uuid = 'uuid_example' # str | 

try:
    api_response = api_instance.retrieve_proposition(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropositionsApi->retrieve_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**PropositionDTO**](PropositionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proposition**
> InitierPropositionCommand update_proposition(uuid, initier_proposition_command=initier_proposition_command)



### Example
```python
from __future__ import print_function
import time
import osis_admission_sdk
from osis_admission_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = osis_admission_sdk.PropositionsApi()
uuid = 'uuid_example' # str | 
initier_proposition_command = osis_admission_sdk.InitierPropositionCommand() # InitierPropositionCommand |  (optional)

try:
    api_response = api_instance.update_proposition(uuid, initier_proposition_command=initier_proposition_command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropositionsApi->update_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **initier_proposition_command** | [**InitierPropositionCommand**](InitierPropositionCommand.md)|  | [optional] 

### Return type

[**InitierPropositionCommand**](InitierPropositionCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

