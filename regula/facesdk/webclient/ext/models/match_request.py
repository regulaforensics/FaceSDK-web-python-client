from typing import List, Union

from regula.facesdk.webclient.ext.common import Base64String
from regula.facesdk.webclient.ext.models.match_image import MatchImage
from regula.facesdk.webclient.gen import ApiValueError
from regula.facesdk.webclient.gen.models import MatchRequest as GenMatchRequest


class MatchRequest(GenMatchRequest):
    def __init__(
            self,
            images: List[Union[MatchImage, Base64String, bytes]],
            output_image_params=None,
            tag=None,
            env=None,
            tenant=None
    ):
        if not images:
            raise ApiValueError(f"compare request images: expected size <more than 1>")

        input_images = []
        for index, item in enumerate(images):
            if isinstance(item, MatchImage):
                input_images.append(item)
            else:
                input_images.append(MatchImage(index, None, item))

        super().__init__(
            images=input_images,
            output_image_params=output_image_params,
            tag=tag,
            env=env,
            tenant=tenant
        )
