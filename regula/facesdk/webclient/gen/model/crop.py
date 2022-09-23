# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API # Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 4.1.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class Crop(object):
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
        'type': 'FaceImageQualityAlignType',
        'pad_color': 'RGB',
        'size': '[int]',
        'return_original_rect': 'bool',
    }

    attribute_map = {
        'type': 'type',
        'pad_color': 'padColor',
        'size': 'size',
        'return_original_rect': 'returnOriginalRect',
    }

    def __init__(self, type=None, pad_color=None, size=None, return_original_rect=None, local_vars_configuration=None):  # noqa: E501
        """Crop - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._pad_color = None
        self._size = None
        self._return_original_rect = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if pad_color is not None:
            self.pad_color = pad_color
        if size is not None:
            self.size = size
        if return_original_rect is not None:
            self.return_original_rect = return_original_rect

    @property
    def type(self):
        """Gets the type of this Crop.  # noqa: E501


        :return: The type of this Crop.  # noqa: E501
        :rtype: FaceImageQualityAlignType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Crop.


        :param type: The type of this Crop.  # noqa: E501
        :type type: FaceImageQualityAlignType
        """

        self._type = type

    @property
    def pad_color(self):
        """Gets the pad_color of this Crop.  # noqa: E501


        :return: The pad_color of this Crop.  # noqa: E501
        :rtype: RGB
        """
        return self._pad_color

    @pad_color.setter
    def pad_color(self, pad_color):
        """Sets the pad_color of this Crop.


        :param pad_color: The pad_color of this Crop.  # noqa: E501
        :type pad_color: RGB
        """

        self._pad_color = pad_color

    @property
    def size(self):
        """Gets the size of this Crop.  # noqa: E501

        The resize value in case type matches this value. It it doesn't, no resize is done.  # noqa: E501

        :return: The size of this Crop.  # noqa: E501
        :rtype: [int]
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Crop.

        The resize value in case type matches this value. It it doesn't, no resize is done.  # noqa: E501

        :param size: The size of this Crop.  # noqa: E501
        :type size: [int]
        """
        if (self.local_vars_configuration.client_side_validation and
                size is not None and len(size) > 2):
            raise ValueError("Invalid value for `size`, number of items must be less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and len(size) < 2):
            raise ValueError("Invalid value for `size`, number of items must be greater than or equal to `2`")  # noqa: E501

        self._size = size

    @property
    def return_original_rect(self):
        """Gets the return_original_rect of this Crop.  # noqa: E501

        Whether to return the coordinates of the rectangle with the face in the original image prepared for the face crop.  # noqa: E501

        :return: The return_original_rect of this Crop.  # noqa: E501
        :rtype: bool
        """
        return self._return_original_rect

    @return_original_rect.setter
    def return_original_rect(self, return_original_rect):
        """Sets the return_original_rect of this Crop.

        Whether to return the coordinates of the rectangle with the face in the original image prepared for the face crop.  # noqa: E501

        :param return_original_rect: The return_original_rect of this Crop.  # noqa: E501
        :type return_original_rect: bool
        """

        self._return_original_rect = return_original_rect

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
        if not isinstance(other, Crop):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Crop):
            return True

        return self.to_dict() != other.to_dict()
