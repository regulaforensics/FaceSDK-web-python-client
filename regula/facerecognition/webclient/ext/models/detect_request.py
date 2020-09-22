from typing import Union

from regula.facerecognition.webclient.ext.common import Base64String, bytes_to_base64
from regula.facerecognition.webclient.gen import DetectRequest as GetDetectRequest, ApiValueError


class DetectRequest(GetDetectRequest):
    def __init__(self, image: Union[Base64String, bytes], only_central_face=False, local_vars_configuration=None):
        if not image:
            raise ApiValueError(f"image: expected <not empty> - obtained <{image}>", "image")

        if isinstance(image, bytes):
            image = bytes_to_base64(image)

        super().__init__(image, only_central_face, local_vars_configuration)
