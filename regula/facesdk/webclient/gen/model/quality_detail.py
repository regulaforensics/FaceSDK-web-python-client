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


class QualityDetail(object):
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
        'group_id': 'FaceImageQualityGroups',
        'name': 'FaceQualityConfigName',
        'range': '[float]',
        'status': 'FaceImageQualityStatus',
        'value': 'float',
    }

    attribute_map = {
        'group_id': 'groupId',
        'name': 'name',
        'range': 'range',
        'status': 'status',
        'value': 'value',
    }

    def __init__(self, group_id=None, name=None, range=None, status=None, value=None, local_vars_configuration=None):  # noqa: E501
        """QualityDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_id = None
        self._name = None
        self._range = None
        self._status = None
        self._value = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if range is not None:
            self.range = range
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value

    @property
    def group_id(self):
        """Gets the group_id of this QualityDetail.  # noqa: E501


        :return: The group_id of this QualityDetail.  # noqa: E501
        :rtype: FaceImageQualityGroups
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this QualityDetail.


        :param group_id: The group_id of this QualityDetail.  # noqa: E501
        :type group_id: FaceImageQualityGroups
        """

        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this QualityDetail.  # noqa: E501


        :return: The name of this QualityDetail.  # noqa: E501
        :rtype: FaceQualityConfigName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QualityDetail.


        :param name: The name of this QualityDetail.  # noqa: E501
        :type name: FaceQualityConfigName
        """

        self._name = name

    @property
    def range(self):
        """Gets the range of this QualityDetail.  # noqa: E501

        The range of set values for this characteristic.  # noqa: E501

        :return: The range of this QualityDetail.  # noqa: E501
        :rtype: [float]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this QualityDetail.

        The range of set values for this characteristic.  # noqa: E501

        :param range: The range of this QualityDetail.  # noqa: E501
        :type range: [float]
        """
        if (self.local_vars_configuration.client_side_validation and
                range is not None and len(range) > 2):
            raise ValueError("Invalid value for `range`, number of items must be less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                range is not None and len(range) < 2):
            raise ValueError("Invalid value for `range`, number of items must be greater than or equal to `2`")  # noqa: E501

        self._range = range

    @property
    def status(self):
        """Gets the status of this QualityDetail.  # noqa: E501


        :return: The status of this QualityDetail.  # noqa: E501
        :rtype: FaceImageQualityStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QualityDetail.


        :param status: The status of this QualityDetail.  # noqa: E501
        :type status: FaceImageQualityStatus
        """

        self._status = status

    @property
    def value(self):
        """Gets the value of this QualityDetail.  # noqa: E501

        The assessed value for the characteristic, returned in the set units.  # noqa: E501

        :return: The value of this QualityDetail.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this QualityDetail.

        The assessed value for the characteristic, returned in the set units.  # noqa: E501

        :param value: The value of this QualityDetail.  # noqa: E501
        :type value: float
        """

        self._value = value

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
        if not isinstance(other, QualityDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualityDetail):
            return True

        return self.to_dict() != other.to_dict()