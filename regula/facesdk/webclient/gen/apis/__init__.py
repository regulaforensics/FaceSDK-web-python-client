
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.group_api import GroupApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from regula.facesdk.webclient.gen.api.group_api import GroupApi
from regula.facesdk.webclient.gen.api.healthcheck_api import HealthcheckApi
from regula.facesdk.webclient.gen.api.liveness_2_0_api import Liveness20Api
from regula.facesdk.webclient.gen.api.match_api import MatchApi
from regula.facesdk.webclient.gen.api.person_api import PersonApi
from regula.facesdk.webclient.gen.api.search_api import SearchApi
