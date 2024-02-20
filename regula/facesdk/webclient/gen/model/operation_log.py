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


class OperationLog(object):
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
        'status_code': 'int',
        'type': 'str',
        'msg': 'str',
        'metadata': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
    }

    attribute_map = {
        'status_code': 'statusCode',
        'type': 'type',
        'msg': 'msg',
        'metadata': 'metadata',
    }

    def __init__(self, status_code=None, type=None, msg=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """OperationLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status_code = None
        self._type = None
        self._msg = None
        self._metadata = None
        self.discriminator = None

        if status_code is not None:
            self.status_code = status_code
        if type is not None:
            self.type = type
        if msg is not None:
            self.msg = msg
        if metadata is not None:
            self.metadata = metadata

    @property
    def status_code(self):
        """Gets the status_code of this OperationLog.  # noqa: E501

        Status code.  # noqa: E501

        :return: The status_code of this OperationLog.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this OperationLog.

        Status code.  # noqa: E501

        :param status_code: The status_code of this OperationLog.  # noqa: E501
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def type(self):
        """Gets the type of this OperationLog.  # noqa: E501

        Error type.  # noqa: E501

        :return: The type of this OperationLog.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OperationLog.

        Error type.  # noqa: E501

        :param type: The type of this OperationLog.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def msg(self):
        """Gets the msg of this OperationLog.  # noqa: E501

        Error message.  # noqa: E501

        :return: The msg of this OperationLog.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this OperationLog.

        Error message.  # noqa: E501

        :param msg: The msg of this OperationLog.  # noqa: E501
        :type msg: str
        """

        self._msg = msg

    @property
    def metadata(self):
        """Gets the metadata of this OperationLog.  # noqa: E501

        A free-form object containing group's extended attributes.  # noqa: E501

        :return: The metadata of this OperationLog.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OperationLog.

        A free-form object containing group's extended attributes.  # noqa: E501

        :param metadata: The metadata of this OperationLog.  # noqa: E501
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
        if not isinstance(other, OperationLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationLog):
            return True

        return self.to_dict() != other.to_dict()
