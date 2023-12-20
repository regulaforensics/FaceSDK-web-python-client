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


class FaceQualityConfigName(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    ""
    IMAGE_WIDTH = "ImageWidth"

    ""
    IMAGE_HEIGHT = "ImageHeight"

    ""
    IMAGE_WIDTH_TO_HEIGHT = "ImageWidthToHeight"

    ""
    IMAGE_CHANNELS_NUMBER = "ImageChannelsNumber"

    ""
    PADDING_RATIO = "PaddingRatio"

    ""
    FACE_MID_POINT_HORIZONTAL_POSITION = "FaceMidPointHorizontalPosition"

    ""
    FACE_MID_POINT_VERTICAL_POSITION = "FaceMidPointVerticalPosition"

    ""
    HEAD_WIDTH_RATIO = "HeadWidthRatio"

    ""
    HEAD_HEIGHT_RATIO = "HeadHeightRatio"

    ""
    EYES_DISTANCE = "EyesDistance"

    ""
    YAW = "Yaw"

    ""
    PITCH = "Pitch"

    ""
    ROLL = "Roll"

    ""
    BLUR_LEVEL = "BlurLevel"

    ""
    NOISE_LEVEL = "NoiseLevel"

    ""
    EYE_RIGHT_CLOSED = "EyeRightClosed"

    ""
    EYE_LEFT_CLOSED = "EyeLeftClosed"

    ""
    EYE_RIGHT_OCCLUDED = "EyeRightOccluded"

    ""
    EYE_LEFT_OCCLUDED = "EyeLeftOccluded"

    ""
    EYES_RED = "EyesRed"

    ""
    EYE_RIGHT_COVERED_WITH_HAIR = "EyeRightCoveredWithHair"

    ""
    EYE_LEFT_COVERED_WITH_HAIR = "EyeLeftCoveredWithHair"

    ""
    OFF_GAZE = "OffGaze"

    ""
    FACE_DYNAMIC_RANGE = "FaceDynamicRange"

    ""
    UNNATURAL_SKIN_TONE = "UnnaturalSkinTone"

    ""
    TOO_DARK = "TooDark"

    ""
    TOO_LIGHT = "TooLight"

    ""
    FACE_GLARE = "FaceGlare"

    ""
    SHADOWS_ON_FACE = "ShadowsOnFace"

    ""
    DARK_GLASSES = "DarkGlasses"

    ""
    REFLECTION_ON_GLASSES = "ReflectionOnGlasses"

    ""
    FRAMES_TOO_HEAVY = "FramesTooHeavy"

    ""
    FACE_OCCLUDED = "FaceOccluded"

    ""
    HEAD_COVERING = "HeadCovering"

    ""
    BACKGROUND_UNIFORMITY = "BackgroundUniformity"

    ""
    SHADOWS_ON_BACKGROUND = "ShadowsOnBackground"

    ""
    OTHER_FACES = "OtherFaces"

    ""
    SHOULDERS_POSE = "ShouldersPose"

    ""
    EXPRESSION_LEVEL = "ExpressionLevel"

    ""
    MOUTH_OPEN = "MouthOpen"

    ""
    FOREHEAD_COVERING = "ForeheadCovering"

    ""
    SMILE = "Smile"

    ""
    STRONG_MAKEUP = "StrongMakeup"

    ""
    HEADPHONES = "Headphones"

    ""
    MEDICAL_MASK = "MedicalMask"

    ""
    BACKGROUND_COLOR_MATCH = "BackgroundColorMatch"

    ""
    ART_FACE = "ArtFace"

    ""
    CONTACT_LENSES = "ContactLenses"

    allowable_values = [IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_WIDTH_TO_HEIGHT, IMAGE_CHANNELS_NUMBER, PADDING_RATIO, FACE_MID_POINT_HORIZONTAL_POSITION, FACE_MID_POINT_VERTICAL_POSITION, HEAD_WIDTH_RATIO, HEAD_HEIGHT_RATIO, EYES_DISTANCE, YAW, PITCH, ROLL, BLUR_LEVEL, NOISE_LEVEL, EYE_RIGHT_CLOSED, EYE_LEFT_CLOSED, EYE_RIGHT_OCCLUDED, EYE_LEFT_OCCLUDED, EYES_RED, EYE_RIGHT_COVERED_WITH_HAIR, EYE_LEFT_COVERED_WITH_HAIR, OFF_GAZE, FACE_DYNAMIC_RANGE, UNNATURAL_SKIN_TONE, TOO_DARK, TOO_LIGHT, FACE_GLARE, SHADOWS_ON_FACE, DARK_GLASSES, REFLECTION_ON_GLASSES, FRAMES_TOO_HEAVY, FACE_OCCLUDED, HEAD_COVERING, BACKGROUND_UNIFORMITY, SHADOWS_ON_BACKGROUND, OTHER_FACES, SHOULDERS_POSE, EXPRESSION_LEVEL, MOUTH_OPEN, FOREHEAD_COVERING, SMILE, STRONG_MAKEUP, HEADPHONES, MEDICAL_MASK, BACKGROUND_COLOR_MATCH, ART_FACE, CONTACT_LENSES]  # noqa: E501

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
        """FaceQualityConfigName - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, FaceQualityConfigName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FaceQualityConfigName):
            return True

        return self.to_dict() != other.to_dict()
