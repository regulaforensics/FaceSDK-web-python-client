# compatibility import
from regula.facesdk.webclient.ext import MatchImage, MatchRequest
from regula.facesdk.webclient.gen.model.face_sdk_result import FaceSDKResult
from regula.facesdk.webclient.gen.model.face_sdk_result_code import FaceSDKResultCode
from regula.facesdk.webclient.gen.model.match_image_detection import MatchImageDetection
from regula.facesdk.webclient.gen.model.match_image_result import MatchImageResult
from regula.facesdk.webclient.gen.model.match_response import MatchResponse

FaceRecognitionResult = FaceSDKResult
FaceRecognitionResultCode = FaceSDKResultCode
CompareImage = MatchImage
CompareImageDetection = MatchImageDetection
CompareImageResult = MatchImageResult
CompareRequest = MatchRequest
CompareResponse = MatchResponse
