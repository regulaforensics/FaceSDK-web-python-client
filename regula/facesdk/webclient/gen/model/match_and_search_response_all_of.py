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


class MatchAndSearchResponseAllOf(object):
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
        'results': '[MatchImageResult]',
        'elapsed_time': 'float',
        'metadata': '{str: (bool, date, datetime, dict, float, int, list, str, none_type)}',
        'detections': '[MatchAndSearchResponseAllOfDetections]',
    }

    attribute_map = {
        'results': 'results',
        'elapsed_time': 'elapsedTime',
        'metadata': 'metadata',
        'detections': 'detections',
    }

    def __init__(self, results=None, elapsed_time=None, metadata=None, detections=None, local_vars_configuration=None):  # noqa: E501
        """MatchAndSearchResponseAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._results = None
        self._elapsed_time = None
        self._metadata = None
        self._detections = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if metadata is not None:
            self.metadata = metadata
        if detections is not None:
            self.detections = detections

    @property
    def results(self):
        """Gets the results of this MatchAndSearchResponseAllOf.  # noqa: E501


        :return: The results of this MatchAndSearchResponseAllOf.  # noqa: E501
        :rtype: [MatchImageResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this MatchAndSearchResponseAllOf.


        :param results: The results of this MatchAndSearchResponseAllOf.  # noqa: E501
        :type results: [MatchImageResult]
        """

        self._results = results

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this MatchAndSearchResponseAllOf.  # noqa: E501


        :return: The elapsed_time of this MatchAndSearchResponseAllOf.  # noqa: E501
        :rtype: float
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this MatchAndSearchResponseAllOf.


        :param elapsed_time: The elapsed_time of this MatchAndSearchResponseAllOf.  # noqa: E501
        :type elapsed_time: float
        """

        self._elapsed_time = elapsed_time

    @property
    def metadata(self):
        """Gets the metadata of this MatchAndSearchResponseAllOf.  # noqa: E501

        A free-form object containing person's extended attributes.  # noqa: E501

        :return: The metadata of this MatchAndSearchResponseAllOf.  # noqa: E501
        :rtype: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MatchAndSearchResponseAllOf.

        A free-form object containing person's extended attributes.  # noqa: E501

        :param metadata: The metadata of this MatchAndSearchResponseAllOf.  # noqa: E501
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
        """

        self._metadata = metadata

    @property
    def detections(self):
        """Gets the detections of this MatchAndSearchResponseAllOf.  # noqa: E501


        :return: The detections of this MatchAndSearchResponseAllOf.  # noqa: E501
        :rtype: [MatchAndSearchResponseAllOfDetections]
        """
        return self._detections

    @detections.setter
    def detections(self, detections):
        """Sets the detections of this MatchAndSearchResponseAllOf.


        :param detections: The detections of this MatchAndSearchResponseAllOf.  # noqa: E501
        :type detections: [MatchAndSearchResponseAllOfDetections]
        """

        self._detections = detections

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
        if not isinstance(other, MatchAndSearchResponseAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchAndSearchResponseAllOf):
            return True

        return self.to_dict() != other.to_dict()
