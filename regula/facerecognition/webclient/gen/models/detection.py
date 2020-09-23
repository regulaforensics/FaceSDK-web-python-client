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
        'landmarks': 'list[list[float]]',
        'roi': 'list[float]'
    }

    attribute_map = {
        'landmarks': 'landmarks',
        'roi': 'roi'
    }

    def __init__(self, landmarks=None, roi=None, local_vars_configuration=None):  # noqa: E501
        """Detection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._landmarks = None
        self._roi = None
        self.discriminator = None

        if landmarks is not None:
            self.landmarks = landmarks
        if roi is not None:
            self.roi = roi

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

        self._landmarks = landmarks

    @property
    def roi(self):
        """Gets the roi of this Detection.  # noqa: E501

        Rectangular area of the detected face. First element - X-axis coordinate. Second element - Y-axis coordinate. Third element - rectangular weight. Fourth element - rectangular.  # noqa: E501

        :return: The roi of this Detection.  # noqa: E501
        :rtype: list[float]
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this Detection.

        Rectangular area of the detected face. First element - X-axis coordinate. Second element - Y-axis coordinate. Third element - rectangular weight. Fourth element - rectangular.  # noqa: E501

        :param roi: The roi of this Detection.  # noqa: E501
        :type roi: list[float]
        """

        self._roi = roi

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
