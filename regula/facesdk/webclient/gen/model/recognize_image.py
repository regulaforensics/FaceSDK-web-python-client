# coding: utf-8

"""
    Regula Face SDK Web API

    <a href=\"https://regulaforensics.com/products/face-recognition-sdk/  \" target=\"_blank\">Regula Face SDK</a> is a cross-platform biometric verification solution for a digital identity verification process. The SDK enables convenient and reliable face capture on the client side (mobile, web, and desktop) and further processing on the client or server side.  The Face SDK includes the following features:  * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-detection\" target=\"_blank\">Face Detection</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-comparison-11\" target=\"_blank\">Face Match (1:1)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-identification-1n\" target=\"_blank\">Face Search (1:N)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#liveness-assessment\" target=\"_blank\">Liveness Assessment</a>  Here is the <a href=\"https://github.com/regulaforensics/FaceSDK-web-openapi  \" target=\"_blank\">OpenAPI specification on GitHub</a>.   ### Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class RecognizeImage(object):
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
        'id': 'str',
        'content_type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'path': 'str',
        'url': 'str',
        'metadata': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
        'similarity': 'float',
        'distance': 'float',
    }

    attribute_map = {
        'id': 'id',
        'content_type': 'contentType',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'path': 'path',
        'url': 'url',
        'metadata': 'metadata',
        'similarity': 'similarity',
        'distance': 'distance',
    }

    def __init__(self, id=None, content_type=None, created_at=None, updated_at=None, path=None, url=None, metadata=None, similarity=None, distance=None, local_vars_configuration=None):  # noqa: E501
        """RecognizeImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._content_type = None
        self._created_at = None
        self._updated_at = None
        self._path = None
        self._url = None
        self._metadata = None
        self._similarity = None
        self._distance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content_type is not None:
            self.content_type = content_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if path is not None:
            self.path = path
        if url is not None:
            self.url = url
        if metadata is not None:
            self.metadata = metadata
        if similarity is not None:
            self.similarity = similarity
        if distance is not None:
            self.distance = distance

    @property
    def id(self):
        """Gets the id of this RecognizeImage.  # noqa: E501

        Response image ID. The list is sorted by decreasing ID value.  # noqa: E501

        :return: The id of this RecognizeImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecognizeImage.

        Response image ID. The list is sorted by decreasing ID value.  # noqa: E501

        :param id: The id of this RecognizeImage.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def content_type(self):
        """Gets the content_type of this RecognizeImage.  # noqa: E501

        Original media type of the returned image.  # noqa: E501

        :return: The content_type of this RecognizeImage.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this RecognizeImage.

        Original media type of the returned image.  # noqa: E501

        :param content_type: The content_type of this RecognizeImage.  # noqa: E501
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def created_at(self):
        """Gets the created_at of this RecognizeImage.  # noqa: E501

        Returned image creation date.  # noqa: E501

        :return: The created_at of this RecognizeImage.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecognizeImage.

        Returned image creation date.  # noqa: E501

        :param created_at: The created_at of this RecognizeImage.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this RecognizeImage.  # noqa: E501

        Returned image update date.  # noqa: E501

        :return: The updated_at of this RecognizeImage.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RecognizeImage.

        Returned image update date.  # noqa: E501

        :param updated_at: The updated_at of this RecognizeImage.  # noqa: E501
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def path(self):
        """Gets the path of this RecognizeImage.  # noqa: E501

        Returned image path.  # noqa: E501

        :return: The path of this RecognizeImage.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RecognizeImage.

        Returned image path.  # noqa: E501

        :param path: The path of this RecognizeImage.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def url(self):
        """Gets the url of this RecognizeImage.  # noqa: E501

        Returned image URL.  # noqa: E501

        :return: The url of this RecognizeImage.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RecognizeImage.

        Returned image URL.  # noqa: E501

        :param url: The url of this RecognizeImage.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def metadata(self):
        """Gets the metadata of this RecognizeImage.  # noqa: E501

        A free-form object containing person's extended attributes.  # noqa: E501

        :return: The metadata of this RecognizeImage.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RecognizeImage.

        A free-form object containing person's extended attributes.  # noqa: E501

        :param metadata: The metadata of this RecognizeImage.  # noqa: E501
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """

        self._metadata = metadata

    @property
    def similarity(self):
        """Gets the similarity of this RecognizeImage.  # noqa: E501

        Similarity score.  # noqa: E501

        :return: The similarity of this RecognizeImage.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this RecognizeImage.

        Similarity score.  # noqa: E501

        :param similarity: The similarity of this RecognizeImage.  # noqa: E501
        :type similarity: float
        """

        self._similarity = similarity

    @property
    def distance(self):
        """Gets the distance of this RecognizeImage.  # noqa: E501

        Similarity distance score: the lower the distance, the higher the face's similarity.  # noqa: E501

        :return: The distance of this RecognizeImage.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this RecognizeImage.

        Similarity distance score: the lower the distance, the higher the face's similarity.  # noqa: E501

        :param distance: The distance of this RecognizeImage.  # noqa: E501
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
        if not isinstance(other, RecognizeImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecognizeImage):
            return True

        return self.to_dict() != other.to_dict()
