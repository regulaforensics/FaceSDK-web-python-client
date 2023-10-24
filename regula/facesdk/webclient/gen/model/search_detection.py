# coding: utf-8

"""
    Regula FaceSDK Web api

    Regula FaceSDK Web API # Clients * [JavaScript](https://github.com/regulaforensics/FaceSDK-web-js-client) client for the browser and node.js based on axios * [Java](https://github.com/regulaforensics/FaceSDK-web-java-client) client compatible with jvm and android * [Python](https://github.com/regulaforensics/FaceSDK-web-python-client) 3.5+ client * [C#](https://github.com/regulaforensics/FaceSDK-web-csharp-client) client for .NET & .NET Core   # noqa: E501

    The version of the OpenAPI document: 5.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class SearchDetection(object):
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
        'code': 'int',
        'crop': 'str',
        'detector_type': 'int',
        'hash': 'str',
        'idx': 'int',
        'image': 'str',
        'landmarks': '[[int]]',
        'landmarks_type': 'int',
        'msg': 'str',
        'roi': 'FaceRectangular',
        'version_sdk': 'str',
    }

    attribute_map = {
        'code': 'code',
        'crop': 'crop',
        'detector_type': 'detectorType',
        'hash': 'hash',
        'idx': 'idx',
        'image': 'image',
        'landmarks': 'landmarks',
        'landmarks_type': 'landmarksType',
        'msg': 'msg',
        'roi': 'roi',
        'version_sdk': 'versionSDK',
    }

    def __init__(self, code=None, crop=None, detector_type=None, hash=None, idx=None, image=None, landmarks=None, landmarks_type=None, msg=None, roi=None, version_sdk=None, local_vars_configuration=None):  # noqa: E501
        """SearchDetection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._crop = None
        self._detector_type = None
        self._hash = None
        self._idx = None
        self._image = None
        self._landmarks = None
        self._landmarks_type = None
        self._msg = None
        self._roi = None
        self._version_sdk = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if crop is not None:
            self.crop = crop
        if detector_type is not None:
            self.detector_type = detector_type
        if hash is not None:
            self.hash = hash
        if idx is not None:
            self.idx = idx
        if image is not None:
            self.image = image
        if landmarks is not None:
            self.landmarks = landmarks
        if landmarks_type is not None:
            self.landmarks_type = landmarks_type
        if msg is not None:
            self.msg = msg
        if roi is not None:
            self.roi = roi
        if version_sdk is not None:
            self.version_sdk = version_sdk

    @property
    def code(self):
        """Gets the code of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The code of this SearchDetection.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SearchDetection.

        Internal.  # noqa: E501

        :param code: The code of this SearchDetection.  # noqa: E501
        :type code: int
        """

        self._code = code

    @property
    def crop(self):
        """Gets the crop of this SearchDetection.  # noqa: E501

        Base64 of the aligned and cropped portrait.  # noqa: E501

        :return: The crop of this SearchDetection.  # noqa: E501
        :rtype: str
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this SearchDetection.

        Base64 of the aligned and cropped portrait.  # noqa: E501

        :param crop: The crop of this SearchDetection.  # noqa: E501
        :type crop: str
        """

        self._crop = crop

    @property
    def detector_type(self):
        """Gets the detector_type of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The detector_type of this SearchDetection.  # noqa: E501
        :rtype: int
        """
        return self._detector_type

    @detector_type.setter
    def detector_type(self, detector_type):
        """Sets the detector_type of this SearchDetection.

        Internal.  # noqa: E501

        :param detector_type: The detector_type of this SearchDetection.  # noqa: E501
        :type detector_type: int
        """

        self._detector_type = detector_type

    @property
    def hash(self):
        """Gets the hash of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The hash of this SearchDetection.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this SearchDetection.

        Internal.  # noqa: E501

        :param hash: The hash of this SearchDetection.  # noqa: E501
        :type hash: str
        """

        self._hash = hash

    @property
    def idx(self):
        """Gets the idx of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The idx of this SearchDetection.  # noqa: E501
        :rtype: int
        """
        return self._idx

    @idx.setter
    def idx(self, idx):
        """Sets the idx of this SearchDetection.

        Internal.  # noqa: E501

        :param idx: The idx of this SearchDetection.  # noqa: E501
        :type idx: int
        """

        self._idx = idx

    @property
    def image(self):
        """Gets the image of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The image of this SearchDetection.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this SearchDetection.

        Internal.  # noqa: E501

        :param image: The image of this SearchDetection.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def landmarks(self):
        """Gets the landmarks of this SearchDetection.  # noqa: E501

        Absolute coordinates (x,y) of five points of each detected face: left eye, right eye, nose, left point of lips, right point of lips.  # noqa: E501

        :return: The landmarks of this SearchDetection.  # noqa: E501
        :rtype: [[int]]
        """
        return self._landmarks

    @landmarks.setter
    def landmarks(self, landmarks):
        """Sets the landmarks of this SearchDetection.

        Absolute coordinates (x,y) of five points of each detected face: left eye, right eye, nose, left point of lips, right point of lips.  # noqa: E501

        :param landmarks: The landmarks of this SearchDetection.  # noqa: E501
        :type landmarks: [[int]]
        """

        self._landmarks = landmarks

    @property
    def landmarks_type(self):
        """Gets the landmarks_type of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The landmarks_type of this SearchDetection.  # noqa: E501
        :rtype: int
        """
        return self._landmarks_type

    @landmarks_type.setter
    def landmarks_type(self, landmarks_type):
        """Sets the landmarks_type of this SearchDetection.

        Internal.  # noqa: E501

        :param landmarks_type: The landmarks_type of this SearchDetection.  # noqa: E501
        :type landmarks_type: int
        """

        self._landmarks_type = landmarks_type

    @property
    def msg(self):
        """Gets the msg of this SearchDetection.  # noqa: E501

        Internal.  # noqa: E501

        :return: The msg of this SearchDetection.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SearchDetection.

        Internal.  # noqa: E501

        :param msg: The msg of this SearchDetection.  # noqa: E501
        :type msg: str
        """

        self._msg = msg

    @property
    def roi(self):
        """Gets the roi of this SearchDetection.  # noqa: E501


        :return: The roi of this SearchDetection.  # noqa: E501
        :rtype: FaceRectangular
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this SearchDetection.


        :param roi: The roi of this SearchDetection.  # noqa: E501
        :type roi: FaceRectangular
        """

        self._roi = roi

    @property
    def version_sdk(self):
        """Gets the version_sdk of this SearchDetection.  # noqa: E501


        :return: The version_sdk of this SearchDetection.  # noqa: E501
        :rtype: str
        """
        return self._version_sdk

    @version_sdk.setter
    def version_sdk(self, version_sdk):
        """Sets the version_sdk of this SearchDetection.


        :param version_sdk: The version_sdk of this SearchDetection.  # noqa: E501
        :type version_sdk: str
        """

        self._version_sdk = version_sdk

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
        if not isinstance(other, SearchDetection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchDetection):
            return True

        return self.to_dict() != other.to_dict()
