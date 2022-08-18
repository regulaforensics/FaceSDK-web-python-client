from regula.facesdk.webclient.gen import ApiClient
from regula.facesdk.webclient.gen.api.search_api import SearchApi as GenSearchApi
from regula.facesdk.webclient.gen.model.search_request import SearchRequest
from regula.facesdk.webclient.gen.model.search_result import SearchResult


class SearchApi(GenSearchApi):
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)

    def search(self, search_request: SearchRequest, **kwargs) -> SearchResult:
        return super().search(search_request, **kwargs)
