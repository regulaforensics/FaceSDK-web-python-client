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


class DetectionFace(object):
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
        'face_index': 'int',
        'landmarks': 'list[list[float]]',
        'roi': 'list[float]',
        'thumbnail': 'str'
    }

    attribute_map = {
        'face_index': 'faceIndex',
        'landmarks': 'landmarks',
        'roi': 'roi',
        'thumbnail': 'thumbnail'
    }

    def __init__(self, face_index=None, landmarks=None, roi=None, thumbnail=None, local_vars_configuration=None):  # noqa: E501
        """DetectionFace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._face_index = None
        self._landmarks = None
        self._roi = None
        self._thumbnail = None
        self.discriminator = None

        if face_index is not None:
            self.face_index = face_index
        if landmarks is not None:
            self.landmarks = landmarks
        if roi is not None:
            self.roi = roi
        if thumbnail is not None:
            self.thumbnail = thumbnail

    @property
    def face_index(self):
        """Gets the face_index of this DetectionFace.  # noqa: E501

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :return: The face_index of this DetectionFace.  # noqa: E501
        :rtype: int
        """
        return self._face_index

    @face_index.setter
    def face_index(self, face_index):
        """Sets the face_index of this DetectionFace.

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :param face_index: The face_index of this DetectionFace.  # noqa: E501
        :type face_index: int
        """

        self._face_index = face_index

    @property
    def landmarks(self):
        """Gets the landmarks of this DetectionFace.  # noqa: E501

        Main coordinates of the detected face (eyes, nose, lips, ears and etc.).  # noqa: E501

        :return: The landmarks of this DetectionFace.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._landmarks

    @landmarks.setter
    def landmarks(self, landmarks):
        """Sets the landmarks of this DetectionFace.

        Main coordinates of the detected face (eyes, nose, lips, ears and etc.).  # noqa: E501

        :param landmarks: The landmarks of this DetectionFace.  # noqa: E501
        :type landmarks: list[list[float]]
        """

        self._landmarks = landmarks

    @property
    def roi(self):
        """Gets the roi of this DetectionFace.  # noqa: E501

        Rectangular area of the detected face. First element - X-axis coordinate. Second element - Y-axis coordinate. (X, Y) - left top point. Third element - rectangular width. Fourth element - rectangular height.  # noqa: E501

        :return: The roi of this DetectionFace.  # noqa: E501
        :rtype: list[float]
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this DetectionFace.

        Rectangular area of the detected face. First element - X-axis coordinate. Second element - Y-axis coordinate. (X, Y) - left top point. Third element - rectangular width. Fourth element - rectangular height.  # noqa: E501

        :param roi: The roi of this DetectionFace.  # noqa: E501
        :type roi: list[float]
        """

        self._roi = roi

    @property
    def thumbnail(self):
        """Gets the thumbnail of this DetectionFace.  # noqa: E501

        Formatted base64 face detection image.  # noqa: E501

        :return: The thumbnail of this DetectionFace.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this DetectionFace.

        Formatted base64 face detection image.  # noqa: E501

        :param thumbnail: The thumbnail of this DetectionFace.  # noqa: E501
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
        if not isinstance(other, DetectionFace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetectionFace):
            return True

        return self.to_dict() != other.to_dict()
