# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.3.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eve_api.api_client import ApiClient


class RoutesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_route_origin_destination(self, destination, origin, **kwargs):  # noqa: E501
        """Get route  # noqa: E501

        Get the systems between origin and destination  ---  This route is cached for up to 86400 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_route_origin_destination(destination, origin, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int destination: destination solar system ID (required)
        :param int origin: origin solar system ID (required)
        :param list[int] avoid: avoid solar system ID(s)
        :param list[list[int]] connections: connected solar system pairs
        :param str datasource: The server name you would like data from
        :param str flag: route security preference
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_route_origin_destination_with_http_info(destination, origin, **kwargs)  # noqa: E501
        else:
            (data) = self.get_route_origin_destination_with_http_info(destination, origin, **kwargs)  # noqa: E501
            return data

    def get_route_origin_destination_with_http_info(self, destination, origin, **kwargs):  # noqa: E501
        """Get route  # noqa: E501

        Get the systems between origin and destination  ---  This route is cached for up to 86400 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_route_origin_destination_with_http_info(destination, origin, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int destination: destination solar system ID (required)
        :param int origin: origin solar system ID (required)
        :param list[int] avoid: avoid solar system ID(s)
        :param list[list[int]] connections: connected solar system pairs
        :param str datasource: The server name you would like data from
        :param str flag: route security preference
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['destination', 'origin', 'avoid', 'connections', 'datasource', 'flag', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_route_origin_destination" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'destination' is set
        if ('destination' not in params or
                params['destination'] is None):
            raise ValueError("Missing the required parameter `destination` when calling `get_route_origin_destination`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if ('origin' not in params or
                params['origin'] is None):
            raise ValueError("Missing the required parameter `origin` when calling `get_route_origin_destination`")  # noqa: E501

        if ('avoid' in params and
                len(params['avoid']) > 100):
            raise ValueError("Invalid value for parameter `avoid` when calling `get_route_origin_destination`, number of items must be less than or equal to `100`")  # noqa: E501
        if ('connections' in params and
                len(params['connections']) > 100):
            raise ValueError("Invalid value for parameter `connections` when calling `get_route_origin_destination`, number of items must be less than or equal to `100`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'destination' in params:
            path_params['destination'] = params['destination']  # noqa: E501
        if 'origin' in params:
            path_params['origin'] = params['origin']  # noqa: E501

        query_params = []
        if 'avoid' in params:
            query_params.append(('avoid', params['avoid']))  # noqa: E501
            collection_formats['avoid'] = 'csv'  # noqa: E501
        if 'connections' in params:
            query_params.append(('connections', params['connections']))  # noqa: E501
            collection_formats['connections'] = 'csv'  # noqa: E501
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'flag' in params:
            query_params.append(('flag', params['flag']))  # noqa: E501

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
            '/v1/route/{origin}/{destination}/', 'GET',
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
