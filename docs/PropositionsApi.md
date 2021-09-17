# osis_admission_sdk.PropositionsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/admission*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proposition**](PropositionsApi.md#create_proposition) | **POST** /propositions | 
[**list_propositions**](PropositionsApi.md#list_propositions) | **GET** /propositions | 
[**retrieve_proposition**](PropositionsApi.md#retrieve_proposition) | **GET** /propositions/{uuid} | 
[**update_proposition**](PropositionsApi.md#update_proposition) | **PUT** /propositions/{uuid} | 


# **create_proposition**
> PropositionIdentityDTO create_proposition()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_admission_sdk
from osis_admission_sdk.api import propositions_api
from osis_admission_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_admission_sdk.model.initier_proposition_command import InitierPropositionCommand
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
    api_instance = propositions_api.PropositionsApi(api_client)
    initier_proposition_command = InitierPropositionCommand(
        type_admission="ADMISSION",
        sigle_formation="sigle_formation_example",
        annee_formation=1,
        matricule_candidat="matricule_candidat_example",
        justification="justification_example",
        bureau_cde="ECONOMY",
        type_financement="type_financement_example",
        type_contrat_travail="type_contrat_travail_example",
        eft=1,
        bourse_recherche="bourse_recherche_example",
        duree_prevue=1,
        temps_consacre=1,
        titre_projet="titre_projet_example",
        resume_projet="resume_projet_example",
        documents_projet=[
            "documents_projet_example",
        ],
        graphe_gantt=[],
        proposition_programme_doctoral=[],
        projet_formation_complementaire=[],
        langue_redaction_these="UNDECIDED",
        doctorat_deja_realise="NO",
        institution="institution_example",
        date_soutenance=dateutil_parser('1970-01-01').date(),
        raison_non_soutenue="raison_non_soutenue_example",
    ) # InitierPropositionCommand |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_proposition(initier_proposition_command=initier_proposition_command)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->create_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initier_proposition_command** | [**InitierPropositionCommand**](InitierPropositionCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_propositions**
> [PropositionSearchDTO] list_propositions()



### Example

* Api Key Authentication (Token):
```python
import time
import osis_admission_sdk
from osis_admission_sdk.api import propositions_api
from osis_admission_sdk.model.proposition_search_dto import PropositionSearchDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_propositions()
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->list_propositions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[PropositionSearchDTO]**](PropositionSearchDTO.md)

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

# **retrieve_proposition**
> PropositionDTO retrieve_proposition(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_admission_sdk
from osis_admission_sdk.api import propositions_api
from osis_admission_sdk.model.proposition_dto import PropositionDTO
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_proposition(uuid)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->retrieve_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |

### Return type

[**PropositionDTO**](PropositionDTO.md)

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

# **update_proposition**
> PropositionIdentityDTO update_proposition(uuid)



### Example

* Api Key Authentication (Token):
```python
import time
import osis_admission_sdk
from osis_admission_sdk.api import propositions_api
from osis_admission_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_admission_sdk.model.completer_proposition_command import CompleterPropositionCommand
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
    api_instance = propositions_api.PropositionsApi(api_client)
    uuid = "uuid_example" # str | 
    completer_proposition_command = CompleterPropositionCommand(
        uuid="uuid_example",
        type_admission="ADMISSION",
        justification="justification_example",
        bureau_cde="ECONOMY",
        type_financement="type_financement_example",
        type_contrat_travail="type_contrat_travail_example",
        eft=1,
        bourse_recherche="bourse_recherche_example",
        duree_prevue=1,
        temps_consacre=1,
        titre_projet="titre_projet_example",
        resume_projet="resume_projet_example",
        documents_projet=[
            "documents_projet_example",
        ],
        graphe_gantt=[],
        proposition_programme_doctoral=[],
        projet_formation_complementaire=[],
        langue_redaction_these="UNDECIDED",
        doctorat_deja_realise="NO",
        institution="institution_example",
        date_soutenance=dateutil_parser('1970-01-01').date(),
        raison_non_soutenue="raison_non_soutenue_example",
    ) # CompleterPropositionCommand |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_proposition(uuid)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->update_proposition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_proposition(uuid, completer_proposition_command=completer_proposition_command)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling PropositionsApi->update_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **completer_proposition_command** | [**CompleterPropositionCommand**](CompleterPropositionCommand.md)|  | [optional]

### Return type

[**PropositionIdentityDTO**](PropositionIdentityDTO.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

