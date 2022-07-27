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


class MatchImageResult(object):
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
        'first_index': 'int',
        'first_face_index': 'float',
        'second_index': 'int',
        'second_face_index': 'float',
        'score': 'float',
        'similarity': 'float',
        'error_code': 'FaceSDKResultCode',
        'error_msg': 'str'
    }

    attribute_map = {
        'first_index': 'firstIndex',
        'first_face_index': 'firstFaceIndex',
        'second_index': 'secondIndex',
        'second_face_index': 'secondFaceIndex',
        'score': 'score',
        'similarity': 'similarity',
        'error_code': 'errorCode',
        'error_msg': 'errorMsg'
    }

    def __init__(self, first_index=None, first_face_index=None, second_index=None, second_face_index=None, score=None, similarity=None, error_code=None, error_msg=None, local_vars_configuration=None):  # noqa: E501
        """MatchImageResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._first_index = None
        self._first_face_index = None
        self._second_index = None
        self._second_face_index = None
        self._score = None
        self._similarity = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.first_index = first_index
        if first_face_index is not None:
            self.first_face_index = first_face_index
        self.second_index = second_index
        if second_face_index is not None:
            self.second_face_index = second_face_index
        if score is not None:
            self.score = score
        if similarity is not None:
            self.similarity = similarity
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def first_index(self):
        """Gets the first_index of this MatchImageResult.  # noqa: E501

        Image index used to identify input photos between themselves. If not specified, than input list index is used  # noqa: E501

        :return: The first_index of this MatchImageResult.  # noqa: E501
        :rtype: int
        """
        return self._first_index

    @first_index.setter
    def first_index(self, first_index):
        """Sets the first_index of this MatchImageResult.

        Image index used to identify input photos between themselves. If not specified, than input list index is used  # noqa: E501

        :param first_index: The first_index of this MatchImageResult.  # noqa: E501
        :type first_index: int
        """
        if self.local_vars_configuration.client_side_validation and first_index is None:  # noqa: E501
            raise ValueError("Invalid value for `first_index`, must not be `None`")  # noqa: E501

        self._first_index = first_index

    @property
    def first_face_index(self):
        """Gets the first_face_index of this MatchImageResult.  # noqa: E501

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :return: The first_face_index of this MatchImageResult.  # noqa: E501
        :rtype: float
        """
        return self._first_face_index

    @first_face_index.setter
    def first_face_index(self, first_face_index):
        """Sets the first_face_index of this MatchImageResult.

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :param first_face_index: The first_face_index of this MatchImageResult.  # noqa: E501
        :type first_face_index: float
        """

        self._first_face_index = first_face_index

    @property
    def second_index(self):
        """Gets the second_index of this MatchImageResult.  # noqa: E501

        Image index used to identify input photos between themselves. If not specified, than input list index is used  # noqa: E501

        :return: The second_index of this MatchImageResult.  # noqa: E501
        :rtype: int
        """
        return self._second_index

    @second_index.setter
    def second_index(self, second_index):
        """Sets the second_index of this MatchImageResult.

        Image index used to identify input photos between themselves. If not specified, than input list index is used  # noqa: E501

        :param second_index: The second_index of this MatchImageResult.  # noqa: E501
        :type second_index: int
        """
        if self.local_vars_configuration.client_side_validation and second_index is None:  # noqa: E501
            raise ValueError("Invalid value for `second_index`, must not be `None`")  # noqa: E501

        self._second_index = second_index

    @property
    def second_face_index(self):
        """Gets the second_face_index of this MatchImageResult.  # noqa: E501

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :return: The second_face_index of this MatchImageResult.  # noqa: E501
        :rtype: float
        """
        return self._second_face_index

    @second_face_index.setter
    def second_face_index(self, second_face_index):
        """Sets the second_face_index of this MatchImageResult.

        Faces index used to identify faces in scope of one photo.  # noqa: E501

        :param second_face_index: The second_face_index of this MatchImageResult.  # noqa: E501
        :type second_face_index: float
        """

        self._second_face_index = second_face_index

    @property
    def score(self):
        """Gets the score of this MatchImageResult.  # noqa: E501


        :return: The score of this MatchImageResult.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this MatchImageResult.


        :param score: The score of this MatchImageResult.  # noqa: E501
        :type score: float
        """

        self._score = score

    @property
    def similarity(self):
        """Gets the similarity of this MatchImageResult.  # noqa: E501


        :return: The similarity of this MatchImageResult.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this MatchImageResult.


        :param similarity: The similarity of this MatchImageResult.  # noqa: E501
        :type similarity: float
        """

        self._similarity = similarity

    @property
    def error_code(self):
        """Gets the error_code of this MatchImageResult.  # noqa: E501


        :return: The error_code of this MatchImageResult.  # noqa: E501
        :rtype: FaceSDKResultCode
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this MatchImageResult.


        :param error_code: The error_code of this MatchImageResult.  # noqa: E501
        :type error_code: FaceSDKResultCode
        """

        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this MatchImageResult.  # noqa: E501


        :return: The error_msg of this MatchImageResult.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this MatchImageResult.


        :param error_msg: The error_msg of this MatchImageResult.  # noqa: E501
        :type error_msg: str
        """

        self._error_msg = error_msg

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
        if not isinstance(other, MatchImageResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchImageResult):
            return True

        return self.to_dict() != other.to_dict()
