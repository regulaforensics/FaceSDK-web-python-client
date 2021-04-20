from regula.facesdk.webclient.gen import MatchingApi as GenMatchingApi, Configuration, ApiClient, \
    DetectResponse, MatchResponse
from regula.facesdk.webclient.ext.models import MatchRequest, DetectRequest


class MatchingApi(GenMatchingApi):
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

    def match(self, match_request: MatchRequest, **kwargs) -> MatchResponse:
        return super().match(match_request, **kwargs)

    # deprecated use match
    def compare(self, compare_request: MatchRequest, **kwargs) -> MatchResponse:
        return super().match(compare_request, **kwargs)

    def detect(self, detect_request: DetectRequest, **kwargs) -> DetectResponse:
        return super().detect(detect_request, **kwargs)
