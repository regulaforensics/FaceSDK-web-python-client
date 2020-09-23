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


class CompareImage(object):
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
        'index': 'float',
        'type': 'ImageSource',
        'data': 'str'
    }

    attribute_map = {
        'index': 'index',
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, index=None, type=None, data=None, local_vars_configuration=None):  # noqa: E501
        """CompareImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._type = None
        self._data = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if type is not None:
            self.type = type
        self.data = data

    @property
    def index(self):
        """Gets the index of this CompareImage.  # noqa: E501


        :return: The index of this CompareImage.  # noqa: E501
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this CompareImage.


        :param index: The index of this CompareImage.  # noqa: E501
        :type index: float
        """

        self._index = index

    @property
    def type(self):
        """Gets the type of this CompareImage.  # noqa: E501


        :return: The type of this CompareImage.  # noqa: E501
        :rtype: ImageSource
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CompareImage.


        :param type: The type of this CompareImage.  # noqa: E501
        :type type: ImageSource
        """

        self._type = type

    @property
    def data(self):
        """Gets the data of this CompareImage.  # noqa: E501

        Base64 encoded image  # noqa: E501

        :return: The data of this CompareImage.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CompareImage.

        Base64 encoded image  # noqa: E501

        :param data: The data of this CompareImage.  # noqa: E501
        :type data: str
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, CompareImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompareImage):
            return True

        return self.to_dict() != other.to_dict()
