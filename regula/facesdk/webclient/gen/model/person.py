# coding: utf-8

"""
    Regula FaceSDK Web API

    [Download OpenAPI specification](https://github.com/regulaforensics/FaceSDK-web-openapi) ### Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class Person(object):
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
        'name': 'str',
        'metadata': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
        'groups': '[str]',
        'id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'groups': 'groups',
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
    }

    def __init__(self, name=None, metadata=None, groups=None, id=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Person - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._metadata = None
        self._groups = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata
        if groups is not None:
            self.groups = groups
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this Person.  # noqa: E501

        Person name.  # noqa: E501

        :return: The name of this Person.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Person.

        Person name.  # noqa: E501

        :param name: The name of this Person.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this Person.  # noqa: E501

        A free-form object containing person's extended attributes.  # noqa: E501

        :return: The metadata of this Person.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Person.

        A free-form object containing person's extended attributes.  # noqa: E501

        :param metadata: The metadata of this Person.  # noqa: E501
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """

        self._metadata = metadata

    @property
    def groups(self):
        """Gets the groups of this Person.  # noqa: E501

        List of groups this person belongs to.  # noqa: E501

        :return: The groups of this Person.  # noqa: E501
        :rtype: [str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Person.

        List of groups this person belongs to.  # noqa: E501

        :param groups: The groups of this Person.  # noqa: E501
        :type groups: [str]
        """

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this Person.  # noqa: E501

        Person ID. The list of persons is sorted by decreasing ID value.  # noqa: E501

        :return: The id of this Person.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Person.

        Person ID. The list of persons is sorted by decreasing ID value.  # noqa: E501

        :param id: The id of this Person.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Person.  # noqa: E501

        Person creation date.  # noqa: E501

        :return: The created_at of this Person.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Person.

        Person creation date.  # noqa: E501

        :param created_at: The created_at of this Person.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Person.  # noqa: E501

        Person update date.  # noqa: E501

        :return: The updated_at of this Person.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Person.

        Person update date.  # noqa: E501

        :param updated_at: The updated_at of this Person.  # noqa: E501
        :type updated_at: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Person):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Person):
            return True

        return self.to_dict() != other.to_dict()
