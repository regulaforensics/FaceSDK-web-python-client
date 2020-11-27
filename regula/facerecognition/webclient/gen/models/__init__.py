# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from regula.facerecognition.webclient.gen.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from regula.facerecognition.webclient.gen.model.compare_image import CompareImage
from regula.facerecognition.webclient.gen.model.compare_image_result import CompareImageResult
from regula.facerecognition.webclient.gen.model.compare_request import CompareRequest
from regula.facerecognition.webclient.gen.model.compare_response import CompareResponse
from regula.facerecognition.webclient.gen.model.compare_response_all_of import CompareResponseAllOf
from regula.facerecognition.webclient.gen.model.detect_request import DetectRequest
from regula.facerecognition.webclient.gen.model.detect_response import DetectResponse
from regula.facerecognition.webclient.gen.model.detect_response_all_of import DetectResponseAllOf
from regula.facerecognition.webclient.gen.model.detect_result import DetectResult
from regula.facerecognition.webclient.gen.model.detection import Detection
from regula.facerecognition.webclient.gen.model.face_recognition_result import FaceRecognitionResult
from regula.facerecognition.webclient.gen.model.face_recognition_result_code import FaceRecognitionResultCode
from regula.facerecognition.webclient.gen.model.face_rectangular import FaceRectangular
from regula.facerecognition.webclient.gen.model.image_source import ImageSource
from regula.facerecognition.webclient.gen.model.operation_log import OperationLog
