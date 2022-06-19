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


class CalendarApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_calendar(self, character_id, **kwargs):  # noqa: E501
        """List calendar event summaries  # noqa: E501

        Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event  ---  This route is cached for up to 5 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_calendar(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_event: The event ID to retrieve events from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdCalendar200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_calendar_with_http_info(character_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_calendar_with_http_info(character_id, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_calendar_with_http_info(self, character_id, **kwargs):  # noqa: E501
        """List calendar event summaries  # noqa: E501

        Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event  ---  This route is cached for up to 5 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_calendar_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_event: The event ID to retrieve events from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdCalendar200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'from_event', 'if_none_match', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_calendar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_calendar`")  # noqa: E501

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_calendar`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'from_event' in params:
            query_params.append(('from_event', params['from_event']))  # noqa: E501
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
            '/v1/characters/{character_id}/calendar/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetCharactersCharacterIdCalendar200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_characters_character_id_calendar_event_id(self, character_id, event_id, **kwargs):  # noqa: E501
        """Get an event  # noqa: E501

        Get all the information for a specific event  ---  This route is cached for up to 5 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_calendar_event_id(character_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int event_id: The id of the event requested (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: GetCharactersCharacterIdCalendarEventIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_calendar_event_id_with_http_info(character_id, event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_calendar_event_id_with_http_info(character_id, event_id, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_calendar_event_id_with_http_info(self, character_id, event_id, **kwargs):  # noqa: E501
        """Get an event  # noqa: E501

        Get all the information for a specific event  ---  This route is cached for up to 5 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_calendar_event_id_with_http_info(character_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int event_id: The id of the event requested (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: GetCharactersCharacterIdCalendarEventIdOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'event_id', 'datasource', 'if_none_match', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_calendar_event_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_calendar_event_id`")  # noqa: E501
        # verify the required parameter 'event_id' is set
        if self.api_client.client_side_validation and ('event_id' not in params or
                                                       params['event_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `event_id` when calling `get_characters_character_id_calendar_event_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_calendar_event_id`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501
        if 'event_id' in params:
            path_params['event_id'] = params['event_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
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
            '/v3/characters/{character_id}/calendar/{event_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCharactersCharacterIdCalendarEventIdOk',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_characters_character_id_calendar_event_id_attendees(self, character_id, event_id, **kwargs):  # noqa: E501
        """Get attendees  # noqa: E501

        Get all invited attendees for a given event  ---  This route is cached for up to 600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_calendar_event_id_attendees(character_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int event_id: The id of the event requested (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdCalendarEventIdAttendees200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_calendar_event_id_attendees_with_http_info(character_id, event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_characters_character_id_calendar_event_id_attendees_with_http_info(character_id, event_id, **kwargs)  # noqa: E501
            return data

    def get_characters_character_id_calendar_event_id_attendees_with_http_info(self, character_id, event_id, **kwargs):  # noqa: E501
        """Get attendees  # noqa: E501

        Get all invited attendees for a given event  ---  This route is cached for up to 600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_calendar_event_id_attendees_with_http_info(character_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int event_id: The id of the event requested (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[GetCharactersCharacterIdCalendarEventIdAttendees200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'event_id', 'datasource', 'if_none_match', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_calendar_event_id_attendees" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_calendar_event_id_attendees`")  # noqa: E501
        # verify the required parameter 'event_id' is set
        if self.api_client.client_side_validation and ('event_id' not in params or
                                                       params['event_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `event_id` when calling `get_characters_character_id_calendar_event_id_attendees`")  # noqa: E501

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_calendar_event_id_attendees`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501
        if 'event_id' in params:
            path_params['event_id'] = params['event_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
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
            '/v1/characters/{character_id}/calendar/{event_id}/attendees/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetCharactersCharacterIdCalendarEventIdAttendees200Ok]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_characters_character_id_calendar_event_id(self, character_id, event_id, response, **kwargs):  # noqa: E501
        """Respond to an event  # noqa: E501

        Set your response status to an event  ---  This route is cached for up to 5 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_characters_character_id_calendar_event_id(character_id, event_id, response, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int event_id: The ID of the event requested (required)
        :param PutCharactersCharacterIdCalendarEventIdResponse response: The response value to set, overriding current value (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_characters_character_id_calendar_event_id_with_http_info(character_id, event_id, response, **kwargs)  # noqa: E501
        else:
            (data) = self.put_characters_character_id_calendar_event_id_with_http_info(character_id, event_id, response, **kwargs)  # noqa: E501
            return data

    def put_characters_character_id_calendar_event_id_with_http_info(self, character_id, event_id, response, **kwargs):  # noqa: E501
        """Respond to an event  # noqa: E501

        Set your response status to an event  ---  This route is cached for up to 5 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_characters_character_id_calendar_event_id_with_http_info(character_id, event_id, response, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int event_id: The ID of the event requested (required)
        :param PutCharactersCharacterIdCalendarEventIdResponse response: The response value to set, overriding current value (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'event_id', 'response', 'datasource', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_characters_character_id_calendar_event_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `character_id` when calling `put_characters_character_id_calendar_event_id`")  # noqa: E501
        # verify the required parameter 'event_id' is set
        if self.api_client.client_side_validation and ('event_id' not in params or
                                                       params['event_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `event_id` when calling `put_characters_character_id_calendar_event_id`")  # noqa: E501
        # verify the required parameter 'response' is set
        if self.api_client.client_side_validation and ('response' not in params or
                                                       params['response'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `response` when calling `put_characters_character_id_calendar_event_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `character_id` when calling `put_characters_character_id_calendar_event_id`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']  # noqa: E501
        if 'event_id' in params:
            path_params['event_id'] = params['event_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'response' in params:
            body_params = params['response']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['evesso']  # noqa: E501

        return self.api_client.call_api(
            '/v3/characters/{character_id}/calendar/{event_id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
