# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API # Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 5.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class DetectRequest(object):
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
        'tag': 'str',
        'process_param': 'ProcessParam',
        'image': 'str',
        'thumbnails': 'bool',
        'attributes': 'DetectRequestAttributes',
    }

    attribute_map = {
        'tag': 'tag',
        'process_param': 'processParam',
        'image': 'image',
        'thumbnails': 'thumbnails',
        'attributes': 'attributes',
    }

    def __init__(self, tag=None, process_param=None, image=None, thumbnails=False, attributes=None, local_vars_configuration=None):  # noqa: E501
        """DetectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._process_param = None
        self._image = None
        self._thumbnails = None
        self._attributes = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if process_param is not None:
            self.process_param = process_param
        if image is not None:
            self.image = image
        if thumbnails is not None:
            self.thumbnails = thumbnails
        if attributes is not None:
            self.attributes = attributes

    @property
    def tag(self):
        """Gets the tag of this DetectRequest.  # noqa: E501

        Session identificator.  # noqa: E501

        :return: The tag of this DetectRequest.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DetectRequest.

        Session identificator.  # noqa: E501

        :param tag: The tag of this DetectRequest.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def process_param(self):
        """Gets the process_param of this DetectRequest.  # noqa: E501


        :return: The process_param of this DetectRequest.  # noqa: E501
        :rtype: ProcessParam
        """
        return self._process_param

    @process_param.setter
    def process_param(self, process_param):
        """Sets the process_param of this DetectRequest.


        :param process_param: The process_param of this DetectRequest.  # noqa: E501
        :type process_param: ProcessParam
        """

        self._process_param = process_param

    @property
    def image(self):
        """Gets the image of this DetectRequest.  # noqa: E501

        Base64 encoded image.  # noqa: E501

        :return: The image of this DetectRequest.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DetectRequest.

        Base64 encoded image.  # noqa: E501

        :param image: The image of this DetectRequest.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def thumbnails(self):
        """Gets the thumbnails of this DetectRequest.  # noqa: E501

        Whether to return the cropped portrains with the detected faces.  # noqa: E501

        :return: The thumbnails of this DetectRequest.  # noqa: E501
        :rtype: bool
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this DetectRequest.

        Whether to return the cropped portrains with the detected faces.  # noqa: E501

        :param thumbnails: The thumbnails of this DetectRequest.  # noqa: E501
        :type thumbnails: bool
        """

        self._thumbnails = thumbnails

    @property
    def attributes(self):
        """Gets the attributes of this DetectRequest.  # noqa: E501


        :return: The attributes of this DetectRequest.  # noqa: E501
        :rtype: DetectRequestAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DetectRequest.


        :param attributes: The attributes of this DetectRequest.  # noqa: E501
        :type attributes: DetectRequestAttributes
        """

        self._attributes = attributes

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
        if not isinstance(other, DetectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetectRequest):
            return True

        return self.to_dict() != other.to_dict()
