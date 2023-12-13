from regula.facesdk.webclient.gen.model.image_source import ImageSource
from regula.facesdk.webclient import MatchImage, MatchRequest
from tests.misc.paths_and_urls import *


def validate_response(response, expected_detections_count, expected_first, expected_second=None):
    assert response['code'] == 0, f"Unexpected response code: {response['code']}"
    assert isinstance(response.get('detections', []), list), "'detections' field should be an array"
    assert len(response.get('detections', [])) == expected_detections_count, \
        f"'detections' array should have {expected_detections_count} entries"
    assert 'results' in response, "'results' field not found in response"
    assert isinstance(response['results'], list), "'results' should be an array"
    assert response['results'][0]['first'] == expected_first, f"Expected 'first' to be {expected_first}"
    if expected_second is not None:
        assert response['results'][0].get('second',
                                          None) == expected_second, f"Expected 'second' to be {expected_second}"


def create_match_request(type1, path1, type2=None, path2=None):
    images = [MatchImage(index=1, data=read_image_bytes(path1), type=type1)]
    if type2 and path2:
        images.append(MatchImage(index=2, data=read_image_bytes(path2), type=type2))
    return MatchRequest(images=images)


def test_matching_api(facesdk):
    match_request = create_match_request(ImageSource.LIVE, FACE_1_PATH, ImageSource.DOCUMENT_RFID, FACE_1_PATH)
    response_dict = create_dictionary(facesdk.matching_api.match(match_request))
    validate_response(response_dict, expected_detections_count=2, expected_first=3, expected_second=2)


def test_liveAndPrintedDoc_type(facesdk):
    match_request = create_match_request(ImageSource.DOCUMENT_PRINTED, PRINTED_DOCUMENT_PATH, ImageSource.LIVE,
                                         LIVE_PHOTO_PATH)
    response_dict = create_dictionary(facesdk.matching_api.match(match_request))
    validate_response(response_dict, expected_detections_count=2, expected_first=1, expected_second=3)


def test_docWithLive_type(facesdk):
    match_request = create_match_request(ImageSource.DOCUMENT_WITH_LIVE, DOCUMENT_WITH_LIVE_PATH)
    response_dict = create_dictionary(facesdk.matching_api.match(match_request))
    validate_response(response_dict, expected_detections_count=1, expected_first=4)


def test_external_type(facesdk):
    match_request = create_match_request(ImageSource.DOCUMENT_PRINTED, PRINTED_DOCUMENT_PATH, ImageSource.EXTERNAL,
                                         LIVE_PHOTO_PATH)
    response_dict = create_dictionary(facesdk.matching_api.match(match_request))
    validate_response(response_dict, expected_detections_count=2, expected_first=1, expected_second=5)


def test_documentRFID_type(facesdk):
    match_request = create_match_request(ImageSource.DOCUMENT_PRINTED, PRINTED_DOCUMENT_PATH, ImageSource.DOCUMENT_RFID,
                                         LIVE_PHOTO_PATH)
    response_dict = create_dictionary(facesdk.matching_api.match(match_request))
    validate_response(response_dict, expected_detections_count=2, expected_first=1, expected_second=2)


def test_ghost_type(facesdk):
    match_request = create_match_request(ImageSource.DOCUMENT_PRINTED, PRINTED_DOCUMENT_PATH, ImageSource.GHOST,
                                         LIVE_PHOTO_PATH)
    response_dict = create_dictionary(facesdk.matching_api.match(match_request))
    validate_response(response_dict, expected_detections_count=2, expected_first=1, expected_second=6)
