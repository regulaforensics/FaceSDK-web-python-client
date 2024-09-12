# coding: utf-8

"""
    Regula Face SDK Web API

    <a href=\"https://regulaforensics.com/products/face-recognition-sdk/  \" target=\"_blank\">Regula Face SDK</a> is a cross-platform biometric verification solution for a digital identity verification process and image quality assurance. The SDK enables convenient and reliable face capture on the client side (mobile, web, and desktop) and further processing on the client or server side.   The Face SDK includes the following features:  * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-detection\" target=\"_blank\">Face detection and image quality assessment</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-comparison-11\" target=\"_blank\">Face match (1:1)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-identification-1n\" target=\"_blank\">Face search (1:N)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#liveness-assessment\" target=\"_blank\">Liveness detection</a>  Here is the <a href=\"https://github.com/regulaforensics/FaceSDK-web-openapi  \" target=\"_blank\">OpenAPI specification on GitHub</a>.   ### Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.2.0
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


class Liveness20Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_liveness_transaction_info(self, transaction_id, **kwargs):  # noqa: E501
        """liveness check  # noqa: E501

        To verify the presence of a real person in front of a camera, use the GET `/api/v2/liveness` endpoint. When starting, you can specify `tag` which all attempts to read liveness will be bound to. If left unspecified, the application automatically generates one. The calling application returns `tag` and `transactionId`. One session may include many transactions, and from a transaction ID it is clear which session it belongs to.  When specifying `tag`, note that only Latin uppercase and lowercase letters, digits, and symbols `-` and `_` are allowed. The maximum supported number of characters is 127.  The metadata (device model, screen data, frame size, app ID and version, OS version, platform, SDK version, etc.), a person's selfie and video of the liveness detection session are stored on the backend at: `faceapi-session/year={year}/month={month}/day={day}/hour={hour}/minute={minute}/{tag}/transactionId`  By default, liveness checks operate with eventual consistency. This means that when you submit a request and receive a response, the associated data (like the selfie and session video) may be saved after the response is sent. If this doesn't meet your requirements, you can switch to strong consistency; refer to the [Architecture page](https://docs.regulaforensics.com/develop/face-sdk/overview/architecture/#consistency-models) for details.  To access the liveness transaction data, use GET `/api/v2/liveness?transactionId={transactionId}`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_liveness_transaction_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param transaction_id: ID of the current liveness transaction. (required)
        :type transaction_id: str
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
        :rtype: TransactionInfo
        """
        kwargs['_return_http_data_only'] = True
        return self.get_liveness_transaction_info_with_http_info(transaction_id, **kwargs)  # noqa: E501

    def get_liveness_transaction_info_with_http_info(self, transaction_id, **kwargs):  # noqa: E501
        """liveness check  # noqa: E501

        To verify the presence of a real person in front of a camera, use the GET `/api/v2/liveness` endpoint. When starting, you can specify `tag` which all attempts to read liveness will be bound to. If left unspecified, the application automatically generates one. The calling application returns `tag` and `transactionId`. One session may include many transactions, and from a transaction ID it is clear which session it belongs to.  When specifying `tag`, note that only Latin uppercase and lowercase letters, digits, and symbols `-` and `_` are allowed. The maximum supported number of characters is 127.  The metadata (device model, screen data, frame size, app ID and version, OS version, platform, SDK version, etc.), a person's selfie and video of the liveness detection session are stored on the backend at: `faceapi-session/year={year}/month={month}/day={day}/hour={hour}/minute={minute}/{tag}/transactionId`  By default, liveness checks operate with eventual consistency. This means that when you submit a request and receive a response, the associated data (like the selfie and session video) may be saved after the response is sent. If this doesn't meet your requirements, you can switch to strong consistency; refer to the [Architecture page](https://docs.regulaforensics.com/develop/face-sdk/overview/architecture/#consistency-models) for details.  To access the liveness transaction data, use GET `/api/v2/liveness?transactionId={transactionId}`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_liveness_transaction_info_with_http_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param transaction_id: ID of the current liveness transaction. (required)
        :type transaction_id: str
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
        :rtype: tuple(TransactionInfo, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'transaction_id',
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
                    " to method get_liveness_transaction_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `get_liveness_transaction_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'transaction_id' in local_var_params and local_var_params['transaction_id'] is not None:  # noqa: E501
            query_params.append(('transactionId', local_var_params['transaction_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/liveness', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
