# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from regula.facesdk.webclient.gen.api.group_api import GroupApi
    from regula.facesdk.webclient.gen.api.healthcheck_api import HealthcheckApi
    from regula.facesdk.webclient.gen.api.liveness20_api import Liveness20Api
    from regula.facesdk.webclient.gen.api.match_api import MatchApi
    from regula.facesdk.webclient.gen.api.person_api import PersonApi
    from regula.facesdk.webclient.gen.api.search_api import SearchApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from regula.facesdk.webclient.gen.api.group_api import GroupApi
from regula.facesdk.webclient.gen.api.healthcheck_api import HealthcheckApi
from regula.facesdk.webclient.gen.api.liveness20_api import Liveness20Api
from regula.facesdk.webclient.gen.api.match_api import MatchApi
from regula.facesdk.webclient.gen.api.person_api import PersonApi
from regula.facesdk.webclient.gen.api.search_api import SearchApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
