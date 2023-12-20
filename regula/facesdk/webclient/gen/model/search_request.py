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


class SearchRequest(object):
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
        'create_person': 'SearchParametersCreatePerson',
        'group_ids': '[str]',
        'tag': 'str',
        'image': 'ImageFieldsImage',
        'output_image_params': 'OutputImageParams',
        'detect_all': 'bool',
        'threshold': 'float',
        'limit': 'int',
    }

    attribute_map = {
        'create_person': 'createPerson',
        'group_ids': 'groupIds',
        'tag': 'tag',
        'image': 'image',
        'output_image_params': 'outputImageParams',
        'detect_all': 'detectAll',
        'threshold': 'threshold',
        'limit': 'limit',
    }

    def __init__(self, create_person=None, group_ids=None, tag=None, image=None, output_image_params=None, detect_all=False, threshold=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """SearchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_person = None
        self._group_ids = None
        self._tag = None
        self._image = None
        self._output_image_params = None
        self._detect_all = None
        self._threshold = None
        self._limit = None
        self.discriminator = None

        if create_person is not None:
            self.create_person = create_person
        if group_ids is not None:
            self.group_ids = group_ids
        if tag is not None:
            self.tag = tag
        if image is not None:
            self.image = image
        if output_image_params is not None:
            self.output_image_params = output_image_params
        if detect_all is not None:
            self.detect_all = detect_all
        if threshold is not None:
            self.threshold = threshold
        if limit is not None:
            self.limit = limit

    @property
    def create_person(self):
        """Gets the create_person of this SearchRequest.  # noqa: E501


        :return: The create_person of this SearchRequest.  # noqa: E501
        :rtype: SearchParametersCreatePerson
        """
        return self._create_person

    @create_person.setter
    def create_person(self, create_person):
        """Sets the create_person of this SearchRequest.


        :param create_person: The create_person of this SearchRequest.  # noqa: E501
        :type create_person: SearchParametersCreatePerson
        """

        self._create_person = create_person

    @property
    def group_ids(self):
        """Gets the group_ids of this SearchRequest.  # noqa: E501

        IDs of the groups in which the search is performed.  # noqa: E501

        :return: The group_ids of this SearchRequest.  # noqa: E501
        :rtype: [str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this SearchRequest.

        IDs of the groups in which the search is performed.  # noqa: E501

        :param group_ids: The group_ids of this SearchRequest.  # noqa: E501
        :type group_ids: [str]
        """

        self._group_ids = group_ids

    @property
    def tag(self):
        """Gets the tag of this SearchRequest.  # noqa: E501

        Session identificator.  # noqa: E501

        :return: The tag of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SearchRequest.

        Session identificator.  # noqa: E501

        :param tag: The tag of this SearchRequest.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def image(self):
        """Gets the image of this SearchRequest.  # noqa: E501


        :return: The image of this SearchRequest.  # noqa: E501
        :rtype: ImageFieldsImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this SearchRequest.


        :param image: The image of this SearchRequest.  # noqa: E501
        :type image: ImageFieldsImage
        """

        self._image = image

    @property
    def output_image_params(self):
        """Gets the output_image_params of this SearchRequest.  # noqa: E501


        :return: The output_image_params of this SearchRequest.  # noqa: E501
        :rtype: OutputImageParams
        """
        return self._output_image_params

    @output_image_params.setter
    def output_image_params(self, output_image_params):
        """Sets the output_image_params of this SearchRequest.


        :param output_image_params: The output_image_params of this SearchRequest.  # noqa: E501
        :type output_image_params: OutputImageParams
        """

        self._output_image_params = output_image_params

    @property
    def detect_all(self):
        """Gets the detect_all of this SearchRequest.  # noqa: E501

        Whether to detect all faces in the image. If set to false, only the most central face is detected.  # noqa: E501

        :return: The detect_all of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._detect_all

    @detect_all.setter
    def detect_all(self, detect_all):
        """Sets the detect_all of this SearchRequest.

        Whether to detect all faces in the image. If set to false, only the most central face is detected.  # noqa: E501

        :param detect_all: The detect_all of this SearchRequest.  # noqa: E501
        :type detect_all: bool
        """

        self._detect_all = detect_all

    @property
    def threshold(self):
        """Gets the threshold of this SearchRequest.  # noqa: E501

        The similarity threshold.  # noqa: E501

        :return: The threshold of this SearchRequest.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this SearchRequest.

        The similarity threshold.  # noqa: E501

        :param threshold: The threshold of this SearchRequest.  # noqa: E501
        :type threshold: float
        """

        self._threshold = threshold

    @property
    def limit(self):
        """Gets the limit of this SearchRequest.  # noqa: E501

        The maximum number of results to be returned.  # noqa: E501

        :return: The limit of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchRequest.

        The maximum number of results to be returned.  # noqa: E501

        :param limit: The limit of this SearchRequest.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

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
        if not isinstance(other, SearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchRequest):
            return True

        return self.to_dict() != other.to_dict()
