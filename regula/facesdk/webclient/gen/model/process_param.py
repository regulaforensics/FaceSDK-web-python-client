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


class ProcessParam(object):
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
        'scenario': 'FaceQualityScenarios',
        'only_central_face': 'bool',
        'output_image_params': 'OutputImageParams',
        'quality': 'QualityRequest',
        'attributes': 'ProcessParamAttributes',
    }

    attribute_map = {
        'scenario': 'scenario',
        'only_central_face': 'onlyCentralFace',
        'output_image_params': 'outputImageParams',
        'quality': 'quality',
        'attributes': 'attributes',
    }

    def __init__(self, scenario=None, only_central_face=None, output_image_params=None, quality=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """ProcessParam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scenario = None
        self._only_central_face = None
        self._output_image_params = None
        self._quality = None
        self._attributes = None
        self.discriminator = None

        if scenario is not None:
            self.scenario = scenario
        if only_central_face is not None:
            self.only_central_face = only_central_face
        if output_image_params is not None:
            self.output_image_params = output_image_params
        if quality is not None:
            self.quality = quality
        if attributes is not None:
            self.attributes = attributes

    @property
    def scenario(self):
        """Gets the scenario of this ProcessParam.  # noqa: E501


        :return: The scenario of this ProcessParam.  # noqa: E501
        :rtype: FaceQualityScenarios
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this ProcessParam.


        :param scenario: The scenario of this ProcessParam.  # noqa: E501
        :type scenario: FaceQualityScenarios
        """

        self._scenario = scenario

    @property
    def only_central_face(self):
        """Gets the only_central_face of this ProcessParam.  # noqa: E501

        Whether to process only the central face on the image (true) or all the faces (false).  # noqa: E501

        :return: The only_central_face of this ProcessParam.  # noqa: E501
        :rtype: bool
        """
        return self._only_central_face

    @only_central_face.setter
    def only_central_face(self, only_central_face):
        """Sets the only_central_face of this ProcessParam.

        Whether to process only the central face on the image (true) or all the faces (false).  # noqa: E501

        :param only_central_face: The only_central_face of this ProcessParam.  # noqa: E501
        :type only_central_face: bool
        """

        self._only_central_face = only_central_face

    @property
    def output_image_params(self):
        """Gets the output_image_params of this ProcessParam.  # noqa: E501


        :return: The output_image_params of this ProcessParam.  # noqa: E501
        :rtype: OutputImageParams
        """
        return self._output_image_params

    @output_image_params.setter
    def output_image_params(self, output_image_params):
        """Sets the output_image_params of this ProcessParam.


        :param output_image_params: The output_image_params of this ProcessParam.  # noqa: E501
        :type output_image_params: OutputImageParams
        """

        self._output_image_params = output_image_params

    @property
    def quality(self):
        """Gets the quality of this ProcessParam.  # noqa: E501


        :return: The quality of this ProcessParam.  # noqa: E501
        :rtype: QualityRequest
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this ProcessParam.


        :param quality: The quality of this ProcessParam.  # noqa: E501
        :type quality: QualityRequest
        """

        self._quality = quality

    @property
    def attributes(self):
        """Gets the attributes of this ProcessParam.  # noqa: E501


        :return: The attributes of this ProcessParam.  # noqa: E501
        :rtype: ProcessParamAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ProcessParam.


        :param attributes: The attributes of this ProcessParam.  # noqa: E501
        :type attributes: ProcessParamAttributes
        """

        self._attributes = attributes

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
        if not isinstance(other, ProcessParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessParam):
            return True

        return self.to_dict() != other.to_dict()
