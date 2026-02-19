import base64

from regula.facesdk.webclient.gen.api.search_api import SearchApi as GenSearchApi
from regula.facesdk.webclient.gen.models.search_request import SearchRequest
from regula.facesdk.webclient.gen.models.search_result import SearchResult


class SearchApi(GenSearchApi):
    def search(self, search_request: SearchRequest, **kwargs) -> SearchResult:
        image = search_request.image
        if image is not None:
            search_request.image.content = base64.b64encode(image.content).decode("utf-8") if image.content else None
        return super().search(search_request, **kwargs)
