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


class FacesResponse(object):
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
        'face_index': 'float',
        'landmarks': '[[float]]',
        'roi': 'FaceRectangular',
        'thumbnail': 'str',
        'persons': '[PersonWithImages]',
        'rotation_angle': 'float',
    }

    attribute_map = {
        'face_index': 'faceIndex',
        'landmarks': 'landmarks',
        'roi': 'roi',
        'thumbnail': 'thumbnail',
        'persons': 'persons',
        'rotation_angle': 'rotationAngle',
    }

    def __init__(self, face_index=None, landmarks=None, roi=None, thumbnail=None, persons=None, rotation_angle=None, local_vars_configuration=None):  # noqa: E501
        """FacesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._face_index = None
        self._landmarks = None
        self._roi = None
        self._thumbnail = None
        self._persons = None
        self._rotation_angle = None
        self.discriminator = None

        if face_index is not None:
            self.face_index = face_index
        if landmarks is not None:
            self.landmarks = landmarks
        if roi is not None:
            self.roi = roi
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if persons is not None:
            self.persons = persons
        if rotation_angle is not None:
            self.rotation_angle = rotation_angle

    @property
    def face_index(self):
        """Gets the face_index of this FacesResponse.  # noqa: E501

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :return: The face_index of this FacesResponse.  # noqa: E501
        :rtype: float
        """
        return self._face_index

    @face_index.setter
    def face_index(self, face_index):
        """Sets the face_index of this FacesResponse.

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :param face_index: The face_index of this FacesResponse.  # noqa: E501
        :type face_index: float
        """

        self._face_index = face_index

    @property
    def landmarks(self):
        """Gets the landmarks of this FacesResponse.  # noqa: E501

        Absolute coordinates (x,y) of five points of each detected face: left eye, right eye, nose, left point of lips, right point of lips.  # noqa: E501

        :return: The landmarks of this FacesResponse.  # noqa: E501
        :rtype: [[float]]
        """
        return self._landmarks

    @landmarks.setter
    def landmarks(self, landmarks):
        """Sets the landmarks of this FacesResponse.

        Absolute coordinates (x,y) of five points of each detected face: left eye, right eye, nose, left point of lips, right point of lips.  # noqa: E501

        :param landmarks: The landmarks of this FacesResponse.  # noqa: E501
        :type landmarks: [[float]]
        """

        self._landmarks = landmarks

    @property
    def roi(self):
        """Gets the roi of this FacesResponse.  # noqa: E501


        :return: The roi of this FacesResponse.  # noqa: E501
        :rtype: FaceRectangular
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this FacesResponse.


        :param roi: The roi of this FacesResponse.  # noqa: E501
        :type roi: FaceRectangular
        """

        self._roi = roi

    @property
    def thumbnail(self):
        """Gets the thumbnail of this FacesResponse.  # noqa: E501

        Base64 of the cropped portrait.  # noqa: E501

        :return: The thumbnail of this FacesResponse.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this FacesResponse.

        Base64 of the cropped portrait.  # noqa: E501

        :param thumbnail: The thumbnail of this FacesResponse.  # noqa: E501
        :type thumbnail: str
        """

        self._thumbnail = thumbnail

    @property
    def persons(self):
        """Gets the persons of this FacesResponse.  # noqa: E501


        :return: The persons of this FacesResponse.  # noqa: E501
        :rtype: [PersonWithImages]
        """
        return self._persons

    @persons.setter
    def persons(self, persons):
        """Sets the persons of this FacesResponse.


        :param persons: The persons of this FacesResponse.  # noqa: E501
        :type persons: [PersonWithImages]
        """

        self._persons = persons

    @property
    def rotation_angle(self):
        """Gets the rotation_angle of this FacesResponse.  # noqa: E501


        :return: The rotation_angle of this FacesResponse.  # noqa: E501
        :rtype: float
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """Sets the rotation_angle of this FacesResponse.


        :param rotation_angle: The rotation_angle of this FacesResponse.  # noqa: E501
        :type rotation_angle: float
        """

        self._rotation_angle = rotation_angle

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
        if not isinstance(other, FacesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FacesResponse):
            return True

        return self.to_dict() != other.to_dict()
