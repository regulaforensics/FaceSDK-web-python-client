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


class SearchResult(object):
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
        'code': 'int',
        'persons': '[SearchPerson]',
        'id': 'str, none_type',
        'created_at': 'str, none_type',
        'updated_at': 'str, none_type',
        'groups': '[str], none_type',
        'name': 'str, none_type',
        'metadata': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
    }

    attribute_map = {
        'code': 'code',
        'persons': 'persons',
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'groups': 'groups',
        'name': 'name',
        'metadata': 'metadata',
    }

    def __init__(self, code=None, persons=None, id=None, created_at=None, updated_at=None, groups=None, name=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """SearchResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._persons = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._groups = None
        self._name = None
        self._metadata = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if persons is not None:
            self.persons = persons
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.groups = groups
        self.name = name
        if metadata is not None:
            self.metadata = metadata

    @property
    def code(self):
        """Gets the code of this SearchResult.  # noqa: E501

        Result code. It is returned only with response 200.  # noqa: E501

        :return: The code of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SearchResult.

        Result code. It is returned only with response 200.  # noqa: E501

        :param code: The code of this SearchResult.  # noqa: E501
        :type code: int
        """

        self._code = code

    @property
    def persons(self):
        """Gets the persons of this SearchResult.  # noqa: E501

        Array of Person images. It is returned only with response 200.  # noqa: E501

        :return: The persons of this SearchResult.  # noqa: E501
        :rtype: [SearchPerson]
        """
        return self._persons

    @persons.setter
    def persons(self, persons):
        """Sets the persons of this SearchResult.

        Array of Person images. It is returned only with response 200.  # noqa: E501

        :param persons: The persons of this SearchResult.  # noqa: E501
        :type persons: [SearchPerson]
        """

        self._persons = persons

    @property
    def id(self):
        """Gets the id of this SearchResult.  # noqa: E501

        Person ID. The list of persons is sorted by decreasing ID value.  # noqa: E501

        :return: The id of this SearchResult.  # noqa: E501
        :rtype: str, none_type
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchResult.

        Person ID. The list of persons is sorted by decreasing ID value.  # noqa: E501

        :param id: The id of this SearchResult.  # noqa: E501
        :type id: str, none_type
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this SearchResult.  # noqa: E501

        Person creation date.  # noqa: E501

        :return: The created_at of this SearchResult.  # noqa: E501
        :rtype: str, none_type
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SearchResult.

        Person creation date.  # noqa: E501

        :param created_at: The created_at of this SearchResult.  # noqa: E501
        :type created_at: str, none_type
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SearchResult.  # noqa: E501

        Person update date.  # noqa: E501

        :return: The updated_at of this SearchResult.  # noqa: E501
        :rtype: str, none_type
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SearchResult.

        Person update date.  # noqa: E501

        :param updated_at: The updated_at of this SearchResult.  # noqa: E501
        :type updated_at: str, none_type
        """

        self._updated_at = updated_at

    @property
    def groups(self):
        """Gets the groups of this SearchResult.  # noqa: E501

        List of groups this person belongs to.  # noqa: E501

        :return: The groups of this SearchResult.  # noqa: E501
        :rtype: [str], none_type
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this SearchResult.

        List of groups this person belongs to.  # noqa: E501

        :param groups: The groups of this SearchResult.  # noqa: E501
        :type groups: [str], none_type
        """

        self._groups = groups

    @property
    def name(self):
        """Gets the name of this SearchResult.  # noqa: E501

        Person's name.  # noqa: E501

        :return: The name of this SearchResult.  # noqa: E501
        :rtype: str, none_type
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchResult.

        Person's name.  # noqa: E501

        :param name: The name of this SearchResult.  # noqa: E501
        :type name: str, none_type
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this SearchResult.  # noqa: E501

        A free-form object containing person's extended attributes. Available when a person is being created  # noqa: E501

        :return: The metadata of this SearchResult.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SearchResult.

        A free-form object containing person's extended attributes. Available when a person is being created  # noqa: E501

        :param metadata: The metadata of this SearchResult.  # noqa: E501
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """

        self._metadata = metadata

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
        if not isinstance(other, SearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchResult):
            return True

        return self.to_dict() != other.to_dict()
