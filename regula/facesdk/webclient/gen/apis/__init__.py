
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.diagnostic_api import DiagnosticApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from regula.facesdk.webclient.gen.api.diagnostic_api import DiagnosticApi
from regula.facesdk.webclient.gen.api.face_comparison_api import FaceComparisonApi
from regula.facesdk.webclient.gen.api.face_detection_api import FaceDetectionApi
from regula.facesdk.webclient.gen.api.face_identification_api import FaceIdentificationApi
from regula.facesdk.webclient.gen.api.liveness_assessment_api import LivenessAssessmentApi
