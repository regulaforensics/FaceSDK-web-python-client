# coding: utf-8

"""
    Regula Face SDK Web API

    <a href=\"https://regulaforensics.com/products/face-recognition-sdk/  \" target=\"_blank\">Regula Face SDK</a> is a cross-platform biometric verification solution for a digital identity verification process and image quality assurance. The SDK enables convenient and reliable face capture on the client side (mobile, web, and desktop) and further processing on the client or server side.   The Face SDK includes the following features:  * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-detection\" target=\"_blank\">Face detection and image quality assessment</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-comparison-11\" target=\"_blank\">Face match (1:1)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-identification-1n\" target=\"_blank\">Face search (1:N)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#liveness-assessment\" target=\"_blank\">Liveness detection</a>  Here is the <a href=\"https://github.com/regulaforensics/FaceSDK-web-openapi  \" target=\"_blank\">OpenAPI specification on GitHub</a>.   ### Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class QualityRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'background_match_color': 'RGB',
        'config': 'QualityConfigList',
    }

    attribute_map = {
        'background_match_color': 'backgroundMatchColor',
        'config': 'config',
    }

    def __init__(self, background_match_color=None, config=None, local_vars_configuration=None):  # noqa: E501
        """QualityRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._background_match_color = None
        self._config = None
        self.discriminator = None

        if background_match_color is not None:
            self.background_match_color = background_match_color
        if config is not None:
            self.config = config

    @property
    def background_match_color(self):
        """Gets the background_match_color of this QualityRequest.  # noqa: E501


        :return: The background_match_color of this QualityRequest.  # noqa: E501
        :rtype: RGB
        """
        return self._background_match_color

    @background_match_color.setter
    def background_match_color(self, background_match_color):
        """Sets the background_match_color of this QualityRequest.


        :param background_match_color: The background_match_color of this QualityRequest.  # noqa: E501
        :type background_match_color: RGB
        """

        self._background_match_color = background_match_color

    @property
    def config(self):
        """Gets the config of this QualityRequest.  # noqa: E501


        :return: The config of this QualityRequest.  # noqa: E501
        :rtype: QualityConfigList
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this QualityRequest.


        :param config: The config of this QualityRequest.  # noqa: E501
        :type config: QualityConfigList
        """

        self._config = config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QualityRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualityRequest):
            return True

        return self.to_dict() != other.to_dict()
