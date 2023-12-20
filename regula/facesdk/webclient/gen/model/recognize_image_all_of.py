# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API # Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class RecognizeImageAllOf(object):
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
        'similarity': 'float',
        'distance': 'float',
    }

    attribute_map = {
        'similarity': 'similarity',
        'distance': 'distance',
    }

    def __init__(self, similarity=None, distance=None, local_vars_configuration=None):  # noqa: E501
        """RecognizeImageAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._similarity = None
        self._distance = None
        self.discriminator = None

        if similarity is not None:
            self.similarity = similarity
        if distance is not None:
            self.distance = distance

    @property
    def similarity(self):
        """Gets the similarity of this RecognizeImageAllOf.  # noqa: E501

        Similarity score.  # noqa: E501

        :return: The similarity of this RecognizeImageAllOf.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this RecognizeImageAllOf.

        Similarity score.  # noqa: E501

        :param similarity: The similarity of this RecognizeImageAllOf.  # noqa: E501
        :type similarity: float
        """

        self._similarity = similarity

    @property
    def distance(self):
        """Gets the distance of this RecognizeImageAllOf.  # noqa: E501

        Similarity distance score: the lower the distance, the higher the face's similarity.  # noqa: E501

        :return: The distance of this RecognizeImageAllOf.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this RecognizeImageAllOf.

        Similarity distance score: the lower the distance, the higher the face's similarity.  # noqa: E501

        :param distance: The distance of this RecognizeImageAllOf.  # noqa: E501
        :type distance: float
        """

        self._distance = distance

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
        if not isinstance(other, RecognizeImageAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecognizeImageAllOf):
            return True

        return self.to_dict() != other.to_dict()
