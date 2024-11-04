from typing import List

from regula.facesdk.webclient.gen import Configuration, ApiClient
from regula.facesdk.webclient.gen.apis import MatchApi as GenMatchApi
from regula.facesdk.webclient.ext.models import MatchRequest, DetectRequest
from regula.facesdk.webclient.gen.model.detect_response import DetectResponse
from regula.facesdk.webclient.gen.model.match_and_search_request import MatchAndSearchRequest
from regula.facesdk.webclient.gen.model.match_and_search_request_all_of_images import MatchAndSearchRequestAllOfImages
from regula.facesdk.webclient.gen.model.match_and_search_response import MatchAndSearchResponse
from regula.facesdk.webclient.gen.model.match_response import MatchResponse


class MatchApi(GenMatchApi):
    def __init__(self, host=None, debug=False, verify_ssl=False, api_client=None):
        if api_client:
            super().__init__(api_client)
        else:
            configuration = Configuration(host=host)
            configuration.debug = debug
            configuration.verify_ssl = verify_ssl

            super().__init__(ApiClient(configuration=configuration))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.api_client.close()

    def match_and_search(self, images: List[MatchAndSearchRequestAllOfImages], group_ids: List[int],
                         limit: int = 100, threshold: float = 1.0) -> MatchAndSearchResponse:
        body = MatchAndSearchRequest(
            images=images,
            group_ids=group_ids
        )
        return super().match_and_search(body)

    def match(self, match_request: MatchRequest, **kwargs) -> MatchResponse:
        return super().match(match_request, **kwargs)

    # deprecated use match
    def compare(self, compare_request: MatchRequest, **kwargs) -> MatchResponse:
        return super().match(compare_request, **kwargs)

    def detect(self, detect_request: DetectRequest, **kwargs) -> DetectResponse:
        return super().detect(detect_request, **kwargs)
