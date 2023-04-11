# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API # Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class MatchAndSearchRequestAllOfImages(object):
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
        'content': 'str',
        'type': 'ImageSource',
    }

    attribute_map = {
        'content': 'content',
        'type': 'type',
    }

    def __init__(self, content=None, type=None, local_vars_configuration=None):  # noqa: E501
        """MatchAndSearchRequestAllOfImages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._type = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if type is not None:
            self.type = type

    @property
    def content(self):
        """Gets the content of this MatchAndSearchRequestAllOfImages.  # noqa: E501

        Base64 encoded image.  # noqa: E501

        :return: The content of this MatchAndSearchRequestAllOfImages.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MatchAndSearchRequestAllOfImages.

        Base64 encoded image.  # noqa: E501

        :param content: The content of this MatchAndSearchRequestAllOfImages.  # noqa: E501
        :type content: str
        """

        self._content = content

    @property
    def type(self):
        """Gets the type of this MatchAndSearchRequestAllOfImages.  # noqa: E501


        :return: The type of this MatchAndSearchRequestAllOfImages.  # noqa: E501
        :rtype: ImageSource
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MatchAndSearchRequestAllOfImages.


        :param type: The type of this MatchAndSearchRequestAllOfImages.  # noqa: E501
        :type type: ImageSource
        """

        self._type = type

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
        if not isinstance(other, MatchAndSearchRequestAllOfImages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchAndSearchRequestAllOfImages):
            return True

        return self.to_dict() != other.to_dict()
