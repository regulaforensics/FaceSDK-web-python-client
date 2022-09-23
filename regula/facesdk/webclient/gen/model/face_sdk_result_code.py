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


class FaceSDKResultCode(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    ""
    FACER_OK = int(0)

    ""
    FACER_NO_LICENSE = int(200)

    ""
    FACER_IS_NOT_INITIALIZED = int(201)

    ""
    FACER_COMMAND_IS_NOT_SUPPORTED = int(202)

    ""
    FACER_COMMAND_PARAMS_READ_ERROR = int(203)

    ""
    FACER_SEARCHER_INDEX_FILE_NOT_EXIST = int(204)

    ""
    FACER_SEARCHER_INDEX_FILE_READ_ERROR = int(205)

    ""
    FACER_SEARCHER_INDEX_FILE_DECRYPTION_ERROR = int(206)

    ""
    FACER_SEARCHER_INDEX_LOAD_ERROR = int(207)

    ""
    FACER_SEARCHER_WRONG_DESCRIPTOR_VERSION = int(208)

    ""
    FACER_SEARCHER_INDEX_FILE_ENCRYPTION_ERROR = int(209)

    ""
    FACER_SEARCHER_INDEX_FILE_SAVE_ERROR = int(210)

    ""
    FACER_SEARCHER_IMAGE_DECODE_ERROR = int(211)

    ""
    FACER_SEARCHER_ID_EXISTS_IN_INDEX = int(212)

    ""
    FACER_SEARCHER_ID_NOT_IN_INDEX = int(213)

    ""
    FACER_SEARCHER_NO_FACES = int(214)

    ""
    FACER_SEARCHER_DESCRIPTOR_EXTRACTOR_ERROR = int(215)

    ""
    FACER_SEARCHER_METADATA_READ_ERROR = int(216)

    ""
    FACER_SEARCHER_NO_SEARCH_LICENSE = int(217)

    ""
    FACER_SEARCHER_DESCRIPTOR_DECODE_ERROR = int(218)

    ""
    FACER_SEARCHER_DESCRIPTOR_WRONG_SIZE = int(219)

    ""
    FACER_SEARCHER_ZIP_IMAGE_READ_ERROR = int(220)

    ""
    FACER_SEARCHER_ZIP_META_READ_ERROR = int(221)

    ""
    FACER_SEARCHER_SIMILAR_PHOTOS_EXIST = int(222)

    ""
    FACER_SEARCHER_PERSON_ZIP_READ_ERROR = int(223)

    ""
    FACER_LESS_THAN_TWO_IMAGES_IN_REQUEST = int(224)

    ""
    FACER_SEARCHER_WRONG_ID = int(225)

    ""
    FACER_SEARCHER_ID_EXISTS_IN_DELETED = int(226)

    ""
    FACER_VIDEO_DECODE_ERROR = int(227)

    ""
    FACER_NOT_ENOUGH_FRAMES = int(228)

    ""
    FACER_OUTPUT_IS_NOT_DEFINED = int(229)

    allowable_values = [FACER_OK, FACER_NO_LICENSE, FACER_IS_NOT_INITIALIZED, FACER_COMMAND_IS_NOT_SUPPORTED, FACER_COMMAND_PARAMS_READ_ERROR, FACER_SEARCHER_INDEX_FILE_NOT_EXIST, FACER_SEARCHER_INDEX_FILE_READ_ERROR, FACER_SEARCHER_INDEX_FILE_DECRYPTION_ERROR, FACER_SEARCHER_INDEX_LOAD_ERROR, FACER_SEARCHER_WRONG_DESCRIPTOR_VERSION, FACER_SEARCHER_INDEX_FILE_ENCRYPTION_ERROR, FACER_SEARCHER_INDEX_FILE_SAVE_ERROR, FACER_SEARCHER_IMAGE_DECODE_ERROR, FACER_SEARCHER_ID_EXISTS_IN_INDEX, FACER_SEARCHER_ID_NOT_IN_INDEX, FACER_SEARCHER_NO_FACES, FACER_SEARCHER_DESCRIPTOR_EXTRACTOR_ERROR, FACER_SEARCHER_METADATA_READ_ERROR, FACER_SEARCHER_NO_SEARCH_LICENSE, FACER_SEARCHER_DESCRIPTOR_DECODE_ERROR, FACER_SEARCHER_DESCRIPTOR_WRONG_SIZE, FACER_SEARCHER_ZIP_IMAGE_READ_ERROR, FACER_SEARCHER_ZIP_META_READ_ERROR, FACER_SEARCHER_SIMILAR_PHOTOS_EXIST, FACER_SEARCHER_PERSON_ZIP_READ_ERROR, FACER_LESS_THAN_TWO_IMAGES_IN_REQUEST, FACER_SEARCHER_WRONG_ID, FACER_SEARCHER_ID_EXISTS_IN_DELETED, FACER_VIDEO_DECODE_ERROR, FACER_NOT_ENOUGH_FRAMES, FACER_OUTPUT_IS_NOT_DEFINED]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """FaceSDKResultCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, FaceSDKResultCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FaceSDKResultCode):
            return True

        return self.to_dict() != other.to_dict()
