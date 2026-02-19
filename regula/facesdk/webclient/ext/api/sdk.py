from regula.facesdk.webclient.ext.api import MatchApi
from regula.facesdk.webclient.ext.api import PersonApi
from regula.facesdk.webclient.ext.api.group_api import GroupApi
from regula.facesdk.webclient.ext.api.search_api import SearchApi
from regula.facesdk.webclient.gen import ApiClient, Configuration, HealthcheckApi, Liveness20Api


class FaceSdk:
    def __init__(self, host=None, debug=None, verify_ssl=True, api_client=None):
        if api_client:
            self.__api_client = api_client
        else:
            configuration = Configuration(host=host)
            configuration.debug = debug
            configuration.verify_ssl = verify_ssl

            self.__api_client = ApiClient(configuration=configuration)

        self.match_api = MatchApi(api_client=self.__api_client)
        self.person_api = PersonApi(api_client=self.__api_client)
        self.group_api = GroupApi(api_client=self.__api_client)
        self.search_api = SearchApi(api_client=self.__api_client)
        self.healthcheck = HealthcheckApi(api_client=self.__api_client)
        self.liveness = Liveness20Api(api_client=self.__api_client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
