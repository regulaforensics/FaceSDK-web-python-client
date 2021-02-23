from typing import List, Union

from regula.facerecognition.webclient.ext.common import Base64String
from regula.facerecognition.webclient.ext.models.compare_image import CompareImage
from regula.facerecognition.webclient.gen import CompareRequest as GenCompareRequest, ApiValueError


class CompareRequest(GenCompareRequest):
    def __init__(
            self, images: List[Union[CompareImage, Base64String, bytes]], thumbnails=False,
            local_vars_configuration=None
    ):
        if not images:
            raise ApiValueError(f"compare request images: expected size <more than 1>")

        input_images = []
        for index, item in enumerate(images):
            if isinstance(item, CompareImage):
                input_images.append(item)
            else:
                input_images.append(CompareImage(index, None, item, local_vars_configuration))

        super().__init__(
            images=input_images, local_vars_configuration=local_vars_configuration, thumbnails=thumbnails
        )
