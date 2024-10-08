# coding: utf-8

"""
    Regula Face SDK Web API

    <a href=\"https://regulaforensics.com/products/face-recognition-sdk/  \" target=\"_blank\">Regula Face SDK</a> is a cross-platform biometric verification solution for a digital identity verification process and image quality assurance. The SDK enables convenient and reliable face capture on the client side (mobile, web, and desktop) and further processing on the client or server side.   The Face SDK includes the following features:  * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-detection\" target=\"_blank\">Face detection and image quality assessment</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-comparison-11\" target=\"_blank\">Face match (1:1)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#face-identification-1n\" target=\"_blank\">Face search (1:N)</a> * <a href=\"https://docs.regulaforensics.com/develop/face-sdk/overview/introduction/#liveness-assessment\" target=\"_blank\">Liveness detection</a>  Here is the <a href=\"https://github.com/regulaforensics/FaceSDK-web-openapi  \" target=\"_blank\">OpenAPI specification on GitHub</a>.   ### Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 6.2.0
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
    FR_IMAGE_EMPTY = int(1)

    ""
    FR_FACE_NOT_DETECTED = int(2)

    ""
    FR_LANDMARKS_NOT_DETECTED = int(3)

    ""
    FR_FACE_ALIGHNER_FAILED = int(4)

    ""
    FR_DESCRIPTOR_EXTRACTOR_ERROR = int(5)

    ""
    FR_IMAGE_DECODE_ERROR = int(6)

    ""
    FR_INTERNAL_ERROR = int(7)

    ""
    FACER_CONFIG_ERROR = int(199)

    ""
    FACER_NO_LICENSE = int(200)

    ""
    FACER_IS_NOT_INITIALIZED = int(201)

    ""
    FACER_COMMAND_IS_NOT_SUPPORTED = int(202)

    ""
    FACER_COMMAND_PARAMS_READ_ERROR = int(203)

    ""
    FACER_LESS_THAN_TWO_IMAGES_IN_REQUEST = int(224)

    ""
    FACER_VIDEO_DECODE_ERROR = int(227)

    ""
    FACER_NOT_ENOUGH_FRAMES = int(228)

    ""
    FACER_OUTPUT_IS_NOT_DEFINED = int(229)

    ""
    FACER_CLOSED_EYES_DETECTED = int(230)

    ""
    FACER_LOW_QUALITY = int(231)

    ""
    FACER_HIGH_ASYMMETRY = int(232)

    ""
    FACER_FACE_OVER_EMOTIONAL = int(233)

    ""
    FACER_SUNGLASSES_DETECTED = int(234)

    ""
    FACER_SMALL_AGE = int(235)

    ""
    FACER_HEADDRESS_DETECTED = int(236)

    ""
    FACER_FACES_NOT_MATCHED = int(237)

    ""
    FACER_IMAGES_COUNT_LIMIT_EXCEEDED = int(238)

    ""
    FACER_MEDICINE_MASK_DETECTED = int(239)

    ""
    FACER_OCCLUSION_DETECTED = int(240)

    ""
    FACER_FOREHEAD_GLASSES_DETECTED = int(242)

    ""
    FACER_MOUTH_OPENED = int(243)

    ""
    FACER_ART_MASK_DETECTED = int(244)

    ""
    FACER_ELECTRONIC_DEVICE_DETECTED = int(245)

    ""
    FACER_TRACK_BREAK = int(246)

    ""
    FACER_WRONG_GEO = int(247)

    ""
    FACER_WRONG_OF = int(248)

    ""
    FACER_WRONG_VIEW = int(249)

    ""
    FACER_TIMEOUT_LIVENESS_TRANSACTION = int(250)

    ""
    FACER_FAILED_LIVENESS_TRANSACTION = int(251)

    ""
    FACER_ABORTED_LIVENESS_TRANSACTION = int(252)

    ""
    FACER_GENERAL_ERROR = int(253)

    ""
    FACER_PASSIVE_LIVENESS_FAIL = int(254)

    allowable_values = [FACER_OK, FR_IMAGE_EMPTY, FR_FACE_NOT_DETECTED, FR_LANDMARKS_NOT_DETECTED, FR_FACE_ALIGHNER_FAILED, FR_DESCRIPTOR_EXTRACTOR_ERROR, FR_IMAGE_DECODE_ERROR, FR_INTERNAL_ERROR, FACER_CONFIG_ERROR, FACER_NO_LICENSE, FACER_IS_NOT_INITIALIZED, FACER_COMMAND_IS_NOT_SUPPORTED, FACER_COMMAND_PARAMS_READ_ERROR, FACER_LESS_THAN_TWO_IMAGES_IN_REQUEST, FACER_VIDEO_DECODE_ERROR, FACER_NOT_ENOUGH_FRAMES, FACER_OUTPUT_IS_NOT_DEFINED, FACER_CLOSED_EYES_DETECTED, FACER_LOW_QUALITY, FACER_HIGH_ASYMMETRY, FACER_FACE_OVER_EMOTIONAL, FACER_SUNGLASSES_DETECTED, FACER_SMALL_AGE, FACER_HEADDRESS_DETECTED, FACER_FACES_NOT_MATCHED, FACER_IMAGES_COUNT_LIMIT_EXCEEDED, FACER_MEDICINE_MASK_DETECTED, FACER_OCCLUSION_DETECTED, FACER_FOREHEAD_GLASSES_DETECTED, FACER_MOUTH_OPENED, FACER_ART_MASK_DETECTED, FACER_ELECTRONIC_DEVICE_DETECTED, FACER_TRACK_BREAK, FACER_WRONG_GEO, FACER_WRONG_OF, FACER_WRONG_VIEW, FACER_TIMEOUT_LIVENESS_TRANSACTION, FACER_FAILED_LIVENESS_TRANSACTION, FACER_ABORTED_LIVENESS_TRANSACTION, FACER_GENERAL_ERROR, FACER_PASSIVE_LIVENESS_FAIL]  # noqa: E501

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
