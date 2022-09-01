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


class QualityDetailsGroups(object):
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
        'total_count': 'int',
        'compliant_count': 'int',
    }

    attribute_map = {
        'group_id': 'groupId',
        'name': 'name',
        'total_count': 'totalCount',
        'compliant_count': 'compliantCount',
    }

    def __init__(self, group_id=None, name=None, total_count=None, compliant_count=None, local_vars_configuration=None):  # noqa: E501
        """QualityDetailsGroups - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_id = None
        self._name = None
        self._total_count = None
        self._compliant_count = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if total_count is not None:
            self.total_count = total_count
        if compliant_count is not None:
            self.compliant_count = compliant_count

    @property
    def group_id(self):
        """Gets the group_id of this QualityDetailsGroups.  # noqa: E501


        :return: The group_id of this QualityDetailsGroups.  # noqa: E501
        :rtype: FaceImageQualityGroups
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this QualityDetailsGroups.


        :param group_id: The group_id of this QualityDetailsGroups.  # noqa: E501
        :type group_id: FaceImageQualityGroups
        """

        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this QualityDetailsGroups.  # noqa: E501


        :return: The name of this QualityDetailsGroups.  # noqa: E501
        :rtype: FaceQualityConfigName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QualityDetailsGroups.


        :param name: The name of this QualityDetailsGroups.  # noqa: E501
        :type name: FaceQualityConfigName
        """

        self._name = name

    @property
    def total_count(self):
        """Gets the total_count of this QualityDetailsGroups.  # noqa: E501

        The total number of characteristics in the group.  # noqa: E501

        :return: The total_count of this QualityDetailsGroups.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this QualityDetailsGroups.

        The total number of characteristics in the group.  # noqa: E501

        :param total_count: The total_count of this QualityDetailsGroups.  # noqa: E501
        :type total_count: int
        """

        self._total_count = total_count

    @property
    def compliant_count(self):
        """Gets the compliant_count of this QualityDetailsGroups.  # noqa: E501

        The number of compliant characteristics in the group.  # noqa: E501

        :return: The compliant_count of this QualityDetailsGroups.  # noqa: E501
        :rtype: int
        """
        return self._compliant_count

    @compliant_count.setter
    def compliant_count(self, compliant_count):
        """Sets the compliant_count of this QualityDetailsGroups.

        The number of compliant characteristics in the group.  # noqa: E501

        :param compliant_count: The compliant_count of this QualityDetailsGroups.  # noqa: E501
        :type compliant_count: int
        """

        self._compliant_count = compliant_count

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
        if not isinstance(other, QualityDetailsGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualityDetailsGroups):
            return True

        return self.to_dict() != other.to_dict()
