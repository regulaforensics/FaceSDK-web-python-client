from typing import Union

from regula.facesdk.webclient.ext.common import Base64String, bytes_to_base64
from regula.facesdk.webclient.gen import ApiValueError
from regula.facesdk.webclient.gen.models.process_param import ProcessParam
from regula.facesdk.webclient.gen.models import DetectRequest as GetDetectRequest


class DetectRequest(GetDetectRequest):
    def __init__(
            self,
            image: Union[Base64String, bytes],
            process_param: ProcessParam = None,
            tag=None,
            env=None,
            tenant=None
    ):
        if not image:
            raise ApiValueError(f"image: expected <not empty> - obtained <{image}>", "image")

        if isinstance(image, bytes):
            image = bytes_to_base64(image)

        super().__init__(
            image=image,
            tag=tag,
            process_param=process_param,
            env=env,
            tenant=tenant
        )
