# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eve_api.api_client import ApiClient


class KillmailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_killmails_recent(self, character_id, **kwargs):  # noqa: E501
        """Get a character's recent kills and losses  # noqa: E501

        Return a list of a character's kills and losses going back 90 days  ---  This route is cached for up to 300 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_killmails_recent(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdKillmailsRecent200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_killmails_recent_with_http_info(character_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_killmails_recent_with_http_info(character_id, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_killmails_recent_with_http_info(self, character_id, **kwargs):  # noqa: E501
        """Get a character's recent kills and losses  # noqa: E501

        Return a list of a character's kills and losses going back 90 days  ---  This route is cached for up to 300 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_killmails_recent_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdKillmailsRecent200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'if_none_match', 'page', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_killmails_recent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params or
                params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_killmails_recent`")  # noqa: E501

        if 'character_id' in params and params['character_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_killmails_recent`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_characters_character_id_killmails_recent`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}
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
            '/v1/characters/{character_id}/killmails/recent/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetCharactersCharacterIdKillmailsRecent200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_corporations_corporation_id_killmails_recent(self, corporation_id, **kwargs):  # noqa: E501
        """Get a corporation's recent kills and losses  # noqa: E501

        Get a list of a corporation's kills and losses going back 90 days  ---  This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Director  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_killmails_recent(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[GetCorporationsCorporationIdKillmailsRecent200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_corporations_corporation_id_killmails_recent_with_http_info(corporation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_corporations_corporation_id_killmails_recent_with_http_info(corporation_id, **kwargs)  # noqa: E501
            return data

    def get_corporations_corporation_id_killmails_recent_with_http_info(self, corporation_id, **kwargs):  # noqa: E501
        """Get a corporation's recent kills and losses  # noqa: E501

        Get a list of a corporation's kills and losses going back 90 days  ---  This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Director  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_killmails_recent_with_http_info(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[GetCorporationsCorporationIdKillmailsRecent200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'datasource', 'if_none_match', 'page', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_killmails_recent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if ('corporation_id' not in params or
                params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_killmails_recent`")  # noqa: E501

        if 'corporation_id' in params and params['corporation_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `corporation_id` when calling `get_corporations_corporation_id_killmails_recent`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_corporations_corporation_id_killmails_recent`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}
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
            '/v1/corporations/{corporation_id}/killmails/recent/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetCorporationsCorporationIdKillmailsRecent200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_killmails_killmail_id_killmail_hash(self, killmail_hash, killmail_id, **kwargs):  # noqa: E501
        """Get a single killmail  # noqa: E501

        Return a single killmail from its ID and hash  ---  This route is cached for up to 30758400 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_killmails_killmail_id_killmail_hash(killmail_hash, killmail_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str killmail_hash: The killmail hash for verification (required)
        :param int killmail_id: The killmail ID to be queried (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetKillmailsKillmailIdKillmailHashOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_killmails_killmail_id_killmail_hash_with_http_info(killmail_hash, killmail_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_killmails_killmail_id_killmail_hash_with_http_info(killmail_hash, killmail_id, **kwargs)  # noqa: E501
            return data

    def get_killmails_killmail_id_killmail_hash_with_http_info(self, killmail_hash, killmail_id, **kwargs):  # noqa: E501
        """Get a single killmail  # noqa: E501

        Return a single killmail from its ID and hash  ---  This route is cached for up to 30758400 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_killmails_killmail_id_killmail_hash_with_http_info(killmail_hash, killmail_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str killmail_hash: The killmail hash for verification (required)
        :param int killmail_id: The killmail ID to be queried (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetKillmailsKillmailIdKillmailHashOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['killmail_hash', 'killmail_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_killmails_killmail_id_killmail_hash" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'killmail_hash' is set
        if ('killmail_hash' not in params or
                params['killmail_hash'] is None):
            raise ValueError("Missing the required parameter `killmail_hash` when calling `get_killmails_killmail_id_killmail_hash`")  # noqa: E501
        # verify the required parameter 'killmail_id' is set
        if ('killmail_id' not in params or
                params['killmail_id'] is None):
            raise ValueError("Missing the required parameter `killmail_id` when calling `get_killmails_killmail_id_killmail_hash`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'killmail_hash' in params:
            path_params['killmail_hash'] = params['killmail_hash']  # noqa: E501
        if 'killmail_id' in params:
            path_params['killmail_id'] = params['killmail_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501

        header_params = {}
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
            '/v1/killmails/{killmail_id}/{killmail_hash}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetKillmailsKillmailIdKillmailHashOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
