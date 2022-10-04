"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.39
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_admission_sdk.api_client import ApiClient, Endpoint as _Endpoint
from osis_admission_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from osis_admission_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from osis_admission_sdk.model.error import Error
from osis_admission_sdk.model.inline_response2001 import InlineResponse2001
from osis_admission_sdk.model.inline_response2002 import InlineResponse2002
from osis_admission_sdk.model.sector_dto import SectorDTO


class AutocompleteApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_doctorat_dtos_endpoint = _Endpoint(
            settings={
                'response_type': ([DoctoratDTO],),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/autocomplete/sector/{sigle}/doctorates',
                'operation_id': 'list_doctorat_dtos',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sigle',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'sigle',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sigle':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'sigle': 'sigle',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'sigle': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_persons_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2002,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/autocomplete/person',
                'operation_id': 'list_persons',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search',
                    'limit',
                    'offset',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'search',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'search': 'search',
                    'limit': 'limit',
                    'offset': 'offset',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'search': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_sector_dtos_endpoint = _Endpoint(
            settings={
                'response_type': ([SectorDTO],),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/autocomplete/sector',
                'operation_id': 'list_sector_dtos',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tutors_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/autocomplete/tutor',
                'operation_id': 'list_tutors',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search',
                    'limit',
                    'offset',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'search',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'search': 'search',
                    'limit': 'limit',
                    'offset': 'offset',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'search': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def list_doctorat_dtos(
        self,
        sigle,
        **kwargs
    ):
        """list_doctorat_dtos  # noqa: E501

        Autocomplete doctorates given a sector  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_doctorat_dtos(sigle, async_req=True)
        >>> result = thread.get()

        Args:
            sigle (str):

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.). [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [DoctoratDTO]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['sigle'] = \
            sigle
        return self.list_doctorat_dtos_endpoint.call_with_http_info(**kwargs)

    def list_persons(
        self,
        search,
        **kwargs
    ):
        """list_persons  # noqa: E501

        Autocomplete person  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_persons(search, async_req=True)
        >>> result = thread.get()

        Args:
            search (str): The term to search the persons on (first or last name, or global id)

        Keyword Args:
            limit (int): Number of results to return per page.. [optional]
            offset (int): The initial index from which to return the results.. [optional]
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.). [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2002
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search'] = \
            search
        return self.list_persons_endpoint.call_with_http_info(**kwargs)

    def list_sector_dtos(
        self,
        **kwargs
    ):
        """list_sector_dtos  # noqa: E501

        Autocomplete sectors  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_sector_dtos(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.). [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [SectorDTO]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_sector_dtos_endpoint.call_with_http_info(**kwargs)

    def list_tutors(
        self,
        search,
        **kwargs
    ):
        """list_tutors  # noqa: E501

        Autocomplete tutors  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tutors(search, async_req=True)
        >>> result = thread.get()

        Args:
            search (str): The term to search the persons on (first or last name, or global id)

        Keyword Args:
            limit (int): Number of results to return per page.. [optional]
            offset (int): The initial index from which to return the results.. [optional]
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.). [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2001
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search'] = \
            search
        return self.list_tutors_endpoint.call_with_http_info(**kwargs)

