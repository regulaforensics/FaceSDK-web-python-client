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


class MatchAndSearchResponseAllOfDetections(object):
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
        'faces': '[FacesResponse]',
        'image_index': 'int',
        'status': 'FaceSDKResultCode',
    }

    attribute_map = {
        'faces': 'faces',
        'image_index': 'imageIndex',
        'status': 'status',
    }

    def __init__(self, faces=None, image_index=None, status=None, local_vars_configuration=None):  # noqa: E501
        """MatchAndSearchResponseAllOfDetections - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._faces = None
        self._image_index = None
        self._status = None
        self.discriminator = None

        if faces is not None:
            self.faces = faces
        if image_index is not None:
            self.image_index = image_index
        if status is not None:
            self.status = status

    @property
    def faces(self):
        """Gets the faces of this MatchAndSearchResponseAllOfDetections.  # noqa: E501


        :return: The faces of this MatchAndSearchResponseAllOfDetections.  # noqa: E501
        :rtype: [FacesResponse]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this MatchAndSearchResponseAllOfDetections.


        :param faces: The faces of this MatchAndSearchResponseAllOfDetections.  # noqa: E501
        :type faces: [FacesResponse]
        """

        self._faces = faces

    @property
    def image_index(self):
        """Gets the image_index of this MatchAndSearchResponseAllOfDetections.  # noqa: E501

        The image index number. Can be given; if not given, the index numbers are set automatically starting from 0. All index numbers must be whole and unique—not repeated.  # noqa: E501

        :return: The image_index of this MatchAndSearchResponseAllOfDetections.  # noqa: E501
        :rtype: int
        """
        return self._image_index

    @image_index.setter
    def image_index(self, image_index):
        """Sets the image_index of this MatchAndSearchResponseAllOfDetections.

        The image index number. Can be given; if not given, the index numbers are set automatically starting from 0. All index numbers must be whole and unique—not repeated.  # noqa: E501

        :param image_index: The image_index of this MatchAndSearchResponseAllOfDetections.  # noqa: E501
        :type image_index: int
        """

        self._image_index = image_index

    @property
    def status(self):
        """Gets the status of this MatchAndSearchResponseAllOfDetections.  # noqa: E501


        :return: The status of this MatchAndSearchResponseAllOfDetections.  # noqa: E501
        :rtype: FaceSDKResultCode
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MatchAndSearchResponseAllOfDetections.


        :param status: The status of this MatchAndSearchResponseAllOfDetections.  # noqa: E501
        :type status: FaceSDKResultCode
        """

        self._status = status

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
        if not isinstance(other, MatchAndSearchResponseAllOfDetections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchAndSearchResponseAllOfDetections):
            return True

        return self.to_dict() != other.to_dict()
