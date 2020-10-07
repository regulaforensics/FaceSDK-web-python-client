from typing import Union

from regula.facerecognition.webclient.ext.common import Base64String, bytes_to_base64
from regula.facerecognition.webclient.gen import ImageLivenessItem as GenImageLivenessItem, ApiValueError


class ImageLivenessItem(GenImageLivenessItem):
    def __init__(self, data: Union[Base64String, bytes], local_vars_configuration=None):
        if not data:
            raise ApiValueError("image liveness frame: expected <not empty>")

        if isinstance(data, bytes):
            data = bytes_to_base64(data)

        super().__init__(data, local_vars_configuration)
