import base64
from typing import Union

from regula.facerecognition.webclient.ext.common import Base64String
from regula.facerecognition.webclient.gen import ApiValueError, CompareImage as GenCompareImage, ImageSource


class CompareImage(GenCompareImage):
    def __init__(self, index=None, format=None, type=None, data: Union[Base64String, bytes] = None, local_vars_configuration=None):
        if not data:
            raise ApiValueError(f"compare image {index} data: expected <not empty>")

        if not type:
            type = ImageSource.LIVE
        if isinstance(data, bytes):
            data = base64.b64encode(data).decode("utf-8")

        super().__init__(index, format, type, data, local_vars_configuration)
