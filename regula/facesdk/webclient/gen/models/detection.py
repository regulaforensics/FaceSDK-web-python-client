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


class Detection(object):
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
        'crop': 'str',
        'attributes': 'dict(str, object)',
        'landmarks': 'list[list[float]]',
        'quality': 'DetectionQuality',
        'roi': 'list[float]',
        'thumbnail': 'str'
    }

    attribute_map = {
        'crop': 'crop',
        'attributes': 'attributes',
        'landmarks': 'landmarks',
        'quality': 'quality',
        'roi': 'roi',
        'thumbnail': 'thumbnail'
    }

    def __init__(self, crop=None, attributes=None, landmarks=None, quality=None, roi=None, thumbnail=None, local_vars_configuration=None):  # noqa: E501
        """Detection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._crop = None
        self._attributes = None
        self._landmarks = None
        self._quality = None
        self._roi = None
        self._thumbnail = None
        self.discriminator = None

        if crop is not None:
            self.crop = crop
        if attributes is not None:
            self.attributes = attributes
        self.landmarks = landmarks
        if quality is not None:
            self.quality = quality
        self.roi = roi
        if thumbnail is not None:
            self.thumbnail = thumbnail

    @property
    def crop(self):
        """Gets the crop of this Detection.  # noqa: E501

        Base64 encoded image  # noqa: E501

        :return: The crop of this Detection.  # noqa: E501
        :rtype: str
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this Detection.

        Base64 encoded image  # noqa: E501

        :param crop: The crop of this Detection.  # noqa: E501
        :type crop: str
        """

        self._crop = crop

    @property
    def attributes(self):
        """Gets the attributes of this Detection.  # noqa: E501


        :return: The attributes of this Detection.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Detection.


        :param attributes: The attributes of this Detection.  # noqa: E501
        :type attributes: dict(str, object)
        """

        self._attributes = attributes

    @property
    def landmarks(self):
        """Gets the landmarks of this Detection.  # noqa: E501

        Main coordinates of the detected face (eyes, nose, lips, ears and etc.).  # noqa: E501

        :return: The landmarks of this Detection.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._landmarks

    @landmarks.setter
    def landmarks(self, landmarks):
        """Sets the landmarks of this Detection.

        Main coordinates of the detected face (eyes, nose, lips, ears and etc.).  # noqa: E501

        :param landmarks: The landmarks of this Detection.  # noqa: E501
        :type landmarks: list[list[float]]
        """
        if self.local_vars_configuration.client_side_validation and landmarks is None:  # noqa: E501
            raise ValueError("Invalid value for `landmarks`, must not be `None`")  # noqa: E501

        self._landmarks = landmarks

    @property
    def quality(self):
        """Gets the quality of this Detection.  # noqa: E501


        :return: The quality of this Detection.  # noqa: E501
        :rtype: DetectionQuality
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this Detection.


        :param quality: The quality of this Detection.  # noqa: E501
        :type quality: DetectionQuality
        """

        self._quality = quality

    @property
    def roi(self):
        """Gets the roi of this Detection.  # noqa: E501

        Rectangular area of the detected face. First element - X-axis coordinate. Second element - Y-axis coordinate. (X, Y) - left top point. Third element - rectangular width. Fourth element - rectangular height.  # noqa: E501

        :return: The roi of this Detection.  # noqa: E501
        :rtype: list[float]
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this Detection.

        Rectangular area of the detected face. First element - X-axis coordinate. Second element - Y-axis coordinate. (X, Y) - left top point. Third element - rectangular width. Fourth element - rectangular height.  # noqa: E501

        :param roi: The roi of this Detection.  # noqa: E501
        :type roi: list[float]
        """
        if self.local_vars_configuration.client_side_validation and roi is None:  # noqa: E501
            raise ValueError("Invalid value for `roi`, must not be `None`")  # noqa: E501

        self._roi = roi

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Detection.  # noqa: E501

        Formatted base64 face detection image.  # noqa: E501

        :return: The thumbnail of this Detection.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Detection.

        Formatted base64 face detection image.  # noqa: E501

        :param thumbnail: The thumbnail of this Detection.  # noqa: E501
        :type thumbnail: str
        """

        self._thumbnail = thumbnail

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
        if not isinstance(other, Detection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Detection):
            return True

        return self.to_dict() != other.to_dict()
