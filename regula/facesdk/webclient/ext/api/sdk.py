from regula.facesdk.webclient.ext.api import MatchingApi
from regula.facesdk.webclient.ext.api import PersonApi
from regula.facesdk.webclient.ext.api.group_api import GroupApi
from regula.facesdk.webclient.ext.api.search_api import SearchApi
from regula.facesdk.webclient.gen import ApiClient, Configuration


class FaceSdk:
    def __init__(self, host=None, debug=None, verify_ssl=False, api_client=None):
        if api_client:
            self.__api_client = api_client
        else:
            configuration = Configuration(host=host)
            configuration.debug = debug
            configuration.verify_ssl = verify_ssl

            self.__api_client = ApiClient(configuration=configuration)

        self.matching_api = MatchingApi(api_client=self.__api_client)
        self.person_api = PersonApi(api_client=self.__api_client)
        self.group_api = GroupApi(api_client=self.__api_client)
        self.search_api = SearchApi(api_client=self.__api_client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__api_client.close()
