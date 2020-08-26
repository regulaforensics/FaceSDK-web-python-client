from regula.face.webclient.gen import MatchingApi as GenMatchingApi, Configuration, ApiClient, CompareResponse


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

    def compare(self, compare_request, **kwargs) -> CompareResponse:
        return super().compare(compare_request, **kwargs)
