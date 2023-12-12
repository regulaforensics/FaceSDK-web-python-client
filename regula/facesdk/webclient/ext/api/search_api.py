import base64

from regula.facesdk.webclient.gen import ApiClient
from regula.facesdk.webclient.gen.api.search_api import SearchApi as GenSearchApi
from regula.facesdk.webclient.gen.model.search_request import SearchRequest
from regula.facesdk.webclient.gen.model.search_result import SearchResult


class SearchApi(GenSearchApi):
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)

    def search(self, search_request: SearchRequest, **kwargs) -> SearchResult:
        image = search_request.image
        if image is not None:
            search_request.image.content = base64.b64encode(image.content).decode("utf-8") if image.content else None
        return super().search(search_request, **kwargs)
