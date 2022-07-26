from regula.facesdk.webclient import SearchApi as GenSearchApi, ApiClient, SearchRequest, SearchResult


class SearchApi(GenSearchApi):
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)

    def search(self, search_request: SearchRequest, **kwargs) -> SearchResult:
        return super().search(search_request, **kwargs)
