# osis_admission_sdk.AutocompleteApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/admission*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_doctorat_dtos**](AutocompleteApi.md#list_doctorat_dtos) | **GET** /autocomplete/sector/{sigle}/doctorates | 
[**list_sector_dtos**](AutocompleteApi.md#list_sector_dtos) | **GET** /autocomplete/sector | 


# **list_doctorat_dtos**
> [DoctoratDTO] list_doctorat_dtos(sigle)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_admission_sdk
from osis_admission_sdk.api import autocomplete_api
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_admission_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_admission_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    sigle = "sigle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_doctorat_dtos(sigle)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling AutocompleteApi->list_doctorat_dtos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sigle** | **str**|  |

### Return type

[**[DoctoratDTO]**](DoctoratDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sector_dtos**
> [SectorDTO] list_sector_dtos()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_admission_sdk
from osis_admission_sdk.api import autocomplete_api
from osis_admission_sdk.model.sector_dto import SectorDTO
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_admission_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_admission_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autocomplete_api.AutocompleteApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_sector_dtos()
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling AutocompleteApi->list_sector_dtos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[SectorDTO]**](SectorDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
