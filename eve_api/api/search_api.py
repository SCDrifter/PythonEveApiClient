# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eve_api.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_search(self, categories, character_id, search, **kwargs):  # noqa: E501
        """Search on a string  # noqa: E501

        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_search(categories, character_id, search, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] categories: Type of entities to search for (required)
        :param int character_id: An EVE character ID (required)
        :param str search: The string to search on (required)
        :param str accept_language: Language to use in the response
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str language: Language to use in the response, takes precedence over Accept-Language
        :param bool strict: Whether the search should be a strict match
        :param str token: Access token to use if unable to set a header
        :return: GetCharactersCharacterIdSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_search_with_http_info(categories, character_id, search, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_search_with_http_info(categories, character_id, search, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_search_with_http_info(self, categories, character_id, search, **kwargs):  # noqa: E501
        """Search on a string  # noqa: E501

        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_search_with_http_info(categories, character_id, search, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] categories: Type of entities to search for (required)
        :param int character_id: An EVE character ID (required)
        :param str search: The string to search on (required)
        :param str accept_language: Language to use in the response
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str language: Language to use in the response, takes precedence over Accept-Language
        :param bool strict: Whether the search should be a strict match
        :param str token: Access token to use if unable to set a header
        :return: GetCharactersCharacterIdSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['categories', 'character_id', 'search', 'accept_language', 'datasource', 'if_none_match', 'language', 'strict', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'categories' is set
        if ('categories' not in params or
                params['categories'] is None):
            raise ValueError("Missing the required parameter `categories` when calling `get_characters_character_id_search`")  # noqa: E501
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params or
                params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_search`")  # noqa: E501
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `get_characters_character_id_search`")  # noqa: E501

        if ('categories' in params and
                len(params['categories']) > 11):
            raise ValueError("Invalid value for parameter `categories` when calling `get_characters_character_id_search`, number of items must be less than or equal to `11`")  # noqa: E501
        if ('categories' in params and
                len(params['categories']) < 1):
            raise ValueError("Invalid value for parameter `categories` when calling `get_characters_character_id_search`, number of items must be greater than or equal to `1`")  # noqa: E501
        if 'character_id' in params and params['character_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_search`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('search' in params and
                len(params['search']) < 3):
            raise ValueError("Invalid value for parameter `search` when calling `get_characters_character_id_search`, length must be greater than or equal to `3`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501

        query_params = []
        if 'categories' in params:
            query_params.append(('categories', params['categories']))  # noqa: E501
            collection_formats['categories'] = 'csv'  # noqa: E501
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'strict' in params:
            query_params.append(('strict', params['strict']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['evesso']  # noqa: E501

        return self.api_client.call_api(
            '/v3/characters/{character_id}/search/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCharactersCharacterIdSearchOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search(self, categories, search, **kwargs):  # noqa: E501
        """Search on a string  # noqa: E501

        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search(categories, search, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] categories: Type of entities to search for (required)
        :param str search: The string to search on (required)
        :param str accept_language: Language to use in the response
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str language: Language to use in the response, takes precedence over Accept-Language
        :param bool strict: Whether the search should be a strict match
        :return: GetSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_search_with_http_info(categories, search, **kwargs)  # noqa: E501
        else:
            (data) = self.get_search_with_http_info(categories, search, **kwargs)  # noqa: E501
            return data

    def get_search_with_http_info(self, categories, search, **kwargs):  # noqa: E501
        """Search on a string  # noqa: E501

        Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_with_http_info(categories, search, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] categories: Type of entities to search for (required)
        :param str search: The string to search on (required)
        :param str accept_language: Language to use in the response
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str language: Language to use in the response, takes precedence over Accept-Language
        :param bool strict: Whether the search should be a strict match
        :return: GetSearchOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['categories', 'search', 'accept_language', 'datasource', 'if_none_match', 'language', 'strict']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'categories' is set
        if ('categories' not in params or
                params['categories'] is None):
            raise ValueError("Missing the required parameter `categories` when calling `get_search`")  # noqa: E501
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `get_search`")  # noqa: E501

        if ('categories' in params and
                len(params['categories']) > 10):
            raise ValueError("Invalid value for parameter `categories` when calling `get_search`, number of items must be less than or equal to `10`")  # noqa: E501
        if ('categories' in params and
                len(params['categories']) < 1):
            raise ValueError("Invalid value for parameter `categories` when calling `get_search`, number of items must be greater than or equal to `1`")  # noqa: E501
        if ('search' in params and
                len(params['search']) < 3):
            raise ValueError("Invalid value for parameter `search` when calling `get_search`, length must be greater than or equal to `3`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'categories' in params:
            query_params.append(('categories', params['categories']))  # noqa: E501
            collection_formats['categories'] = 'csv'  # noqa: E501
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'strict' in params:
            query_params.append(('strict', params['strict']))  # noqa: E501

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/search/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSearchOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
