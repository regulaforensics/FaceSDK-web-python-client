# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API  # noqa: E501

    The version of the OpenAPI document: 3.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class QualityConfig(object):
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
        'name': 'FaceQualityConfigName',
        'range': '[float]',
    }

    attribute_map = {
        'name': 'name',
        'range': 'range',
    }

    def __init__(self, name=None, range=None, local_vars_configuration=None):  # noqa: E501
        """QualityConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._range = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if range is not None:
            self.range = range

    @property
    def name(self):
        """Gets the name of this QualityConfig.  # noqa: E501


        :return: The name of this QualityConfig.  # noqa: E501
        :rtype: FaceQualityConfigName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QualityConfig.


        :param name: The name of this QualityConfig.  # noqa: E501
        :type name: FaceQualityConfigName
        """

        self._name = name

    @property
    def range(self):
        """Gets the range of this QualityConfig.  # noqa: E501

        The range of applicable values for this characteristic. If the returned in the Response value fits this range, the value is identified as compliant with the requirements.  # noqa: E501

        :return: The range of this QualityConfig.  # noqa: E501
        :rtype: [float]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this QualityConfig.

        The range of applicable values for this characteristic. If the returned in the Response value fits this range, the value is identified as compliant with the requirements.  # noqa: E501

        :param range: The range of this QualityConfig.  # noqa: E501
        :type range: [float]
        """
        if (self.local_vars_configuration.client_side_validation and
                range is not None and len(range) > 2):
            raise ValueError("Invalid value for `range`, number of items must be less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                range is not None and len(range) < 2):
            raise ValueError("Invalid value for `range`, number of items must be greater than or equal to `2`")  # noqa: E501

        self._range = range

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
        if not isinstance(other, QualityConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualityConfig):
            return True

        return self.to_dict() != other.to_dict()
