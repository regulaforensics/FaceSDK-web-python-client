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


class Group(object):
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
        'tag': 'str',
        'name': 'str',
        'metadata': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
        'id': 'str',
        'created_at': 'str',
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'metadata': 'metadata',
        'id': 'id',
        'created_at': 'createdAt',
    }

    def __init__(self, tag=None, name=None, metadata=None, id=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._name = None
        self._metadata = None
        self._id = None
        self._created_at = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at

    @property
    def tag(self):
        """Gets the tag of this Group.  # noqa: E501

        Session identificator.  # noqa: E501

        :return: The tag of this Group.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Group.

        Session identificator.  # noqa: E501

        :param tag: The tag of this Group.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        Group to create name.  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        Group to create name.  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this Group.  # noqa: E501

        A free-form object containing group's extended attributes.  # noqa: E501

        :return: The metadata of this Group.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Group.

        A free-form object containing group's extended attributes.  # noqa: E501

        :param metadata: The metadata of this Group.  # noqa: E501
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """

        self._metadata = metadata

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        Group ID.  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        Group ID.  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Group.  # noqa: E501

        Group creation date.  # noqa: E501

        :return: The created_at of this Group.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Group.

        Group creation date.  # noqa: E501

        :param created_at: The created_at of this Group.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

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
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()
