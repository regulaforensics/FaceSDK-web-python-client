# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API  # noqa: E501

    The version of the OpenAPI document: 3.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class OutputImageParams(object):
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
        'background_color': 'RGB',
        'crop': 'Crop',
    }

    attribute_map = {
        'background_color': 'backgroundColor',
        'crop': 'crop',
    }

    def __init__(self, background_color=None, crop=None, local_vars_configuration=None):  # noqa: E501
        """OutputImageParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._background_color = None
        self._crop = None
        self.discriminator = None

        if background_color is not None:
            self.background_color = background_color
        if crop is not None:
            self.crop = crop

    @property
    def background_color(self):
        """Gets the background_color of this OutputImageParams.  # noqa: E501


        :return: The background_color of this OutputImageParams.  # noqa: E501
        :rtype: RGB
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this OutputImageParams.


        :param background_color: The background_color of this OutputImageParams.  # noqa: E501
        :type background_color: RGB
        """

        self._background_color = background_color

    @property
    def crop(self):
        """Gets the crop of this OutputImageParams.  # noqa: E501


        :return: The crop of this OutputImageParams.  # noqa: E501
        :rtype: Crop
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this OutputImageParams.


        :param crop: The crop of this OutputImageParams.  # noqa: E501
        :type crop: Crop
        """

        self._crop = crop

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
        if not isinstance(other, OutputImageParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutputImageParams):
            return True

        return self.to_dict() != other.to_dict()
