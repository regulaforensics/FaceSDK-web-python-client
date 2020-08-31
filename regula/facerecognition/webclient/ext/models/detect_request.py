from typing import Optional, Union

from regula.facerecognition.webclient.ext.common import Base64String, bytes_to_base64
from regula.facerecognition.webclient.gen import DetectRequest as GetDetectRequest


class DetectRequest(GetDetectRequest):
    def __init__(self, image: Optional[Union[Base64String, bytes]]=None, only_central_face=False, local_vars_configuration=None):
        if isinstance(image, bytes):
            image = bytes_to_base64(image)

        super().__init__(image, only_central_face, local_vars_configuration)
