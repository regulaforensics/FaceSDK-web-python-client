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


class UpdateGroup(object):
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
        'add_items': '[int]',
        'remove_items': '[int]',
    }

    attribute_map = {
        'add_items': 'addItems',
        'remove_items': 'removeItems',
    }

    def __init__(self, add_items=None, remove_items=None, local_vars_configuration=None):  # noqa: E501
        """UpdateGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._add_items = None
        self._remove_items = None
        self.discriminator = None

        if add_items is not None:
            self.add_items = add_items
        if remove_items is not None:
            self.remove_items = remove_items

    @property
    def add_items(self):
        """Gets the add_items of this UpdateGroup.  # noqa: E501

        Add items.  # noqa: E501

        :return: The add_items of this UpdateGroup.  # noqa: E501
        :rtype: [int]
        """
        return self._add_items

    @add_items.setter
    def add_items(self, add_items):
        """Sets the add_items of this UpdateGroup.

        Add items.  # noqa: E501

        :param add_items: The add_items of this UpdateGroup.  # noqa: E501
        :type add_items: [int]
        """

        self._add_items = add_items

    @property
    def remove_items(self):
        """Gets the remove_items of this UpdateGroup.  # noqa: E501

        Remove items.  # noqa: E501

        :return: The remove_items of this UpdateGroup.  # noqa: E501
        :rtype: [int]
        """
        return self._remove_items

    @remove_items.setter
    def remove_items(self, remove_items):
        """Sets the remove_items of this UpdateGroup.

        Remove items.  # noqa: E501

        :param remove_items: The remove_items of this UpdateGroup.  # noqa: E501
        :type remove_items: [int]
        """

        self._remove_items = remove_items

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
        if not isinstance(other, UpdateGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateGroup):
            return True

        return self.to_dict() != other.to_dict()
