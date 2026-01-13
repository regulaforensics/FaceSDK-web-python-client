from regula.facesdk.webclient.gen import Configuration, ApiClient
from regula.facesdk.webclient.gen.api import MatchApi as GenMatchApi


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

    def __exit__(self, exc_type, exc_value, traceback):
        pass
