# coding: utf-8

"""
    Regula Face SDK Web API

    <a href=\"https://regulaforensics.com/products/face-recognition-sdk/  \" target=\"_blank\">Regula Face SDK</a> is a cross-platform biometric verification solution for a digital identity verification process. The SDK enables convenient and reliable face capture on the client side (mobile, web, and desktop) and further processing on the client or server side.  The Face SDK includes the following features:  * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-detection\" target=\"_blank\">Face Detection</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-comparison-11\" target=\"_blank\">Face Match (1:1)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-identification-1n\" target=\"_blank\">Face Search (1:N)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#liveness-assessment\" target=\"_blank\">Liveness Assessment</a>  Here is the <a href=\"https://github.com/regulaforensics/FaceSDK-web-openapi  \" target=\"_blank\">OpenAPI specification on GitHub</a>.   ### Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from regula.facesdk.webclient.gen.api_client import ApiClient
from regula.facesdk.webclient.gen.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FaceComparisonApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def match(self, match_request, **kwargs):  # noqa: E501
        """compare faces (1:1)  # noqa: E501

        To perform a comparison of faces in the same image or in two different images, use POST `/api/match`. It's possible to compare faces in the same image or in two different images, this is defined by the `images.type` parameter. <br><br> The face detection result is displayed in the `detections` field. Each face is identified by two parameters: `faceIndex` (the index number of the face) and `imageIndex` (the index number of the image on which the face is detected). So, if there are two images each of which has two faces in them, the parameters will be the following: - First face in the first image: `faceIndex: 0`, `imageIndex: 0` - Second face in the first image: `faceIndex: 1`, `imageIndex: 0` - First face of the second image: `faceIndex: 0`, `imageIndex: 1` - Second face in the second image: `faceIndex: 1`, `imageIndex: 1`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.match(match_request, async_req=True)
        >>> result = thread.get()

        :param match_request: (required)
        :type match_request: MatchRequest
        :param x_request_id: Request header label.
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MatchResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.match_with_http_info(match_request, **kwargs)  # noqa: E501

    def match_with_http_info(self, match_request, **kwargs):  # noqa: E501
        """compare faces (1:1)  # noqa: E501

        To perform a comparison of faces in the same image or in two different images, use POST `/api/match`. It's possible to compare faces in the same image or in two different images, this is defined by the `images.type` parameter. <br><br> The face detection result is displayed in the `detections` field. Each face is identified by two parameters: `faceIndex` (the index number of the face) and `imageIndex` (the index number of the image on which the face is detected). So, if there are two images each of which has two faces in them, the parameters will be the following: - First face in the first image: `faceIndex: 0`, `imageIndex: 0` - Second face in the first image: `faceIndex: 1`, `imageIndex: 0` - First face of the second image: `faceIndex: 0`, `imageIndex: 1` - Second face in the second image: `faceIndex: 1`, `imageIndex: 1`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.match_with_http_info(match_request, async_req=True)
        >>> result = thread.get()

        :param match_request: (required)
        :type match_request: MatchRequest
        :param x_request_id: Request header label.
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MatchResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'match_request'
            'x_request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'match_request' is set
        if self.api_client.client_side_validation and ('match_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['match_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `match_request` when calling `match`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-RequestID'] = local_var_params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'match_request' in local_var_params:
            body_params = local_var_params['match_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/match', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MatchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def match_and_search(self, match_and_search_request, **kwargs):  # noqa: E501
        """match and search (1:1 + 1:N)  # noqa: E501

        To compare several images from a document and look up a person in the database in one request, use POST `/api/match_and_search`. In this case, the calculation of the descriptor will be performed only once, as opposed to using two requests for the same operation. If only one person is identified, matching is not performed and only search is carried out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.match_and_search(match_and_search_request, async_req=True)
        >>> result = thread.get()

        :param match_and_search_request: (required)
        :type match_and_search_request: MatchAndSearchRequest
        :param x_request_id: Request header label.
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MatchAndSearchResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.match_and_search_with_http_info(match_and_search_request, **kwargs)  # noqa: E501

    def match_and_search_with_http_info(self, match_and_search_request, **kwargs):  # noqa: E501
        """match and search (1:1 + 1:N)  # noqa: E501

        To compare several images from a document and look up a person in the database in one request, use POST `/api/match_and_search`. In this case, the calculation of the descriptor will be performed only once, as opposed to using two requests for the same operation. If only one person is identified, matching is not performed and only search is carried out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.match_and_search_with_http_info(match_and_search_request, async_req=True)
        >>> result = thread.get()

        :param match_and_search_request: (required)
        :type match_and_search_request: MatchAndSearchRequest
        :param x_request_id: Request header label.
        :type x_request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MatchAndSearchResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'match_and_search_request'
            'x_request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match_and_search" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'match_and_search_request' is set
        if self.api_client.client_side_validation and ('match_and_search_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['match_and_search_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `match_and_search_request` when calling `match_and_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-RequestID'] = local_var_params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'match_and_search_request' in local_var_params:
            body_params = local_var_params['match_and_search_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/match_and_search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MatchAndSearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
