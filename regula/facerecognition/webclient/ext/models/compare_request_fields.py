import base64
from typing import Optional, Union

from regula.facerecognition.webclient.ext.common import Base64String
from regula.facerecognition.webclient.gen import CompareRequestFields as GenCompareRequestFields, ImageSource


class CompareRequestFields(GenCompareRequestFields):
    def __init__(self, index=None, format=None, type=None, data: Optional[Union[Base64String, bytes]] = None, local_vars_configuration=None):
        if not type:
            type = ImageSource.LIVE
        if isinstance(data, bytes):
            data = base64.b64encode(data).decode("utf-8")

        super().__init__(index, format, type, data, local_vars_configuration)