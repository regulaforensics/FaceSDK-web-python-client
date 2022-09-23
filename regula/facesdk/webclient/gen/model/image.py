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


class Image(object):
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
        'id': 'int',
        'content_type': 'str',
        'created_at': 'str',
        'path': 'str',
        'url': 'str',
    }

    attribute_map = {
        'id': 'id',
        'content_type': 'content_type',
        'created_at': 'created_at',
        'path': 'path',
        'url': 'url',
    }

    def __init__(self, id=None, content_type=None, created_at=None, path=None, url=None, local_vars_configuration=None):  # noqa: E501
        """Image - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._content_type = None
        self._created_at = None
        self._path = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content_type is not None:
            self.content_type = content_type
        if created_at is not None:
            self.created_at = created_at
        if path is not None:
            self.path = path
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Image.  # noqa: E501

        Response image ID.  # noqa: E501

        :return: The id of this Image.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.

        Response image ID.  # noqa: E501

        :param id: The id of this Image.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def content_type(self):
        """Gets the content_type of this Image.  # noqa: E501

        The original media type of the returned image.  # noqa: E501

        :return: The content_type of this Image.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Image.

        The original media type of the returned image.  # noqa: E501

        :param content_type: The content_type of this Image.  # noqa: E501
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def created_at(self):
        """Gets the created_at of this Image.  # noqa: E501

        The returned image creation date.  # noqa: E501

        :return: The created_at of this Image.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Image.

        The returned image creation date.  # noqa: E501

        :param created_at: The created_at of this Image.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def path(self):
        """Gets the path of this Image.  # noqa: E501

        The returned image S3 path.  # noqa: E501

        :return: The path of this Image.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Image.

        The returned image S3 path.  # noqa: E501

        :param path: The path of this Image.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def url(self):
        """Gets the url of this Image.  # noqa: E501

        The returned image URL.  # noqa: E501

        :return: The url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Image.

        The returned image URL.  # noqa: E501

        :param url: The url of this Image.  # noqa: E501
        :type url: str
        """

        self._url = url

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
        if not isinstance(other, Image):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Image):
            return True

        return self.to_dict() != other.to_dict()
