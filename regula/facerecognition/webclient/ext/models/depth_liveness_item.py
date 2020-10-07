from typing import Union

from regula.facerecognition.webclient.ext.common import Base64String, bytes_to_base64
from regula.facerecognition.webclient.gen import DepthLivenessItem as GenDepthLivenessItem, ApiValueError


class DepthLivenessItem(GenDepthLivenessItem):
    def __init__(self, data_scene: Union[Base64String, bytes], data_depth: Union[Base64String, bytes], depth_scale: float, local_vars_configuration=None):
        if not data_scene:
            raise ApiValueError("depth liveness frame: expected <not empty>")

        if not data_depth:
            raise ApiValueError("depth liveness depth: expected <not empty>")

        if isinstance(data_scene, bytes):
            data_scene = bytes_to_base64(data_scene)

        if isinstance(data_depth, bytes):
            data_depth = bytes_to_base64(data_depth)

        super().__init__(data_scene, data_depth, depth_scale, local_vars_configuration)
