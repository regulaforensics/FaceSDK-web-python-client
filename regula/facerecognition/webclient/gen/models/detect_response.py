# coding: utf-8

"""
    Regula Face Recognition Web API

    Regula Face Recognition Web API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facerecognition.webclient.gen.configuration import Configuration


class DetectResponse(object):
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
        'detections': 'list[Detection]',
        'detector_type': 'int',
        'landmarks_type': 'int'
    }

    attribute_map = {
        'detections': 'detections',
        'detector_type': 'detectorType',
        'landmarks_type': 'landmarksType'
    }

    def __init__(self, detections=None, detector_type=None, landmarks_type=None, local_vars_configuration=None):  # noqa: E501
        """DetectResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._detections = None
        self._detector_type = None
        self._landmarks_type = None
        self.discriminator = None

        if detections is not None:
            self.detections = detections
        if detector_type is not None:
            self.detector_type = detector_type
        if landmarks_type is not None:
            self.landmarks_type = landmarks_type

    @property
    def detections(self):
        """Gets the detections of this DetectResponse.  # noqa: E501


        :return: The detections of this DetectResponse.  # noqa: E501
        :rtype: list[Detection]
        """
        return self._detections

    @detections.setter
    def detections(self, detections):
        """Sets the detections of this DetectResponse.


        :param detections: The detections of this DetectResponse.  # noqa: E501
        :type detections: list[Detection]
        """

        self._detections = detections

    @property
    def detector_type(self):
        """Gets the detector_type of this DetectResponse.  # noqa: E501

        The internal type of detector. Used to calculate the rectangular area of the detected face (roi).  # noqa: E501

        :return: The detector_type of this DetectResponse.  # noqa: E501
        :rtype: int
        """
        return self._detector_type

    @detector_type.setter
    def detector_type(self, detector_type):
        """Sets the detector_type of this DetectResponse.

        The internal type of detector. Used to calculate the rectangular area of the detected face (roi).  # noqa: E501

        :param detector_type: The detector_type of this DetectResponse.  # noqa: E501
        :type detector_type: int
        """

        self._detector_type = detector_type

    @property
    def landmarks_type(self):
        """Gets the landmarks_type of this DetectResponse.  # noqa: E501

        The internal type of detector. Used to calculate the main coordinate of the detected face (landmarks).  # noqa: E501

        :return: The landmarks_type of this DetectResponse.  # noqa: E501
        :rtype: int
        """
        return self._landmarks_type

    @landmarks_type.setter
    def landmarks_type(self, landmarks_type):
        """Sets the landmarks_type of this DetectResponse.

        The internal type of detector. Used to calculate the main coordinate of the detected face (landmarks).  # noqa: E501

        :param landmarks_type: The landmarks_type of this DetectResponse.  # noqa: E501
        :type landmarks_type: int
        """

        self._landmarks_type = landmarks_type

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
        if not isinstance(other, DetectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetectResponse):
            return True

        return self.to_dict() != other.to_dict()
