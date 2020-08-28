from typing import Optional, List

from regula.facerecognition.webclient.ext.models.compare_request_fields import CompareRequestFields
from regula.facerecognition.webclient.gen import CompareRequest as GenCompareRequest


class CompareRequest(GenCompareRequest):
    def __init__(self, images: Optional[List[CompareRequestFields]] = None, local_vars_configuration=None):
        super().__init__(images, local_vars_configuration)
