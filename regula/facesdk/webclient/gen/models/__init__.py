# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from regula.facesdk.webclient.gen.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from regula.facesdk.webclient.gen.model.add_image_to_person_request import AddImageToPersonRequest
from regula.facesdk.webclient.gen.model.add_image_to_person_request_image import AddImageToPersonRequestImage
from regula.facesdk.webclient.gen.model.add_image_to_person_response import AddImageToPersonResponse
from regula.facesdk.webclient.gen.model.attribute_config import AttributeConfig
from regula.facesdk.webclient.gen.model.attribute_config_list import AttributeConfigList
from regula.facesdk.webclient.gen.model.crop import Crop
from regula.facesdk.webclient.gen.model.detect_request import DetectRequest
from regula.facesdk.webclient.gen.model.detect_response import DetectResponse
from regula.facesdk.webclient.gen.model.detect_response_all_of import DetectResponseAllOf
from regula.facesdk.webclient.gen.model.detect_result import DetectResult
from regula.facesdk.webclient.gen.model.detection import Detection
from regula.facesdk.webclient.gen.model.detection_attributes import DetectionAttributes
from regula.facesdk.webclient.gen.model.detection_face import DetectionFace
from regula.facesdk.webclient.gen.model.detection_quality import DetectionQuality
from regula.facesdk.webclient.gen.model.face_attribute import FaceAttribute
from regula.facesdk.webclient.gen.model.face_image_quality_align_type import FaceImageQualityAlignType
from regula.facesdk.webclient.gen.model.face_image_quality_groups import FaceImageQualityGroups
from regula.facesdk.webclient.gen.model.face_image_quality_groups_strings import FaceImageQualityGroupsStrings
from regula.facesdk.webclient.gen.model.face_image_quality_status import FaceImageQualityStatus
from regula.facesdk.webclient.gen.model.face_quality_config_name import FaceQualityConfigName
from regula.facesdk.webclient.gen.model.face_quality_scenarios import FaceQualityScenarios
from regula.facesdk.webclient.gen.model.face_rectangular import FaceRectangular
from regula.facesdk.webclient.gen.model.face_sdk_result import FaceSDKResult
from regula.facesdk.webclient.gen.model.face_sdk_result_code import FaceSDKResultCode
from regula.facesdk.webclient.gen.model.faces_response import FacesResponse
from regula.facesdk.webclient.gen.model.faces_response_all_of import FacesResponseAllOf
from regula.facesdk.webclient.gen.model.filter_op import FilterOp
from regula.facesdk.webclient.gen.model.filter_search_request import FilterSearchRequest
from regula.facesdk.webclient.gen.model.group import Group
from regula.facesdk.webclient.gen.model.group_all_of import GroupAllOf
from regula.facesdk.webclient.gen.model.group_page import GroupPage
from regula.facesdk.webclient.gen.model.group_page_all_of import GroupPageAllOf
from regula.facesdk.webclient.gen.model.group_response import GroupResponse
from regula.facesdk.webclient.gen.model.group_to_create import GroupToCreate
from regula.facesdk.webclient.gen.model.image import Image
from regula.facesdk.webclient.gen.model.image_fields import ImageFields
from regula.facesdk.webclient.gen.model.image_page import ImagePage
from regula.facesdk.webclient.gen.model.image_page_all_of import ImagePageAllOf
from regula.facesdk.webclient.gen.model.image_source import ImageSource
from regula.facesdk.webclient.gen.model.liveness_type import LivenessType
from regula.facesdk.webclient.gen.model.match_and_search_request import MatchAndSearchRequest
from regula.facesdk.webclient.gen.model.match_and_search_request_all_of import MatchAndSearchRequestAllOf
from regula.facesdk.webclient.gen.model.match_and_search_request_all_of_images import MatchAndSearchRequestAllOfImages
from regula.facesdk.webclient.gen.model.match_and_search_response import MatchAndSearchResponse
from regula.facesdk.webclient.gen.model.match_and_search_response_all_of import MatchAndSearchResponseAllOf
from regula.facesdk.webclient.gen.model.match_and_search_response_all_of_detections import MatchAndSearchResponseAllOfDetections
from regula.facesdk.webclient.gen.model.match_image import MatchImage
from regula.facesdk.webclient.gen.model.match_image_detection import MatchImageDetection
from regula.facesdk.webclient.gen.model.match_image_result import MatchImageResult
from regula.facesdk.webclient.gen.model.match_request import MatchRequest
from regula.facesdk.webclient.gen.model.match_response import MatchResponse
from regula.facesdk.webclient.gen.model.match_response_all_of import MatchResponseAllOf
from regula.facesdk.webclient.gen.model.operation_log import OperationLog
from regula.facesdk.webclient.gen.model.output_image_params import OutputImageParams
from regula.facesdk.webclient.gen.model.page import Page
from regula.facesdk.webclient.gen.model.person import Person
from regula.facesdk.webclient.gen.model.person_all_of import PersonAllOf
from regula.facesdk.webclient.gen.model.person_fields import PersonFields
from regula.facesdk.webclient.gen.model.person_to_update_fields import PersonToUpdateFields
from regula.facesdk.webclient.gen.model.person_with_images import PersonWithImages
from regula.facesdk.webclient.gen.model.person_with_images_all_of import PersonWithImagesAllOf
from regula.facesdk.webclient.gen.model.persons_page import PersonsPage
from regula.facesdk.webclient.gen.model.persons_page_all_of import PersonsPageAllOf
from regula.facesdk.webclient.gen.model.process_param import ProcessParam
from regula.facesdk.webclient.gen.model.process_param_attributes import ProcessParamAttributes
from regula.facesdk.webclient.gen.model.quality_config import QualityConfig
from regula.facesdk.webclient.gen.model.quality_config_list import QualityConfigList
from regula.facesdk.webclient.gen.model.quality_detail import QualityDetail
from regula.facesdk.webclient.gen.model.quality_details_groups import QualityDetailsGroups
from regula.facesdk.webclient.gen.model.quality_request import QualityRequest
from regula.facesdk.webclient.gen.model.rgb import RGB
from regula.facesdk.webclient.gen.model.recognize_image import RecognizeImage
from regula.facesdk.webclient.gen.model.recognize_image_all_of import RecognizeImageAllOf
from regula.facesdk.webclient.gen.model.resize_options import ResizeOptions
from regula.facesdk.webclient.gen.model.search_bad_params import SearchBadParams
from regula.facesdk.webclient.gen.model.search_detection import SearchDetection
from regula.facesdk.webclient.gen.model.search_parameters import SearchParameters
from regula.facesdk.webclient.gen.model.search_parameters_create_person import SearchParametersCreatePerson
from regula.facesdk.webclient.gen.model.search_person import SearchPerson
from regula.facesdk.webclient.gen.model.search_person_all_of import SearchPersonAllOf
from regula.facesdk.webclient.gen.model.search_request import SearchRequest
from regula.facesdk.webclient.gen.model.search_result import SearchResult
from regula.facesdk.webclient.gen.model.transaction_info import TransactionInfo
from regula.facesdk.webclient.gen.model.update_group import UpdateGroup
