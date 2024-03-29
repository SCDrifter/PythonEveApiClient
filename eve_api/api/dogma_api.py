# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eve_api.api_client import ApiClient


class DogmaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_dogma_attributes(self, **kwargs):  # noqa: E501
        """Get attributes  # noqa: E501

        Get a list of dogma attribute ids  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_attributes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dogma_attributes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dogma_attributes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dogma_attributes_with_http_info(self, **kwargs):  # noqa: E501
        """Get attributes  # noqa: E501

        Get a list of dogma attribute ids  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_attributes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dogma_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/dogma/attributes/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dogma_attributes_attribute_id(self, attribute_id, **kwargs):  # noqa: E501
        """Get attribute information  # noqa: E501

        Get information on a dogma attribute  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_attributes_attribute_id(attribute_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int attribute_id: A dogma attribute ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetDogmaAttributesAttributeIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dogma_attributes_attribute_id_with_http_info(attribute_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dogma_attributes_attribute_id_with_http_info(attribute_id, **kwargs)  # noqa: E501
            return data

    def get_dogma_attributes_attribute_id_with_http_info(self, attribute_id, **kwargs):  # noqa: E501
        """Get attribute information  # noqa: E501

        Get information on a dogma attribute  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_attributes_attribute_id_with_http_info(attribute_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int attribute_id: A dogma attribute ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetDogmaAttributesAttributeIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attribute_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dogma_attributes_attribute_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'attribute_id' is set
        if self.api_client.client_side_validation and ('attribute_id' not in params or
                                                       params['attribute_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `attribute_id` when calling `get_dogma_attributes_attribute_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in params:
            path_params['attribute_id'] = params['attribute_id']  # noqa: E501

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
            '/v1/dogma/attributes/{attribute_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDogmaAttributesAttributeIdOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dogma_dynamic_items_type_id_item_id(self, item_id, type_id, **kwargs):  # noqa: E501
        """Get dynamic item information  # noqa: E501

        Returns info about a dynamic item resulting from mutation with a mutaplasmid.  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_dynamic_items_type_id_item_id(item_id, type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: item_id integer (required)
        :param int type_id: type_id integer (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetDogmaDynamicItemsTypeIdItemIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dogma_dynamic_items_type_id_item_id_with_http_info(item_id, type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dogma_dynamic_items_type_id_item_id_with_http_info(item_id, type_id, **kwargs)  # noqa: E501
            return data

    def get_dogma_dynamic_items_type_id_item_id_with_http_info(self, item_id, type_id, **kwargs):  # noqa: E501
        """Get dynamic item information  # noqa: E501

        Returns info about a dynamic item resulting from mutation with a mutaplasmid.  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_dynamic_items_type_id_item_id_with_http_info(item_id, type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: item_id integer (required)
        :param int type_id: type_id integer (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetDogmaDynamicItemsTypeIdItemIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'type_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dogma_dynamic_items_type_id_item_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if self.api_client.client_side_validation and ('item_id' not in params or
                                                       params['item_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `item_id` when calling `get_dogma_dynamic_items_type_id_item_id`")  # noqa: E501
        # verify the required parameter 'type_id' is set
        if self.api_client.client_side_validation and ('type_id' not in params or
                                                       params['type_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `type_id` when calling `get_dogma_dynamic_items_type_id_item_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['item_id'] = params['item_id']  # noqa: E501
        if 'type_id' in params:
            path_params['type_id'] = params['type_id']  # noqa: E501

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
            '/v1/dogma/dynamic/items/{type_id}/{item_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDogmaDynamicItemsTypeIdItemIdOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dogma_effects(self, **kwargs):  # noqa: E501
        """Get effects  # noqa: E501

        Get a list of dogma effect ids  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_effects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dogma_effects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dogma_effects_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dogma_effects_with_http_info(self, **kwargs):  # noqa: E501
        """Get effects  # noqa: E501

        Get a list of dogma effect ids  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_effects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dogma_effects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/dogma/effects/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dogma_effects_effect_id(self, effect_id, **kwargs):  # noqa: E501
        """Get effect information  # noqa: E501

        Get information on a dogma effect  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_effects_effect_id(effect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int effect_id: A dogma effect ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetDogmaEffectsEffectIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dogma_effects_effect_id_with_http_info(effect_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dogma_effects_effect_id_with_http_info(effect_id, **kwargs)  # noqa: E501
            return data

    def get_dogma_effects_effect_id_with_http_info(self, effect_id, **kwargs):  # noqa: E501
        """Get effect information  # noqa: E501

        Get information on a dogma effect  ---  This route expires daily at 11:05  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dogma_effects_effect_id_with_http_info(effect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int effect_id: A dogma effect ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: GetDogmaEffectsEffectIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['effect_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dogma_effects_effect_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'effect_id' is set
        if self.api_client.client_side_validation and ('effect_id' not in params or
                                                       params['effect_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `effect_id` when calling `get_dogma_effects_effect_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'effect_id' in params:
            path_params['effect_id'] = params['effect_id']  # noqa: E501

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
            '/v2/dogma/effects/{effect_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDogmaEffectsEffectIdOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
